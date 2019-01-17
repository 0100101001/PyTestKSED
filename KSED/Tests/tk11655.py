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
from KSED.pages import MPages




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocPor(Locator, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        wait_page_loaded(self.w)

    # Авторизация
    def LogIN(self, username, password):

        #**page = Locator(self.w)
        page = MPages(self.w, self.w.current_url)

        page.username_text = username
        print(Locator.username_text)
        page.password_text = password

        page.LogIn_button.click()

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):

        #**page = Locator(self.w)
        page = MPages(self.w, self.w.current_url)

        wait = WebDriverWait(self.w, 10)

        page.newDoc_button.click()

        page.poruchenie.click()

        page.wait_page_loaded()
        #**wait_page_loaded(self.w)

        assert "Страница создания документа" in self.w.title

        # Атрибуты документа
        page.wait_page_loaded()
        #**wait_page_loaded(self.w)

        # Тип поручения
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.tipPoruch)))

        page.tipPoruch.wait_until_not_visible()
        page.tipPoruch.scroll_to_element()
        page.tipPoruch.send_keys(u'Для информации' + Keys.ENTER)

        # Категория документа
        page.category_doc.wait_until_not_visible()
        page.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Ответственный исполнитель
        page.otvetstv_ispoln.scroll_to_element()
        page.otvetstv_ispoln.send_keys(u'Строганов' + Keys.RETURN)

        # Кнопка "Создать"
        page.btnCreateDoc.scroll_to_element()
        page.btnCreateDoc.wait_to_be_clickable()
        page.btnCreateDoc.click()

        page.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        #**wait_page_loaded(self.w)
        page.wait_page_loaded()


        assert "Документ" in self.w.title


    # Сохраним ссылку на документ в файл
    def LinkDocWFile(self):

        url = self.w.current_url
        my_file = open("Tests/linkDocPoruchenie.txt", "w")
        my_file.write(str(url))
        my_file.close()

