#!/usr/bin/python3

# -*- encoding=utf8 -*-



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




class KSEDCreatDocPD(Locator, dataTest, KSEDLocators):


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

        assert "АРМ" in self.w.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])

        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.newDoc_button.click()

        page.proizvDoc.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Заголовок
        page.title.send_keys(u'Документ')

        # Вид документа
        page.doc_typeInp.send_keys(u'Договор'+Keys.RETURN)

        time.sleep(1)
        # Проработка
        self.w.execute_script("arguments[0].scrollIntoView();", page.prorabotka)
        #page.prorabotka.send_keys(u'Строганов'+Keys.RETURN)
        page.chBprorab.click()
        time.sleep(0.5)
        # Нормоконтроль
        self.w.execute_script("arguments[0].scrollIntoView();", page.normokontrol)
        #page.normokontrol.send_keys(u'Строганов' + Keys.RETURN)
        page.chBnorm.click()

        # Согласование
        self.w.execute_script("arguments[0].scrollIntoView();", page.soglasovanie)
        page.soglasovanie.send_keys(u'Строганов' + Keys.RETURN)

        # Подписание
        self.w.execute_script("arguments[0].scrollIntoView();", page.podpisanie)
        page.podpisanie.send_keys(u'Главный' + Keys.RETURN)

        # Утверждение
        self.w.execute_script("arguments[0].scrollIntoView();", page.utverzhdenie)
        page.utverzhdenie.send_keys(u'Главный' + Keys.RETURN)

        # Ознакомление
        self.w.execute_script("arguments[0].scrollIntoView();", page.oznakomlenie)
        page.oznakomlenie.send_keys(u'Строганов' + Keys.RETURN)

        time.sleep(0.5)

        # Кнопка "Создать"
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnCreateDoc)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnCreateDoc)))
        page.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self.w)
#        self.w.set_page_load_timeout(30)
        time.sleep(3)

#
#        wait.until(EC.title_is(self.w.title))

        assert "Документ" in self.w.title

    # Сохраним ссылку на документ в файл
    def LinkDocWFile(self):

        url = self.w.current_url
        my_file = open("Tests/linkPD.txt", "w")
        my_file.write(str(url))
        my_file.close()