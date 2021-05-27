from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import json

driverPath = '/Users/study_kam/Downloads/chromedriver'
main_url = "https://youdo.com/executors-teaching-english"

opts = Options()
# opts.headless = True

driver = webdriver.Chrome(driverPath, options=opts)
driver.get(main_url)

data = []

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def scrap_list():
    executor_item_xpath = "//*[@class='b-executors-list']//li"

    executor_list_length = len(driver.find_elements_by_xpath(executor_item_xpath))

    for i in range(2, executor_list_length):
        nth_executor = executor_item_xpath + "[" + str(i) + "]"
        name_xpath = nth_executor + "//*[@class='name___e3547']"
        skills_xpath = nth_executor + "//*[@class='skills___f177c']"
        image_xpath = nth_executor + "//*[@class='image___6e813']"

        if (check_exists_by_xpath(name_xpath) == False):
            continue

        name = driver.find_element_by_xpath(name_xpath)
        skills = driver.find_element_by_xpath(skills_xpath)
        image = driver.find_element_by_xpath(image_xpath)

        data.append({
            "name_text": name.text,
            "url": name.get_attribute('href'),
            "skills": skills.text,
            "image": image.get_attribute('src'),
        })


scrap_list()

text_file = open("yodo_data.json", "w")
json_data = json.dumps(data, ensure_ascii=False)
text_file.write(json_data)
text_file.close()