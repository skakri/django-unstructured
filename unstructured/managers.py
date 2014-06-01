from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet, EmptyQuerySet
from mptt.managers import TreeManager


class PermissionEmptyQuerySet(EmptyQuerySet):
    def can_read(self, _):
        return self

    def can_write(self, _):
        return self

    def active(self):
        return self


class PermissionQuerySet(QuerySet):
    def can_read(self, user):
        """Filter objects so only the ones with a user's reading access
        are included"""
        if user.has_perm('unstructured.moderator'):
            return self
        if user.is_anonymous():
            q = self.filter(other_read=True)
        else:
            q = self.filter(Q(other_read=True) |
                            Q(owner=user) |
                            (Q(group__user=user) & Q(group_read=True))
                            )
        return q

    def can_write(self, user):
        """Filter objects so only the ones with a user's writing access
        are included"""
        if user.has_perm('unstructured.moderator'):
            return self
        if user.is_anonymous():
            q = self.filter(other_write=True)
        else:
            q = self.filter(Q(other_write=True) |
                            Q(owner=user) |
                            (Q(group__user=user) & Q(group_write=True))
                            )
        return q

    def active(self):
        return self.filter(current_revision__deleted=False)


class SectionFkQuerySetMixin():
    def can_read(self, user):
        """Filter objects so only the ones with a user's reading access
        are included"""
        if user.has_perm('unstructured.moderate'):
            return self
        if user.is_anonymous():
            q = self.filter(section__other_read=True)
        else:
            # https://github.com/benjaoming/django-wiki/issues/67
            q = self.filter(Q(section__other_read=True) |
                            Q(section__owner=user) |
                            (Q(section__group__user=user) & Q(section__group_read=True))
                            ).distinct()
        return q

    def can_write(self, user):
        """Filter objects so only the ones with a user's writing access
        are included"""
        if user.has_perm('unstructured.moderate'):
            return self
        if user.is_anonymous():
            q = self.filter(section__other_write=True)
        else:
            # https://github.com/benjaoming/django-wiki/issues/67
            q = self.filter(Q(section__other_write=True) |
                            Q(section__owner=user) |
                            (Q(section__group__user=user) & Q(section__group_write=True))
                            ).distinct()
        return q

    def active(self):
        return self.filter(section__current_revision__deleted=False)


class SectionFkEmptyQuerySetMixin():
    def can_read(self, _):
        return self

    def can_write(self, _):
        return self

    def active(self):
        return self


class SectionFkQuerySet(SectionFkQuerySetMixin, QuerySet):
    pass


class SectionFkEmptyQuerySet(SectionFkEmptyQuerySetMixin, EmptyQuerySet):
    pass


class PermissionManager(models.Manager):
    def get_empty_query_set(self):
        return PermissionEmptyQuerySet(model=self.model)

    def get_query_set(self):
        return PermissionQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()

    def can_read(self, user):
        return self.get_query_set().can_read(user)

    def can_write(self, user):
        return self.get_query_set().can_write(user)


class SectionFkManager(models.Manager):
    def get_empty_query_set(self):
        return SectionFkEmptyQuerySet(model=self.model)

    def get_query_set(self):
        return SectionFkQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()

    def can_read(self, user):
        return self.get_query_set().can_read(user)

    def can_write(self, user):
        return self.get_query_set().can_write(user)


class URLPathEmptyQuerySet(EmptyQuerySet, SectionFkEmptyQuerySetMixin):
    def select_related_common(self):
        return self


class URLPathQuerySet(QuerySet, SectionFkQuerySetMixin):
    def select_related_common(self):
        return self.select_related(
            'parent',
            'section__current_revision',
            'section__owner'
        )


class URLPathManager(TreeManager):

    def get_empty_query_set(self):
        return URLPathEmptyQuerySet(model=self.model)

    def get_query_set(self):
        """Return a QuerySet with the same ordering as the TreeManager."""
        return URLPathQuerySet(self.model, using=self._db).order_by(
            self.tree_id_attr,
            self.left_attr
        )

    def select_related_common(self):
        return self.get_query_set().common_select_related()

    def active(self):
        return self.get_query_set().active()

    def can_read(self, user):
        return self.get_query_set().can_read(user)

    def can_write(self, user):
        return self.get_query_set().can_write(user)
