from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# lancer le navigateur
driver = webdriver.Chrome()
driver.get("http://www.youtube.com")

xpath = "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"

accepted_all_element = driver.find_element(By.XPATH, xpath)
accepted_all_element.click()

time.sleep(1)
xpath = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"

search_box = driver.find_element(By.XPATH, xpath)
search_box.send_keys("byob")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(3)
xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a"
time.sleep(3)
press_title = driver.find_element(By.XPATH, xpath)
press_title.click()


time.sleep(100)

driver.close()

