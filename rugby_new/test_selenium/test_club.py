import os
import django
import time

import unittest
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from rugby_new.settings import DATA_DIR

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


def count_nb_line():
    """
    return count the number of lines in ODS object
    """
    return ODS.objects.count()


def count_number_of_lines():
    """
    return the value of count displayed
    """
    show_number_of_lines()
    text = driver.find_element(By.ID, "value_count_ODS")
    number_of_lines = text.text
    number_of_lines = int(number_of_lines)
    print(f'nb lignes : {number_of_lines}')
    time.sleep(sleepy)
    return number_of_lines


def count_nb_columns():
    """
    return the number of columns in CSV File
    """

    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')
    df = pd.read_csv(csv_file_path, sep=';')
    # 12
    nb_columns = len(df.columns)

    return nb_columns


class TestClub(unittest.TestCase):
    """
    Some tests with unittest
    """
    def setUp(self) -> None:
        """
        set up the test
        """

    def test_count_nb_lines(self):
        """
        test if the number of lines in CSV fil is equal to the number of lines in DB
        """
        count = count_nb_line()
        print(f"count = {count}")
        display_count = count_number_of_lines()
        self.assertEqual(count, display_count)

    def test_count_nb_columns(self):
        """
        test if the number of columns in CSV fil is equal to the number of columns in DB
        """
        # 13 car il y a date en plus
        nb_columns = len(ODS._meta.fields) - 1
        count = count_nb_columns()
        self.assertEqual(count, nb_columns)

    def test_is_navbar(self):
        """
        is navbar in this url 'url/'?
        """
        navbar = driver.find_element(By.CLASS_NAME, 'navba')
        if navbar:
            return True
        else:
            return False


if __name__ == '__main__':
    unittest.main()
