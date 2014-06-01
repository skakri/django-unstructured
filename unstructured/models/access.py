# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import ugettext_lazy as _

from unstructured.conf import settings
from unstructured.core import permissions
from unstructured import managers


class GroupMixin(models.Model):
    objects = managers.PermissionManager()

    group = models.ForeignKey(
        Group, verbose_name=_('group'),
        blank=True, null=True,
        help_text=_(
            u'Like in a UNIX file system, permissions can be given to a user '
            u'according to group membership. '
            u'Groups are handled through the Django auth system.'),
        on_delete=models.SET_NULL
    )

    group_read = models.BooleanField(
        default=True,
        verbose_name=_(u'group read access')
    )
    group_write = models.BooleanField(
        default=True,
        verbose_name=_(u'group write access')
    )
    other_read = models.BooleanField(
        default=True,
        verbose_name=_(u'others read access')
    )
    other_write = models.BooleanField(
        default=True,
        verbose_name=_(u'others write access')
    )

    # PERMISSIONS
    def can_read(self, user):
        return permissions.can_read(self, user)

    def can_write(self, user):
        return permissions.can_write(self, user)

    def can_delete(self, user):
        return permissions.can_delete(self, user)

    def can_moderate(self, user):
        return permissions.can_moderate(self, user)

    def can_assign(self, user):
        return permissions.can_assign(self, user)

    # All recursive permission methods will use descendant_objects to access
    # generic relations and check if they are using MPTT
    # and have INHERIT_PERMISSIONS=True
    def set_permissions_recursive(self):
        for descendant in self.descendant_objects():
            if descendant.INHERIT_PERMISSIONS:
                descendant.section.group_read = self.group_read
                descendant.section.group_write = self.group_write
                descendant.section.other_read = self.other_read
                descendant.section.other_write = self.other_write
                descendant.section.save()

    def set_group_recursive(self):
        for descendant in self.descendant_objects():
            if descendant.INHERIT_PERMISSIONS:
                descendant.section.group = self.group
                descendant.section.save()

    def set_owner_recursive(self):
        for descendant in self.descendant_objects():
            if descendant.INHERIT_PERMISSIONS:
                descendant.section.owner = self.owner
                descendant.section.save()

    class Meta:
        app_label = settings.APP_LABEL
        abstract = True

        permissions = (
            ("moderate", _(u"can edit all sections and lock/unlock/restore")),
            ("assign", _(u"can change ownership of any section")),
            ("grant", _(u"can assign permissions to other users")),
        )
