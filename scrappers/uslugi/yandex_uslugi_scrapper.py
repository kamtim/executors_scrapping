from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import json
import time

driverPath = '/Users/study_kam/Downloads/chromedriver91'
main_url = "https://yandex.ru/uslugi/43-kazan/category/repetitoryi-i-obuchenie/anglijskij-yazyik--2276"

opts = Options()
# opts.headless = True

driver = webdriver.Chrome(driverPath, options=opts)
driver.get(main_url)

time.sleep(2)

data = []


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def scrap_list():
    executor_item_xpath = "//*[contains(@class, 'WorkersListBlendered-WorkerCard')]"

    # images loades lazy, we should scroll down for for its loading
    driver.execute_script("window.scrollBy(0,500);")

    for i in range(2, len(driver.find_elements_by_xpath(executor_item_xpath))):
        print(i)

        # images loades lazy, we should scroll down for for its loading
        driver.execute_script( "window.scrollBy(0,500);" )

        nth_executor = executor_item_xpath + "[" + str(i) + "]"
        name_xpath = nth_executor + "//*[contains(@class, 'WorkerCardMini-Title')]//a"

        if (check_exists_by_xpath(name_xpath) == False):
            continue

        button_xpath = nth_executor + "//*[contains(@class, 'WorkerCardDescription-TextLink')]"
        skills_xpath = nth_executor + "//*[contains(@class, 'WorkerCardDescription-Text')]"
        image_xpath = nth_executor + "//*[contains(@class, 'WorkerCardMini-Avatar')]/*"

        try:
            try:
                button = driver.find_element_by_xpath(button_xpath)
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                print(button_xpath)
                pass


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

text_file = open("yandex_uslugi_data.json", "w")
json_data = json.dumps(data, ensure_ascii=False)
text_file.write(json_data)
text_file.close()

driver.close()
