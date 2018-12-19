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

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators



def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class Edit_Profile(Locator, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        wait_page_loaded(self.w)

    # Авторизация
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

    # Изменим пароль
    def edit_profile(self):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.user_menu.click()

        page.my_profile.click()

        wait_page_loaded(self.w)

        assert "Профиль пользователя" in self.w.title
        # Нажмем кнопку "Изменить профиль"
        page.btnEdit_profile.click()
        # Заполним поле "Должность"
        page.inputPosition.clear()
        page.inputPosition.send_keys('Тестер')

        # Нажмем кнопку "ОК"
        page.btnOKchange.click()

        wait_page_loaded(self.w)

        assert "Тестер" in page.fieldlabel.text

    # Выйдем из системы
    def USER_LOGOUTs(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.user_menu.click()

        page.USER_LOGOUT.click()

        wait_page_loaded(self.w)

        assert "Войти" in self.w.title




        # page.USER_LOGOUT.click()
        #
        # wait_page_loaded(self.w)
        #
        # assert "Войти" in self.w.title