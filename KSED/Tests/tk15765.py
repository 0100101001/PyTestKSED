#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.pages import MPages, WebPage




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)

class KSEDreject_RD(MPages, dataTest, KSEDLocators):

    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)


    # Авторизация
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password
        self.LogIn_button.click()
        self.wait_page_loaded()

        assert "АРМ" in self._web_driver.title

    #открытие документа
    def getDoc(self):

        my_file = open("Tests/linkDocCS.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self._web_driver.get(my_string)
        my_file.close()

    def rejectDoc(self):
        self.REJECTED_button.wait_to_be_clickable()
        self.REJECTED_button.click()

        self.prop_bpm_comment.wait_until_not_visible()
        self.prop_bpm_comment.send_keys('Доработать')

        self.apply_button_button.wait_to_be_clickable()
        self.apply_button_button.click()

        time.sleep(5)
        assert "Отклонено" in self.statusSogl.get_text()

    # Сохраним ссылку на документ в файл
    def LinkDocWFile(self):

        url = self._web_driver.current_url
        my_file = open("Tests/linkDocCS.txt", "w")
        my_file.write(str(url))
        my_file.close()

