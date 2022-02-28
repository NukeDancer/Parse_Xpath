import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_source_list_view():
    instance1 = test_helpers.create_checker_source()
    instance2 = test_helpers.create_checker_source()
    client = Client()
    url = reverse("checker_source_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_source_create_view():
    client = Client()
    url = reverse("checker_source_create")
    data = {
        "name": "text",
        "title_xpath": "text",
        "source_xpath": "text",
        "base_url": "text",
        "links_xpath": "text",
        "start_url": "text",
        "body_xpath": "text",
        "image_xpath": "text",
        "date_xpath": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_source_detail_view():
    client = Client()
    instance = test_helpers.create_checker_source()
    url = reverse("checker_source_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_source_update_view():
    client = Client()
    instance = test_helpers.create_checker_source()
    url = reverse("checker_source_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "title_xpath": "text",
        "source_xpath": "text",
        "base_url": "text",
        "links_xpath": "text",
        "start_url": "text",
        "body_xpath": "text",
        "image_xpath": "text",
        "date_xpath": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_news_list_view():
    instance1 = test_helpers.create_checker_news()
    instance2 = test_helpers.create_checker_news()
    client = Client()
    url = reverse("checker_news_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_news_create_view():
    source = test_helpers.create_checker_source()
    client = Client()
    url = reverse("checker_news_create")
    data = {
        "image": "text",
        "body": "text",
        "link": "text",
        "date": "text",
        "title": "text",
        "author": "text",
        "source": source.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_news_detail_view():
    client = Client()
    instance = test_helpers.create_checker_news()
    url = reverse("checker_news_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_news_update_view():
    source = test_helpers.create_checker_source()
    client = Client()
    instance = test_helpers.create_checker_news()
    url = reverse("checker_news_update", args=[instance.pk, ])
    data = {
        "image": "text",
        "body": "text",
        "link": "text",
        "date": "text",
        "title": "text",
        "author": "text",
        "source": source.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
