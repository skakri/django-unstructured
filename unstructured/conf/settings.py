# -*- coding: utf-8 -*-
from django.conf import settings as django_settings

APP_LABEL = getattr(
    django_settings,
    'UNSTRUCTURED_APP_LABEL',
    'unstructured'
)

LOG_IPS_ANONYMOUS = getattr(
    django_settings,
    'UNSTRUCTURED_LOG_IPS_ANONYMOUS',
    True
)

LOG_IPS_USERS = getattr(
    django_settings,
    'UNSTRUCTURED_LOG_IPS_USERS',
    True
)
