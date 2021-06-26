from bs4 import BeautifulSoup
import requests

from scrappers.get_sections.config import config_headers

url = "https://kzn.profi.ru/"

with requests.Session() as se:
    se.headers = config_headers


response = se.get(url)
soup = BeautifulSoup(response.text, 'lxml')

executors_categories = soup.select("._3gNSGvU")
executors_categories_text = list(map(lambda category: category.text, executors_categories))

print(executors_categories_text)