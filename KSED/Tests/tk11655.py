#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

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

class KSEDCreatDocPor(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)

       # self.get(dataTest.baseURL)

       # wait_page_loaded(self.w)

    @allure.step("Авторизация")
    def LogIN(self, username, password):

        #**page = Locator(self.w)
        #page = MPages(self.w, self.w.current_url)

        self.username_text = username
 #       print(Locator.username_text)
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()

        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):

        #**page = Locator(self.w)
        #page = MPages(self.w, self.w.current_url)

        wait = WebDriverWait(self._web_driver, 10)

        self.newDoc_button.click()

        self.poruchenie.click()

        self.wait_page_loaded()
        #**wait_page_loaded(self.w)

        assert "Страница создания документа" in self._web_driver.title

        # Атрибуты документа
        self.wait_page_loaded()
        #**wait_page_loaded(self.w)

        # Тип поручения
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.tipPoruch)))

        self.tipPoruch.wait_until_not_visible()
        self.tipPoruch.scroll_to_element()
        self.tipPoruch.send_keys(u'Для информации' + Keys.ENTER)

        # Категория документа
        self.category_doc.wait_until_not_visible()
        self.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Ответственный исполнитель
        self.otvetstv_ispoln.scroll_to_element()
        self.otvetstv_ispoln.send_keys(u'Строганов' + Keys.RETURN)

        # Кнопка "Создать"
        self.btnCreateDoc.scroll_to_element()
        self.btnCreateDoc.wait_to_be_clickable()
        self.btnCreateDoc.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        #**wait_page_loaded(self.w)
        self.wait_page_loaded()


        assert "Документ" in self._web_driver.title


    # Сохраним ссылку на документ в файл
    def LinkDocWFile(self):

        url = self._web_driver.current_url
        my_file = open("Tests/linkDocPoruchenie.txt", "w")
        my_file.write(str(url))
        my_file.close()

