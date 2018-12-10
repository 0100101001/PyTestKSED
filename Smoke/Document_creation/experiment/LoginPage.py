#!/usr/bin/python3

# -*- encoding=utf8 -*-

# https://github.com/alexeystyagaylo/snaapy_old

import time, datetime



from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import *

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from Locators import LoginPageLocatars
from Action import Action





# def wait_page_loaded(driver):
#
#     time.sleep(2)
#
#     page_loaded = False
#
#
#
#     while not page_loaded:
#
#         page_loaded = driver.execute_script("return document.readyState == 'complete';")
#
#         time.sleep(0.1)




class KSEDLogin(PageObject):

    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        #self.get('http://213.128.208.34/share/page/arm?code=SED')


    # Форма авторизации
    # username_text = PageElement(name='username')
    #
    # password_text = PageElement(name='password')
    #
    # LogIn_button = PageElement(xpath='//span/button')


    # def __init__(self, web_driver, uri=''):
    #
    #     super().__init__(web_driver, uri)
    #
    #     self.get('http://213.128.208.34/share/page/arm?code=SED')
    #
    #     wait_page_loaded(self.w)


    def LogIN(self):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #
        #                                        ElementNotSelectableException])

        A = Action.click
        B = Action.find
        C = Action.sendkeys

        C(self, LoginPageLocatars.LOGIN, 'StroganovSN')
        C(LoginPageLocatars.PASSWORD, '12345')
        A(LoginPageLocatars.SUBMIT)

        # self.username_text = username
        # self.password_text = password


        #self.LogIn_button.click()



#        wait_page_loaded(self.w)

        #assert "АРМ" in self.w.title