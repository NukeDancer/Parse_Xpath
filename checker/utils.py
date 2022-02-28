import requests
from lxml import html
import validators
from news_checker.settings import HEADERS, NO_IMAGE
from checker.models import news as news_instance
from checker.models import source as source_class


def get_news_by_source(pk):
    source = source_class.objects.get(id=pk)
    response = requests.get(source.start_url, headers=HEADERS)
    dom = html.fromstring(response.text)
    news_links = dom.xpath(source.links_xpath)

    for item in news_links:
        if not validators.url(item):
            item = source.base_url + item
        news_item = news_instance()
        response = requests.get(item, headers=HEADERS)
        news_page = html.fromstring(response.text)

        if news_page.xpath(source.title_xpath):
            news_title = news_page.xpath(source.title_xpath)[0]
            news_link = item

            if news_page.xpath(source.source_xpath):
                news_source = news_page.xpath(source.source_xpath)[0]
            else:
                news_source = "None"

            if news_page.xpath(source.date_xpath):
                news_date = news_page.xpath(source.date_xpath)[0]
            else:
                news_date = "None"

            if news_page.xpath(source.image_xpath) and validators.url(news_page.xpath(source.image_xpath)[0]):
                news_image = news_page.xpath(source.image_xpath)[0]
            else:
                news_image = NO_IMAGE

            if news_page.xpath(source.body_xpath):
                news_body = " ".join(news_page.xpath(source.body_xpath))
            else:
                news_body = 'Cannot extract'

            news_item.title = news_title
            news_item.link = news_link
            news_item.author = news_source
            news_item.source = source
            news_item.date = news_date
            news_item.image = news_image
            news_item.body = news_body

            if news_instance.objects.filter(link=news_link):
                print('Skipping. Duplicate found.')
            else:
                news_item.save()
                print('News added to DataBase.')
    print('All news checked for Source')
