#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import *

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.TestData.pages import MPages




import allure
def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocReestr(Locator, dataTest, KSEDLocators, MPages):


    def __init__(self, web_driver, uri = dataTest.baseURL):

        super().__init__(web_driver, uri)

        # self.get(dataTest.baseURL)
        #
        # wait_page_loaded(self._web_driver)

    @allure.step("Авторизация")
    def LogIN(self, username, password):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        # page = Locator(self.w)

        self.username_text = username
        print(Locator.username_text)
        self.password_text = password

        self.LogIn_button.click()

        wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):
        wait = WebDriverWait(self._web_driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        actions = ActionChains(self._web_driver)

        # self = Locator(self._web_driver)

        wait = WebDriverWait(self._web_driver, 10)

        self.newDoc_button.click()

        self.reestr.click()

        assert "Страница создания документа" in self._web_driver.title


 #       time.sleep(1)
        # Атрибуты документа

        # Вид реестра
        self.vid_reestra.click()
        self.vid_reestraPP.click()
        time.sleep(0.5)
        # Получатель
        self.poluchatel.send_keys("Сибинтек"+Keys.RETURN)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.poluchatel)))

        # Документы
        self.inpDoc.wait_to_be_clicable()
        self.inpDoc.send_keys(dataTest.BARCODE+Keys.RETURN)

        time.sleep(0.5)
        # Кнопка "Создать и отправить"
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnCreateSend)))
        actions.move_to_element(self.btnCreateSend).click().perform()
        #self.btnCreateSend.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self._web_driver)
#        self._web_driver.set_page_load_timeout(30)
        time.sleep(2)

#
#        wait.until(EC.title_is(self._web_driver.title))

        assert "Документ" in self._web_driver.title

