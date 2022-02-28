from django.db import models
from django.urls import reverse


class source(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    title_xpath = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    source_xpath = models.CharField(max_length=200)
    base_url = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    links_xpath = models.CharField(max_length=200)
    start_url = models.CharField(max_length=100)
    body_xpath = models.CharField(max_length=200)
    image_xpath = models.CharField(max_length=200)
    date_xpath = models.CharField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("checker_source_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("checker_source_update", args=(self.pk,))


class news(models.Model):

    # Relationships
    source = models.ForeignKey("checker.source", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.CharField(max_length=500)
    body = models.TextField()
    link = models.CharField(max_length=500)
    date = models.CharField(max_length=30)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=300)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("checker_news_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("checker_news_update", args=(self.pk,))
