#!/usr/bin/python3

# -*- encoding=utf8 -*-


import time

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators

from KSED.TestData.pages import MPages


import allure
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

    @allure.step("Авторизация")
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title

        self.wait_page_loaded()
        self.mySearch.move_to_element() # Перейти в строку отчеты
        self.mySearch.wait_to_be_clickable()
        self.mySearch.click()
        self.btnPlus.wait_to_be_clickable() # развернуть на "+"
        self.btnPlus.click()
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


