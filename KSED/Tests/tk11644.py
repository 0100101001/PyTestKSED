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
from KSED.pages import MPages




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocVH(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)

        # self.get(dataTest.baseURL)
        #
        # wait_page_loaded(self.w)

    # Авторизация
    def LogIN(self, username, password):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        # page = Locator(self.w)

        self.username_text = username

        self.password_text = password

        self.LogIn_button.click()

        # wait_page_loaded(self._web_driver)
        self.user_menu.wait_to_be_clickable()

        assert "АРМ" in self._web_driver.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])

        # page = Locator(self.w)

        # wait = WebDriverWait(self.w, 10)

        self.newDoc_button.click()

        self.vhDoc.click()

        assert "Страница создания документа" in self._web_driver.title

 #       time.sleep(1)
        # Атрибуты документа

        # Адресат
        self.adresat.scroll_to_element()
        self.adresat.wait_to_be_clickable()
        self.adresat.send_keys(u'Строганов' + Keys.RETURN)


        # Корреспондент
        self.korrespondent.wait_to_be_clickable()
        self.korrespondent.send_keys(u'Логика' + Keys.RETURN)

        # Категория документа
        self.category_doc.wait_to_be_clickable()
        self.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Исходящий номер
        self.ishNumber.send_keys(u'123456')

        # Дата исходящего
        dd = datetime.date.today().strftime('%d%m%Y')
        self.dateIS.send_keys(dd)

        # Кнопка "Создать"
        self.btnCreateDoc.scroll_to_element()
        self.btnCreateDoc.wait_to_be_clickable()
        self.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self._web_driver)
#        self.w.set_page_load_timeout(30)
#         time.sleep(20)

#
#        wait.until(EC.title_is(self.w.title))
        self.mode.wait_to_be_clickable()

        assert "Документ" in self._web_driver.title

