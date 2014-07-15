from django.db import models
from django.db.models.query import QuerySet

class SectionFkManager(models.Manager):
    def active(self):
        return self.get_query_set().active()

    def can_read(self, user):
        return self.get_query_set().can_read(user)

    def can_write(self, user):
        return self.get_query_set().can_write(user)
