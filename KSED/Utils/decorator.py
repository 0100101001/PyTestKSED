#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import *

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from Pages.PageObject import Locator
from TestData.data import dataTest
from TestData.locators import KSEDLocators






def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)

class decorators(Locator, dataTest, KSEDLocators):

    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        #self.get(dataTest.baseURL)

        wait_page_loaded(self.w)

        # Выйдем из системы

    def USER_LOGOUTs(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.user_menu.click()

        page.USER_LOGOUT.click()

        wait_page_loaded(self.w)

        assert "Войти" in self.w.title

    def logout(self, function):

        def wrapper():

            function()
            self.USER_LOGOUTs()
            # page = Locator(self.w)
            #
            # wait = WebDriverWait(self.w, 10)
            #
            # page.user_menu.click()
            #
            # page.USER_LOGOUT.click()
            #
            # wait_page_loaded(self.w)
            #
            # assert "Войти" in self.w.title

        return wrapper


    # @logout
    # def stable():
    #     print('после')


#print(stable())