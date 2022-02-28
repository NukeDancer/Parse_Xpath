import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from checker import models as checker_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_checker_source(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["title_xpath"] = ""
    defaults["source_xpath"] = ""
    defaults["base_url"] = ""
    defaults["links_xpath"] = ""
    defaults["start_url"] = ""
    defaults["body_xpath"] = ""
    defaults["image_xpath"] = ""
    defaults["date_xpath"] = ""
    defaults.update(**kwargs)
    return checker_models.source.objects.create(**defaults)
def create_checker_news(**kwargs):
    defaults = {}
    defaults["image"] = ""
    defaults["body"] = ""
    defaults["link"] = ""
    defaults["date"] = ""
    defaults["title"] = ""
    defaults["author"] = ""
    if "source" not in kwargs:
        defaults["source"] = create_checker_source()
    defaults.update(**kwargs)
    return checker_models.news.objects.create(**defaults)
