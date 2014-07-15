# -*- coding: utf-8 -*-
from mptt.models import TreeForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel
from mptt.managers import TreeManager

from django.db.models.signals import post_save, pre_delete
from unstructured.conf import settings
from unstructured.core import compat
from unstructured.models.revision import BaseRevisionMixin


class SectionForObject(models.Model):
    # Override-able settings.
    section_model = 'Section'

    section = models.ForeignKey(
        section_model,
        on_delete=models.CASCADE)
    # Same as django.contrib.comments
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name='content_type_set_for_%(class)s'
    )
    object_id = models.PositiveIntegerField(_('object ID'))
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    is_mptt = models.BooleanField(default=False, editable=False)

    class Meta:
        app_label = settings.APP_LABEL
        abstract = True
        verbose_name = _(u'Section for object')
        verbose_name_plural = _(u'Section for object')
        # Do not allow several objects
        unique_together = ('content_type', 'object_id')


class Section(MPTTModel):
    # Override-able settings.
    revision_model = 'SectionRevision'
    section_for_object_cls = SectionForObject

    objects = TreeManager()

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children'
    )

    slug = models.SlugField(
        verbose_name=_(u'slug'),
        null=True,
        blank=True,
        max_length=50
    )

    current_revision = models.OneToOneField(
        revision_model,
        verbose_name=_(u'current revision'),
        blank=True,
        null=True,
        related_name='current_set',
        help_text=_(
            u'The revision being displayed for this section. '
            u'If you need to do a roll-back, simply change the '
            u'value of this field.'
        ),
    )

    latest_revision = models.OneToOneField(
        revision_model,
        verbose_name=_(u'latest revision'),
        blank=True,
        null=True,
        related_name='latest_set',
        help_text=_(
            u'Latest revision that has been created.'
        ),
    )

    deleted = models.BooleanField(
        verbose_name=_(u'deleted'),
        default=False,
    )

    locked = models.BooleanField(
        verbose_name=_(u'locked'),
        default=False,
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'created'),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'modified'),
        help_text=_(u'Section properties last modified')
    )

    owner = models.ForeignKey(
        compat.USER_MODEL,
        verbose_name=_('owner'),
        blank=True, null=True, related_name='owned_sections',
        help_text=_(u'The owner of the section, usually the creator. '
                    u'The owner always has both read and write access.'),
        on_delete=models.SET_NULL
    )

    def add_revision(self, new_revision, save=True, switch=True):
        """
        Sets the properties of a new revision.
        If switch is truthy -- sets as current revision.
        """
        assert self.id or save, (
            u'add_revision: Sorry, you cannot add a'
            u'revision to an section that has not been saved '
            u'without using save=True'
        )
        if not self.id:
            self.save()

        revisions = self.sectionrevision_set.all()

        try:
            latest_revision = revisions.latest()
            new_revision.revision_number = latest_revision.revision_number + 1
        except:
            new_revision.revision_number = 0
        new_revision.section = self
        new_revision.previous_revision = self.current_revision

        if save:
            new_revision.save()

        self.latest_revision = new_revision
        if switch:
            self.current_revision = new_revision
        if save:
            self.save()

    def add_object_relation(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        is_mptt = isinstance(obj, MPTTModel)
        rel = self.section_for_object_cls.objects.get_or_create(
            section=self,
            content_type=content_type,
            object_id=obj.id,
            is_mptt=is_mptt
        )
        return rel

    @classmethod
    def get_for_object(cls, obj):
        return cls.section_for_object_cls.objects.get(
            object_id=obj.id,
            content_type=ContentType.objects.get_for_model(obj)
        ).section

    def __unicode__(self):
        if self.current_revision:
            return self.current_revision.title
        obj_name = _(u'Section without content (%(id)d)') % {
            'id': self.id or 0
        }
        return unicode(obj_name)

    class MPTTMeta:
        def __init__(self):
            pass
        pass

    class Meta:
        app_label = settings.APP_LABEL
        abstract = True
        unique_together = ('parent', 'slug')


class SectionRevision(BaseRevisionMixin, models.Model):
    """
    This is where main revision data is stored. To make it easier to
    copy, do NEVER create m2m relationships.
    """
    # Override-able settings.
    section_model = 'Section'

    section = models.ForeignKey(
        section_model,
        on_delete=models.CASCADE,
        verbose_name=_(u'section')
    )

    # This is where the content goes, with whatever markup language is used
    content = models.TextField(blank=True, verbose_name=_(u'section contents'))

    # This title is automatically set from either the section's title or
    # the last used revision...
    title = models.CharField(
        max_length=512,
        verbose_name=_(u'section title'),
        null=False,
        blank=False,
        help_text=_(
            u'Each section contains a title field that must be filled out, '
            u'even if the title has not changed'
        )
    )

    def __unicode__(self):
        return 'SectionRevision: %s (%d)' % (
            self.title, self.revision_number or 0
        )

    def inherit_predecessor(self, section):
        """
        Inherit certain properties from predecessor because it's very
        convenient. Remember to always call this method before
        setting properties :)"""
        predecessor = section.current_revision
        self.section = predecessor.section
        self.content = predecessor.content
        self.title = predecessor.title

    def save(self, *args, **kwargs):
        if (not self.id
                and not self.previous_revision
                and self.section
                and self.section.current_revision
                and self.section.current_revision != self):

            self.previous_revision = self.section.current_revision

        self.section.latest_revision = self

        if not self.revision_number:
            try:
                previous_revision = self.section.sectionrevision_set.latest()
                self.revision_number = previous_revision.revision_number + 1
            except:
                self.revision_number = 1

        super(SectionRevision, self).save(*args, **kwargs)

        if not self.section.current_revision:
            # If I'm saved from Django admin,
            # then section.current_revision is me!
            self.section.current_revision = self
            self.section.save()

    class Meta:
        app_label = settings.APP_LABEL
        abstract = True
        get_latest_by = 'revision_number'
        ordering = ('created',)
        unique_together = ('section', 'revision_number')


######################################################
# SIGNAL HANDLERS
######################################################

# clear the ancestor cache when saving or deleting sections so things like
# section_lists will be refreshed
def _clear_ancestor_cache(section):
    for ancestor in section.ancestor_objects():
        ancestor.section.clear_cache()


def on_section_save_clear_cache(instance, **_):
    _clear_ancestor_cache(instance)
post_save.connect(
    on_section_save_clear_cache,
    Section,
    'unstructured.models.Section.save'
)


def on_section_delete_clear_cache(instance, **_):
    _clear_ancestor_cache(instance)
    instance.clear_cache()
pre_delete.connect(
    on_section_delete_clear_cache,
    Section,
    'unstructured.models.Section.delete'
)
