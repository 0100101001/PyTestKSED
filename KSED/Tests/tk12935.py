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

from Pages.PageObject import Locator
from TestData.data import dataTest
from TestData.locators import KSEDLocators




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocPorNIspoln(Locator, dataTest, KSEDLocators):


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

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])

        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        page.newDoc_button.click()

        page.poruchenie.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Тип поручения
        self.w.execute_script("arguments[0].scrollIntoView();", page.tipPoruch)
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.tipPoruch)))
        page.tipPoruch.send_keys(u'Для информации' + Keys.RETURN)

        time.sleep(0.5)
        # Категория документа
        page.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Ответственный исполнитель
        self.w.execute_script("arguments[0].scrollIntoView();", page.otvetstv_ispoln)
        page.otvetstv_ispoln.send_keys(u'Строганов' + Keys.RETURN)

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

    def attachment(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        actions = ActionChains(self.w)
        actions.move_to_element(page.vlozheniya).perform()
        time.sleep(1)
        page.attachments.click()

        #        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.fileUpload)))
        page.fileUpload2.click()

        time.sleep(0.5)
        # wait.until(EC.presence_of_element_located((By.XPATH, KSEDLocators.files)))
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        page.files.send_keys('C://test.txt')

        # # Добавление пункта "Поручение"
        # def addPoruchenie(self, ):
        #     page = Locator(self.w)
        #
        #     wait = WebDriverWait(self.w, 10)
        #
        #     time.sleep(1)
        #     page.show.click()
        #
        #     WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.punkti)))
        #     page.punkti.click()
        #
        #     WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.punktiBtn)))
        #     page.punktiBtn.click()
        #
        #     page.punktPoruch.click()
        #
        #     page.textPoruch.send_keys("Произвольный текст")
        #
        #     page.tipPoruch.send_keys("Поручение по пункту РД" + Keys.RETURN)
        #
        #     page.otvetstv_ispolnVpunktah.send_keys("Главный" + Keys.RETURN)
        #
        #     dd = datetime.date.today().strftime('%d%m%Y')
        #     page.srokIspoln.send_keys(dd)
        #
        #     page.btnOKform.click()

        # Создание маршрута согласования

    def creation_of_the_approval_route(self):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        time.sleep(1)
        # "Показать общую карточку" клик
        page.show.click()

        # "Согласование" вкладка
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.soglasovanieWkladka)))
        page.soglasovanieWkladka.click()

        # "Создать маршрут" клик по кнопке
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.createRuleBtn)))
        page.createRuleBtn.click()

        # Выберем "Индивидуальный маршрут"
        page.createRuleIndivid.click()

        # Появилась форма "Редактирование маршрута" нажмем "ОК"
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnOKform)))
        page.btnOKform.click()

        # Нажмем кнопку "Добавить этап"
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.addEtap)))
        page.addEtap.click()

        time.sleep(1.5)
        # Заполним "Вид этапа"
        page.tipeEtap.send_keys("Согласование" + Keys.RETURN)
        time.sleep(0.5)

        # Заполним "Согласующие"
        page.soglasuychie.send_keys("Яцкин" + Keys.RETURN)

        # Нажмем кнопку "ОК" на форме
        time.sleep(0.5)
        page.btnOKformSogl.click()

        wait_page_loaded(self.w)

    # Направление на исполнение
    def NapIspolnenie(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        time.sleep(1)
        page.sendFor_execution.click()
        time.sleep(1)
        page.btnOKnaprNaIspoln.click()

        wait_page_loaded(self.w)

        # Проверим статус документа
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.osnSvedeniya)))
        page.osnSvedeniya.click()

        assert "На исполнении" in self.status_Doc.text
