from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains

driverPath = '/Users/study_kam/Downloads/chromedriver'
main_url = "https://youdo.com/tasks-all-opened-all"

def open_main_page():
  opts = Options()
  # opts.headless = True

  driver = webdriver.Chrome(driverPath, options=opts)
  driver.get(main_url)

  return driver

def close_popups(driver):
  time.sleep(5)

  # Popup with useless information, we should close them
  close_popup_button = driver.find_element_by_xpath("//a[@class='close___f8820']")
  close_little_popup_button = driver.find_element_by_xpath("//a[@class='subscribePopupLink']")

  if close_little_popup_button != None:
    try:
      close_little_popup_button.click()
    except Exception:
      time.sleep(5)
      close_little_popup_button.click()

  if close_popup_button != None:
    close_popup_button.click()

def selectFilter(driver, index):
  all_filter = driver.find_element_by_css_selector('.all___286de .checkbox-icon___d1119')
  all_filter.click()

  filter_checkboxes = driver.find_elements_by_css_selector('.item___f31a3 .container___86ec5 .checkbox-icon___d1119')
  filter_checkbox = filter_checkboxes[index + 1]

  # поставим галочку для определенной колонки
  filter_checkbox.click()

def scrapServices(driver):
  services_list = driver.find_elements_by_xpath("//*[@class='listItem___71243']")

  for i in range(1, len(services_list)):
    service_xpath = "//*[@class='listItem___71243']" + "[" + str(i) + "]"

    title = driver.find_element_by_xpath(service_xpath + "//*[@class='title___3ac0d']")
    price = driver.find_element_by_xpath(service_xpath + "//*[@class='price___b4f64']")


    print(title.text)
    print(price.text)

driver = open_main_page()
close_popups(driver)

selectFilter(driver, 0)
time.sleep(5)
scrapServices(driver)