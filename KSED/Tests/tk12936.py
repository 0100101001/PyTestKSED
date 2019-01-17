#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver.common.keys import Keys

from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.pages import MPages




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDDocPorSendAllure(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)

        # Авторизация

    def LogIN(self, username, password):
        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title or "Документ" in self._web_driver.title


    # Открытие документа из прошлого ТК
    def getDoc(self):
        my_file = open("Tests/linkDocPoruchenie.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self._web_driver.get(my_string)
        my_file.close()

        self.wait_page_loaded()

    # Отправка отчета
    def sendAllure(self, ):

        # Кликнем по действию "Отправить отчет" в функциональном меню "Действия"
        self.actionSendAllere.wait_to_be_clickable()
        self.actionSendAllere.click()

        # Заполним поле "Текст отчета"
        self.textAllur.wait_to_be_clickable()
        self.textAllur.click()

        # Добавим связь с документом
        self.btnAddSvyz.click()

        self.searchDoc.send_keys("У" + Keys.RETURN)

        self.oneListEl.wait_until_not_visible()
        self.oneListEl.click()

        self.btnOK.click()

        # Нажмем кнопку "Отправить"
        self.btnSend.wait_to_be_clickable()
        self.btnSend.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()

        # Проверим статус документа
        self.osnSvedeniya.wait_to_be_clickable()
        self.osnSvedeniya.click()

        self.status_Doc.wait_until_not_visible()
        assert "Исполнено" in self.status_Doc.text
