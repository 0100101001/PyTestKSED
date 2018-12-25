#!/usr/bin/python3

# -*- encoding=utf8 -*-


import time, datetime



from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

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


class KSEDallurDeadLine(Locator, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        wait_page_loaded(self.w)


    def LogIN(self, username, password):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        page = Locator(self.w)

        page.username_text = username
        print(Locator.username_text)
        page.password_text = password

        page.LogIn_button.click()

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

        time.sleep(0.5)
        actions = ActionChains(self.w)
        actions.move_to_element(page.section_allur).click().perform()  # Перейти в строку отчеты
        time.sleep(0.5)
        page.node_ispDisp.click()  # Перейти отчеты по исп дисциплине
        time.sleep(1)
        page.allu_NispDI.click()  # Перейти отчеты с истекшим сроком
        time.sleep(1)
        page.confirm.click()  # Перейти отчеты с истекшим сроком
        time.sleep(0.5)
        assert len(self.w.window_handles) == 2  # Проверка, что открытось 2 окно


        #assert page.zaprosToDel.is_displayed() # Проверка, что есть сохраненный элемент
