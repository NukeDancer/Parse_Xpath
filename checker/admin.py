from django.contrib import admin
from django import forms

from . import models


class sourceAdminForm(forms.ModelForm):

    class Meta:
        model = models.source
        fields = "__all__"


class sourceAdmin(admin.ModelAdmin):
    form = sourceAdminForm
    list_display = [
        "name",
        "title_xpath",
        "last_updated",
        "source_xpath",
        "base_url",
        "created",
        "links_xpath",
        "start_url",
        "body_xpath",
        "image_xpath",
        "date_xpath",
    ]
    readonly_fields = [
        "name",
        "title_xpath",
        "last_updated",
        "source_xpath",
        "base_url",
        "created",
        "links_xpath",
        "start_url",
        "body_xpath",
        "image_xpath",
        "date_xpath",
    ]


class newsAdminForm(forms.ModelForm):

    class Meta:
        model = models.news
        fields = "__all__"


class newsAdmin(admin.ModelAdmin):
    form = newsAdminForm
    list_display = [
        "last_updated",
        "created",
        "image",
        "body",
        "link",
        "date",
        "title",
        "author",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "image",
        "body",
        "link",
        "date",
        "title",
        "author",
    ]


admin.site.register(models.source, sourceAdmin)
admin.site.register(models.news, newsAdmin)
