#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest

import allure
def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDLogin(Locator, dataTest):


    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get(dataTest.baseURL)

        # wait_page_loaded(self.w)

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
