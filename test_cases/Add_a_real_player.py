import os
import unittest
import time
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class testAddARealPlayer(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_real_player(self,):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login.click_on_the_add_a_player_button()
        user_login.type_in_name('alejajca')
        time.sleep(2)
        user_login.type_in_surname('jakberety')
        time.sleep(2)
        user_login.type_in_position('Missionary')
        time.sleep(2)
        user_login.type_in_age('12122012')
        user_login.click_on_the_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()