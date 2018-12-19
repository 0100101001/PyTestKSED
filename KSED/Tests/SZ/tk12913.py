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





def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDPrintAttach(Locator, dataTest, KSEDLocators):


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


    # Открытие документа из прошлого ТК
    def getDoc(self):

        my_file = open("D:\PyTestKSED\KSED\Tests\SZ/tempSZ.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self.w.get(my_string)
        my_file.close()

        #self.w.get(KSEDLocators.LinkDoc)
        wait_page_loaded(self.w)

    def printAttach(self):
        wait = WebDriverWait(self.w, 2, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        page = Locator(self.w)
        #time.sleep(3)
        page.btnPrint.click()
        #time.sleep(1)
        # w = len(self.w.switch_to_alert())#window_handles)
        # print(w)
        time.sleep(2)
        # assert (w == 2)
        #assert self.w.switch_to_alert() is True
        #WebDriverWait(self.w, 3).until(EC.alert_is_present())
        #time.sleep(10)
        #assert wait.until(EC.invisibility_of_element_located((By.XPATH, KSEDLocators.btnPrint)))
        # alert = self.w.switch_to_alert()
        # alert.accept()
        # print(alert.text)
