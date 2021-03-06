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






import allure
def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDStatAllureTemDoc(Locator, dataTest,KSEDLocators):


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
        #page.wait(2)


        # Ожидание
        # select = Select(Locator.username_text)
        # select.select_by_visible_text("текст")

        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

       # r = page.username_text.locator
        #r = "123456"
        # my_file = open("temp.txt", "w")
        # my_file.write(str(r))
        # my_file.close()
        #t = page.username_text.locator

    def StatAllureTemDoc(self):
        wait = WebDriverWait(self.w, 1, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        actions = ActionChains(self.w)
        page = Locator(self.w)

        #self.w.execute_script("arguments[0].scrollIntoView();", page.navigation)
        # Раскрываем раздел "Отчеты"
        page.section_allur.click()

        time.sleep(0.5)
        #actions.move_to_element(page.navigation).move_by_offset(0, 10).click().perform()
        # Кликаем по "Статические отчеты"
        page.node_Statis.click()
        time.sleep(0.5)
        # Открываем отчет
        page.edsBySubjectStat.click()
        time.sleep(2)

        page.btnOKform.click()

        time.sleep(1)
        assert (len(self.w.window_handles) == 2)
#        d = len(page.subordinate)
#        print(str(d))
