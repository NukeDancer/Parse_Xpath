from django import forms
from . import models


class sourceForm(forms.ModelForm):
    class Meta:
        model = models.source
        fields = [
            "name",
            "title_xpath",
            "source_xpath",
            "base_url",
            "links_xpath",
            "start_url",
            "body_xpath",
            "image_xpath",
            "date_xpath",
        ]


class newsForm(forms.ModelForm):
    class Meta:
        model = models.news
        fields = [
            "image",
            "body",
            "link",
            "date",
            "title",
            "author",
            "source",
        ]
