#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


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




class KSEDCreatDocPSoglas(Locator, dataTest, KSEDLocators):


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

        page.protocol.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Вид документа
        page.doc_type.click()

#        time.sleep(1)

        page.addEl.click()

 #       time.sleep(1)
        page.btnOKDT.click()

#        time.sleep(1)
        # Заголовок
        page.title.send_keys(u'Документ')

        # Дата совещания
        dd = datetime.date.today().strftime('%d%m%Y')
        page.date.send_keys(dd)
        time.sleep(0.5)
        # Категория
        page.category.send_keys(u'Оперативное'+Keys.RETURN)

        # Председатель
        page.Chairman.send_keys(u'Строганов'+Keys.RETURN)

        # Секретарь
        page.Secretary.send_keys(u'Главный'+Keys.RETURN)

        # Присутствовали
        page.person_present.send_keys(u'Яцкин'+Keys.RETURN)

        # Категория документа
        page.category_doc.send_keys(u'Открытый'+Keys.RETURN)

        time.sleep(0.5)
        # Кнопка "Создать"
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnCreateDoc)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnCreateDoc)))
        page.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self.w)
#        self.w.set_page_load_timeout(30)
        time.sleep(2)

#
#        wait.until(EC.title_is(self.w.title))

        assert "Документ" in self.w.title

    # Добавление вложения
    def attachment(self,):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.mode.click()

        #        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))

        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.fileUpload)))
        page.fileUpload.click()

        #        time.sleep(0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, KSEDLocators.files)))
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        page.files.send_keys('C:\\test.txt')

    # Добавление пункта "Поручение"
    def addPoruchenie(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        time.sleep(1)
        page.show.click()

        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.punkti)))
        page.punkti.click()

        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.punktiBtn)))
        page.punktiBtn.click()

        page.punktPoruch.click()

        page.textPoruch.send_keys("Произвольный текст")

        page.tipPoruch.send_keys("Поручение по пункту РД" + Keys.RETURN)

        page.otvetstv_ispolnVpunktah.send_keys("Главный" + Keys.RETURN)

        dd = datetime.date.today().strftime('%d%m%Y')
        page.srokIspoln.send_keys(dd)

        page.btnOKform.click()
        time.sleep(1)
    # Направление на согласование и проверка статуса документа
    def NapSoglasovanie(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)


        page.sendFor_approval.click()

        wait_page_loaded(self.w)

        # Проверим статус документа
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.osnSvedeniya)))
        page.osnSvedeniya.click()

        assert "На согласовании" in self.status_Doc.text

