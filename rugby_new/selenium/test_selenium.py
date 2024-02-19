import os
import django
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')
django.setup()
from app.models import ODS

# change all values of time.sleep(sleepy)
sleepy = 5


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
time.sleep(sleepy)


def show_number_of_lines():
    """
    show the number of lines in DB
    """
    btn_showNumber = driver.find_element(By.ID, "btn_showNumberOfLines")
    btn_showNumber.click()
    time.sleep(sleepy)


def bulk_bdd():
    """
    delete and insert values in DB
    """
    btn_bulk = driver.find_element(By.ID, "btn_bulkDB")
    btn_bulk.click()
    time.sleep(sleepy)


def click_element_link_text(value):
    """
    find and click on link
    """
    element = driver.find_element(By.LINK_TEXT, value)
    element.click()
    time.sleep(sleepy)


def click_element_class_name(value):
    """
    find and click on class
    """
    element = driver.find_element(By.CLASS_NAME, value)
    element.click()
    time.sleep(sleepy)


def click_element_id(value):
    """
    find and click on id
    """
    element = driver.find_element(By.ID, value)
    element.click()
    time.sleep(sleepy)


def is_navbar(value):
    """
    is navbar in this url
    """
    navbar = driver.find_element(By.CLASS_NAME, value)
    if navbar:
        print('Navbar: OK')
    else:
        print('navbar: /!\\ ko /!\\ ')


def is_logo(value):
    """
    is logo in this url
    """
    logo = driver.find_element(By.CSS_SELECTOR, value)
    if logo.is_displayed():
        print('logo: OK')
    else:
        print('logo: /!\\ ko /!\\ ')


def count_number_of_lines():
    """
    compare the value of count displayed with the value of rows in DB
    """
    text = driver.find_element(By.ID, "value_count_ODS")
    number_of_lines = text.text
    number_of_lines = int(number_of_lines)
    if number_of_lines == ODS.objects.count():
        print(f"Nombre de lignes ({number_of_lines}): OK")
    else:
        print(f"Nombre de lignes: /!\\ ko /!\\")


def is_first_row():
    """
    Verify Abergement-Clémenciat is in first_row_ODS.commune
    """
    first_row_ODS = ODS.objects.first()
    if 'Abbaretz' in first_row_ODS.commune:
        print("Abbaretz est dans l'objet")
    else:
        print('non abbaretz')
    if 'L\'Abergement-Clémenciat' in first_row_ODS.commune:
        print("L\'Abergement-Clémenciat est dans l'objet")
    else:
        print('non L\'Abergement-Clémenciat')


show_number_of_lines()
count_number_of_lines()
is_navbar('navbar')
is_logo('img[alt="logo_navbar"]')
click_element_link_text('Liste ODS')
is_first_row()
click_element_class_name('next_page')
click_element_id('navbar_home')
bulk_bdd()

time.sleep(100)

driver.close()
