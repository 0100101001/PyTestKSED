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




class KSEDCreatDocPorNSoglas(Locator, dataTest, KSEDLocators):


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

        my_file = open("Tests/linkDocPoruchenie.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self.w.get(my_string)
        my_file.close()

        #self.w.get(KSEDLocators.LinkDocRD)
        wait_page_loaded(self.w)

    # Добавление вложения
    def attachment(self,):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        actions = ActionChains(self.w)
        actions.move_to_element(page.vlozheniya).perform()
        time.sleep(0.5)
        page.attachments.click()

        #        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "default-dialog")]')))
        time.sleep(0.5)
        #wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.fileUpload)))
        page.fileUpload2.click()

        time.sleep(0.5)
        #wait.until(EC.presence_of_element_located((By.XPATH, KSEDLocators.files)))
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

    # Направление на согласование и проверка статуса документа
    def NapSoglasovanie(self, ):
        page = Locator(self.w)

        wait = WebDriverWait(self.w, 10)

        time.sleep(1)
        page.sendFor_approval.click()

        wait_page_loaded(self.w)

        # Проверим статус документа
        wait.until(EC.element_to_be_clickable((By.XPATH, KSEDLocators.osnSvedeniya)))
        page.osnSvedeniya.click()

        assert "На согласовании" in self.status_Doc.text

    # # Сохраним ссылку на документ в файл
    # def LinkDocWFile(self):
    #
    #     url = self.w.current_url
    #     my_file = open("TestData\linkDoc.txt", "w")
    #     my_file.write(str(url))
    #     my_file.close()

