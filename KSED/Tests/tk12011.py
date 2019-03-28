#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select, WebDriverWait

from selenium.common.exceptions import *

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.pages import MPages


def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDStatAllureVidDic(MPages, Locator, dataTest,KSEDLocators):


    def __init__(self, web_driver, uri = dataTest.baseURL):

        super().__init__(web_driver, uri)

        # self.get(dataTest.baseURL)

        # wait_page_loaded(self.w)

    # Авторизация
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title

        # Ожидание
        # select = Select(Locator.username_text)
        # select.select_by_visible_text("текст")

        # self.wait_page_loaded()
        #
        # assert "АРМ" in self._web_driver.title


        # actions = ActionChains(self.w)

        self.section_allur.move_to_element()  # Перейти в строку отчеты
        self.section_allur.click()
        self.stat_tipDoc.wait_until_not_visible()
        self.node_Statis.click()  # Перейти статистические отчеты
        self.stat_tipDoc.wait_until_not_visible()
        self.stat_tipDoc.click()  # Переход в сводку по типам документов
        self.confirm_4.wait_to_be_clickable()
        self.confirm_4.click()  # Перейти отчеты с истекшим сроком

        assert len(self._web_driver.window_handles) == 2 # Проверка, что открытось 2 окно
