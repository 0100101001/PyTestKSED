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
from KSED.pages import MPages

def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False


    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)


class KSEDallurResolution(Locator, dataTest, KSEDLocators):


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
        page2 = MPages(self.w, self.w.current_url)

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

        time.sleep(0.5)
        actions = ActionChains(self.w)
        actions.move_to_element(page.section_allur).click().perform()  # Перейти в строку отчеты
#        time.sleep(0.5) # без этого ожидания не работает
#        WebDriverWait(self.w, 5).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.node_ispDisp)))
#        page.node_ispDisp.click()  # Перейти отчеты по исп дисциплине

        page2.melements.click()

        #        time.sleep(1)
        page2.wait_page_loaded()
        page2.m2elements.click()
#        page.allu_SostIspR.click()  # Перейти в раздел состояние исполнеия резолюций
#        time.sleep(2)
        page.confirm_3.click()  # Кнопка ОК
        time.sleep(0.5)
        assert len(self.w.window_handles) == 2  # Проверка, что открытось 2 окно



