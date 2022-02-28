from rest_framework import serializers

from . import models


class sourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.source
        fields = [
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

class newsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.news
        fields = [
            "last_updated",
            "created",
            "image",
            "body",
            "link",
            "date",
            "title",
            "author",
        ]
