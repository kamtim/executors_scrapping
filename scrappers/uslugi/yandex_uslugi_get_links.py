from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}

print(PROXY)

driverPath = '/Users/study_kam/Downloads/chromedriver91'
main_url = "https://uslugi.yandex.ru/43-kazan/catalog"

opts = Options()
# opts.headless = True

driver = webdriver.Chrome(driverPath, options=opts)

driver.get(main_url)

# first_subtype_link_xpath = "//*[contains(@class, 'HomeRubricMenu-Content')]//a"
# first_subtype_link = driver.find_element_by_xpath(first_subtype_link_xpath)
# driver.get(first_subtype_link.get_attribute('href'))
#
# type_link_xpath = "//*[contains(@class, 'Content-Header')]//a"
# type_link = driver.find_element_by_xpath(type_link_xpath)
# driver.get(type_link.get_attribute('href'))

# driver.close()