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

    "Изменения мои"

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocVH(Locator, dataTest, KSEDLocators, MPages):


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

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])

        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.newDoc_button.click()

        page.vhDoc.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Адресат
        self.w.execute_script("arguments[0].scrollIntoView();", page.adresat)
        self.adresat.wait_to_be_clickable()
        self.adresat.send_keys(u'Строганов' + Keys.RETURN)
        page.adresat.send_keys(Keys.RETURN)

        # Корреспондент
        page.korrespondent.send_keys(u'Сибинтек' + Keys.RETURN)

        # Категория документа
        page.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Исходящий номер
        page.ishNumber.send_keys(u'123456')

        # Дата исходящего
        dd = datetime.date.today().strftime('%d%m%Y')
        page.dateIS.send_keys(dd)

        # Кнопка "Создать"
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnCreateDoc)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnCreateDoc)))
        page.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self.w)
#        self.w.set_page_load_timeout(30)
        time.sleep(20)

#
#        wait.until(EC.title_is(self.w.title))

        assert "Документ" in self.w.title

