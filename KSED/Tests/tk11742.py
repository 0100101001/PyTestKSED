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


class KSEDexpZap(MPages, Locator, dataTest, KSEDLocators):


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

        time.sleep(0.5)

        self.section_allur.move_to_element()  # Перейти в строку отчеты
        self.section_allur.click()
        self.poiskzapr.move_to_element().move_by_offset(-70, 0).click().perform() # развернуть на "+"
        self.zaprosToDel.wait_to_be_clickable()  # выбрать созданный по предусловию запрос
        self.zaprosToDel.click() # выбрать созданный по предусловию запрос
        self.checkBoxFirst.wait_to_be_clickable()  # выбрать созданный по предусловию запрос
        self.checkBoxFirst.click() #Первый чекбокс в списке
        self.butAct.wait_to_be_clickable()   #Кнопка действия с выбором
        self.butAct.click() # Первый чекбокс в списке
        self.butFavorite.wait_to_be_clickable()
        self.butFavorite.click()  #Кнопка добавить в избранное
        self.butOK.wait_to_be_clickable()
        self.butOK.click()  # Кнопка действия с выбором

        assert self.oblProsm.is_displayed()  # Проверка, что отображается рабочая область


