# -*- coding: utf-8 -*-
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
import warnings

# Configuration issues.

if not 'mptt' in django_settings.INSTALLED_APPS:
    raise ImproperlyConfigured(
        u'django-unstructured: needs mptt in INSTALLED_APPS.'
    )

# Warnings.

if not 'south' in django_settings.INSTALLED_APPS:
    warnings.warn(
        u'django-unstructured: No south in your INSTALLED_APPS. '
        u'This is highly discouraged.'
    )
