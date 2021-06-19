from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import json

from database.database_setup import Freelancer
from database.populate import session, write_to_database

print(session.query(Freelancer).all())

driverPath = '/Users/study_kam/Downloads/chromedriver91'
main_url = "https://youdo.com/executors-courier"

opts = Options()
# opts.headless = True

driver = webdriver.Chrome(driverPath, options=opts)
driver.get(main_url)

executors_data = {}


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def get_type_links_list():
    def get_href(a):
        return a.get_attribute('href')

    types_list_xpath = "//*[@class='executors_categories__parent']//*[contains(@class, " \
                       "'executors_categories__parent_link')] "

    return list(map(get_href, driver.find_elements_by_xpath(types_list_xpath)))


def scrap_executors_list():
    type_xpath = "//*[@class='executors_categories__parent active']//*[contains(@class, " \
                 "'executors_categories__parent_link')] "
    type_title = driver.find_elements_by_xpath(type_xpath)[0].text

    executor_item_xpath = "//*[@class='b-executors-list']//li"
    executor_list_length = len(driver.find_elements_by_xpath(executor_item_xpath))

    executors_list = []

    for i in range(2, executor_list_length):
        nth_executor = executor_item_xpath + "[" + str(i) + "]"
        name_xpath = nth_executor + "//*[@class='name__e3547']"
        skills_xpath = nth_executor + "//*[@class='skills__f177c']"
        image_xpath = nth_executor + "//*[@class='image__6e813']"

        if (check_exists_by_xpath(name_xpath) == False):
            continue

        name = driver.find_element_by_xpath(name_xpath)
        skills = driver.find_element_by_xpath(skills_xpath)
        image = driver.find_element_by_xpath(image_xpath)

        executors_list.append({
            "name_text": name.text,
            "url": name.get_attribute('href'),
            "skills": skills.text,
            "image": image.get_attribute('src'),
        })

        executors_data[type_title] = executors_list


def write_to_file(data):
    text_file = open("yodo_data.json", "w")
    json_data = json.dumps(data["Ремонт и строительство"], ensure_ascii=False)
    text_file.write(json_data)
    text_file.close()


def scrap_youdo_data():
    type_links_list = get_type_links_list()

    for type_link in type_links_list[0:1]:
        driver.get(type_link)

        # some kind of advertisement appears, so we should return to original site
        if "https://youdo.com" not in driver.current_url:
            driver.back()

        scrap_executors_list()

    write_to_file(executors_data)
    write_to_database(executors_data["Ремонт и строительство"])
