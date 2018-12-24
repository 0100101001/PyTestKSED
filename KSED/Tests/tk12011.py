#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select, WebDriverWait

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




class KSEDStatAllureVidDic(Locator, dataTest,KSEDLocators):


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
        #page.wait(2)


        # Ожидание
        # select = Select(Locator.username_text)
        # select.select_by_visible_text("текст")

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

        time.sleep(0.5)
        actions = ActionChains(self.w)
        actions.move_to_element(page.section_allur).click().perform()  # Перейти в строку отчеты
        time.sleep(0.5)
        page.node_Statis.click()  # Перейти статистические отчеты
        time.sleep(1)
        page.stat_tipDoc.click()  # Переход в сводку по типам документов
        time.sleep(1)
        page.confirm2.click()  # Перейти отчеты с истекшим сроком
        time.sleep(5)
        w = len(self.driver.window_handles)
        self.assertTrue(w == 2) # Проверка, что открытось 2 окно
