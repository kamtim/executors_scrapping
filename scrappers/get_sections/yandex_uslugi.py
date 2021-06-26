from bs4 import BeautifulSoup
import requests

from scrappers.get_sections.config import config_headers

url = "https://uslugi.yandex.ru/43-kazan/catalog"

with requests.Session() as se:
    se.headers = config_headers


response = se.get(url)
soup = BeautifulSoup(response.text, 'lxml')

executors_categories = soup.select(".HomeRubricMenu-MenuItem")
executors_categories_text = list(map(lambda category: category.text, executors_categories))

print(executors_categories_text)