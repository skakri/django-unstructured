# -*- coding: utf-8 -*-
# from django.db import models
from unstructured.models.section import Section as SectionMixin
from unstructured.models.section import SectionRevision as SectionRevisionMixin


class Section(SectionMixin):
    revision_model = 'example.SectionRevision'


class SectionRevision(SectionRevisionMixin):
    pass
