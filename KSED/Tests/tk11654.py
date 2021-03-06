#!/usr/bin/python3

# -*- encoding=utf8 -*-


import time

from selenium.webdriver import ActionChains

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators


def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False


    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)


class KSEDexpDoc(Locator, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        wait_page_loaded(self.w)


    def LogIN(self, username, password):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        page = Locator(self.w)

        page.username_text = username
        #print(Locator.username_text)
        page.password_text = password

        page.LogIn_button.click()

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

        time.sleep(0.5)

        actions = ActionChains(self.w)
        actions.move_to_element(page.myWork).click().perform()  # Переход в управление моими запросами
        time.sleep(0.5)
        page.WorkImmid.click() # выбрать в моей работе срочные
        time.sleep(0.5)
        page.checkBoxFirst.click() #Девятый документ в списке
        time.sleep(3)
        page.butAct_2.click()  # Кнопка действия с выбором
        time.sleep(1)
        page.butFavorite.click()  # Кнопка добавить в избранное
        time.sleep(1)
        page.butOK.click()  # Кнопка действия с выбором
        time.sleep(1)
        page.butOK.click()  # Кнопка действия с выбором
        time.sleep(1)
        assert page.oblProsm.is_displayed()

