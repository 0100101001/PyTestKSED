#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

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




class KSEDDocPDNapSoglas(Locator, dataTest, KSEDLocators):


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

        self.w.get(KSEDLocators.LinkDocRD)
        wait_page_loaded(self.w)

    # Добавление вложения
    def attachment(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        self.w.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)

        actions = ActionChains(self.w)
        actions.move_to_element(page.vlozheniya).perform()
        time.sleep(0.5)
        page.attachments.click()

        #        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.fileUpload)))
        page.fileUpload.click()

        time.sleep(0.5)
        # wait.until(EC.presence_of_element_located((By.XPATH, KSEDLocators.files)))
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        page.files.send_keys('C://test.txt')

    # Добавление пункта
    def addPunkt(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        # Кликнем по "Показать общую карточку"
        time.sleep(1)
        page.show.click()

        # Кликнем по вкладке "Пункты"
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.punkti)))
        page.punkti.click()

        # Кликнем по кнопке "Добавить пункт"
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.addPunkt)))
        page.addPunkt.click()

        # Заполним поле "Текст пункта РД"
        page.textPunktaRD.send_keys("Произвольный текст")

        # Добавим ответственного исполнителя
        time.sleep(0.5)
        self.w.execute_script("arguments[0].scrollIntoView();", page.otvetstv_ispolnVpunktahRD)
        #WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.otvetstv_ispolnVpunktahRD)))
        page.otvetstv_ispolnVpunktahRD.send_keys("Яцкин" + Keys.RETURN)

        time.sleep(1)
        # Нажмем на кнопку "Сохранить и закрыть"
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnOKform)
        page.btnOKform.click()

    # Создание маршрута согласования
    def creation_of_the_approval_route(self):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        # time.sleep(1)
        # # "Показать общую карточку" клик
        # page.show.click()

        # "Согласование" вкладка
        self.w.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        #self.w.execute_script("arguments[0].scrollIntoView();", page.soglasovanieWkladka)
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
        self.w.execute_script("arguments[0].scrollIntoView();", page.tipeEtap)
        page.tipeEtap.send_keys("Согласование РД" + Keys.ENTER)
        time.sleep(0.5)

        # Заполним "Согласующие"
        page.soglasuychie.send_keys("Яцкин" + Keys.RETURN)

        # Нажмем кнопку "ОК" на форме
        time.sleep(0.5)
        self.w.execute_script("arguments[0].scrollIntoView();", page.btnOKformSogl)
        page.btnOKformSogl.click()

        wait_page_loaded(self.w)

    # Добавление пункта рассылки
    def rassilka(self):
        #Локаторы подготовил, осталось сделать функцию и в файле запуска настроить
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        self.w.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(0.5)
        # Кликнем по вкладке "Рассылка"
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.rassilka)))
        page.rassilka.click()

        # Кликнем по кнопке "Выполнить..."
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.btnVipolnit)))
        page.btnVipolnit.click()

        # Выберем "Создать и заполнить указатель"
        page.punktBtnVipolnit.click()
        time.sleep(0.5)

    # Направление на согласование и проверка статуса документа
    def NapSoglasovanie(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)
        time.sleep(1)
        self.w.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(0.5)

        page.sendFor_approval.click()

        wait_page_loaded(self.w)
        time.sleep(0.5)
        # Проверим статус документа
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.osnSvedeniya)))
        page.osnSvedeniya.click()

        time.sleep(0.5)
        assert "На согласовании" in self.status_Doc.text
