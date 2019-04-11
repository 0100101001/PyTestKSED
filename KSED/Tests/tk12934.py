#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import *

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




class KSEDRD_Podpis(Locator, dataTest, KSEDLocators):


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

    #    assert "АРМ" in self.w.title


    # Открытие документа из прошлого ТК
    def getDoc(self):

        my_file = open("Tests/linkDocRD.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self.w.get(my_string)
        my_file.close()

        #self.w.get(KSEDLocators.LinkDocRD)
        wait_page_loaded(self.w)


    # Направление на подписание и проверка статуса документа
    def Podpis(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.SIGNED_button)))
        page.SIGNED_button.click()

        page.prop_bpm_comment.send_keys('я так хотю')

        page.apply_button_button.click()

        wait_page_loaded(self.w)

        # Проверим статус документа
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.osnSvedeniya)))
        page.osnSvedeniya.click()

        assert "На регистрации" in self.status_Doc.text



