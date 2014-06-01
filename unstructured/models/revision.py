# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from unstructured.core import compat
from unstructured.conf import settings


class BaseRevisionMixin(models.Model):
    """This is an abstract model used as a mixin: Do not override any of the
    core model methods but respect the inheritor's freedom to do so itself."""

    revision_number = models.IntegerField(
        editable=False,
        verbose_name=_(u'revision number')
    )

    user_message = models.TextField(blank=True,)
    automatic_log = models.TextField(blank=True, editable=False,)

    ip_address = models.IPAddressField(
        _('IP address'),
        blank=True,
        null=True,
        editable=False
    )
    user = models.ForeignKey(
        compat.USER_MODEL, verbose_name=_('user'),
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    previous_revision = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL
    )

    def set_from_request(self, request):
        if request.user.is_authenticated():
            self.user = request.user
            if settings.LOG_IPS_USERS:
                self.ip_address = request.META.get('REMOTE_ADDR', None)
        elif settings.LOG_IPS_ANONYMOUS:
            self.ip_address = request.META.get('REMOTE_ADDR', None)

    class Meta:
        abstract = True
