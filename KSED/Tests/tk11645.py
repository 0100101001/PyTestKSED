#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators

import allure
def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocISH(Locator, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        wait_page_loaded(self.w)

    @allure.step("Авторизация")
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

        page.ishDoc.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Заголовок
        self.w.execute_script("arguments[0].scrollIntoView();", page.title)
        page.title.send_keys(u'Документ')

        # Категория документа
        page.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Корреспондент
        time.sleep(0.5)
        page.korrespondentISH.send_keys(u'Логика' + Keys.RETURN)

        # Основание подписания
        self.w.execute_script("arguments[0].scrollIntoView();", page.osnovPodpis)
        page.osnovPodpis.send_keys(u'Договор')

        # Вид документа
        page.doc_typeInp.send_keys(u'Уведомление' + Keys.RETURN)

        # Подписанты
        self.w.execute_script("arguments[0].scrollIntoView();", page.podpisant)
        time.sleep(0.5)
        page.podpisant.send_keys(u'Строганов' + Keys.RETURN)

        time.sleep(0.5)
        # Кнопка "Создать"
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnCreateDoc)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnCreateDoc)))
        page.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self.w)
#        self.w.set_page_load_timeout(30)
#        time.sleep(2)

#
#        wait.until(EC.title_is(self.w.title))

        assert "Документ" in self.w.title

