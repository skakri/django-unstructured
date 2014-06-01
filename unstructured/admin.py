from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from mptt.admin import MPTTModelAdmin
from django import forms
from models.section import *
from models.urlpath import URLPath


class SectionObjectAdmin(GenericTabularInline):
    model = SectionForObject
    extra = 1
    max_num = 1


class SectionRevisionForm(forms.ModelForm):
    
    class Meta:
        model = SectionRevision
        
    def __init__(self, *args, **kwargs):
        super(SectionRevisionForm, self).__init__(*args, **kwargs)


class SectionRevisionAdmin(admin.ModelAdmin):
    form = SectionRevisionForm
    list_display = ('title', 'created', 'modified', 'user', 'ip_address')


class SectionRevisionInline(admin.TabularInline):
    model = SectionRevision
    form = SectionRevisionForm
    fk_name = 'article'
    extra = 1
    fields = ('content', 'title',  'deleted', 'locked',)


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            revisions = SectionRevision.objects.filter(article=self.instance)
            self.fields['current_revision'].queryset = revisions
        else:
            self.fields['current_revision'].queryset = SectionRevision.objects.get_empty_query_set()
            self.fields['current_revision'].widget = forms.HiddenInput()


class SectionAdmin(admin.ModelAdmin):
    inlines = [SectionRevisionInline]
    form = SectionForm


class URLPathAdmin(MPTTModelAdmin):
    inlines = [SectionObjectAdmin]
    list_filter = ('site', 'articles__article__deleted',
                   'articles__article__created',
                   'articles__article__modified')
    list_display = ('__unicode__', 'article', 'get_created')

    def get_created(self, instance):
        return instance.article.created
    
admin.site.register(URLPath, URLPathAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SectionRevision, SectionRevisionAdmin)
