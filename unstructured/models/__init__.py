# -*- coding: utf-8 -*-

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
import warnings

# TODO: Don't use wildcards
from article import *
from section import *
from urlpath import *

# TODO: Should the below stuff be executed a more logical place?

######################
# Configuration stuff
######################

if not 'mptt' in django_settings.INSTALLED_APPS:
    raise ImproperlyConfigured('django-unstructured: needs mptt in INSTALLED_APPS')

######################
# Warnings
######################

if not 'south' in django_settings.INSTALLED_APPS:
    warnings.warn("django-unstructured: No south in your INSTALLED_APPS. This is highly discouraged.")
