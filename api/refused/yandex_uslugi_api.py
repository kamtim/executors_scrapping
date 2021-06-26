import requests

# return captcha because api is not public

for i in range(1, 10):
    r = requests.get('https://uslugi.yandex.ru/api/search_rubrics?rubricId=%2Fremont-i-stroitel_stvo%2Fremont-kvartir-i-domov&text=%D0%A0%D0%B5%D0%BC%D0%BE%D0%BD%D1%82%20%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%20%D0%B8%20%D0%B4%D0%BE%D0%BC%D0%BE%D0%B2')
    print(r.text)