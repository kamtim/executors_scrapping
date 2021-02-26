from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import json
import time

driverPath = '/Users/study_kam/Downloads/chromedriver2'
main_url = "https://kzn.profi.ru/repetitor/english/?seamless=1&tabName=PROFILES"

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
    executor_item_xpath = "//*[contains(@class, 'seamless-profile')]"

    for i in range(2, len(driver.find_elements_by_xpath(executor_item_xpath))):
        print(i)

        nth_executor = executor_item_xpath + "[" + str(i) + "]"
        name_xpath = nth_executor + "//*[contains(@class, 'listing-profile__name')]"

        if (check_exists_by_xpath(name_xpath) == False):
            continue

        skills_xpath = nth_executor + "//*[contains(@class, 'desktop-profile__block')]//p"
        image_xpath = nth_executor + "//*[contains(@class, 'desktop-profile__avatar-img')]/img"

        try:
            name = driver.find_element_by_xpath(name_xpath)
            skills = driver.find_element_by_xpath(skills_xpath)

            data.append({
                "name_text": name.text,
                "url": name.get_attribute('href'),
                "skills": skills.text,
                "image": driver.find_element_by_xpath(image_xpath).get_attribute('src'),
            })
        except NoSuchElementException:
            continue


scrap_list()

text_file = open("profi_data.json", "w")
json_data = json.dumps(data, ensure_ascii=False)
text_file.write(json_data)
text_file.close()

driver.close()