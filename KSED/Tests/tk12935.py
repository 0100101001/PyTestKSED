#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

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




class KSEDCreatDocPorNIspoln(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)


    @allure.step("Авторизация")

    def LogIN(self, username, password):
        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title

    # Создание документа (открытие формы создания и заполнение атрибутов)
    def Creat(self,):

        self.newDoc_button.wait_to_be_clickable()
        self.newDoc_button.click()

        self.poruchenie.wait_to_be_clickable()
        self.poruchenie.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()
        assert "Страница создания документа" in self.w.title

        # Атрибуты документа

        # Тип поручения
        self.tipPoruch.scroll_to_element()
        self.tipPoruch.wait_until_not_visible()
        self.tipPoruch.send_keys(u'Для информации' + Keys.ENTER)

        # Категория документа
        self.category_doc.wait_until_not_visible()
        self.category_doc.send_keys(u'Открытый' + Keys.RETURN)

        # Ответственный исполнитель
        self.otvetstv_ispoln.scroll_to_element()
        self.otvetstv_ispoln.wait_until_not_visible()
        self.otvetstv_ispoln.send_keys(u'Строганов' + Keys.RETURN)

        # Кнопка "Создать"
        self.btnCreateDoc.scroll_to_element()
        self.btnCreateDoc.wait_to_be_clickable()
        self.btnCreateDoc.click()


        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()
        assert "Документ" in self.w.title

        # Добавление вложения

    def attachment(self, ):

        actions = ActionChains(self._web_driver)
        actions.move_to_element(self.vlozheniya).perform()

        self.attachments.wait_to_be_clickable()
        self.attachments.click()

        self.fileUpload2.wait_to_be_clickable()
        self.fileUpload2.click()

        self.files.wait_to_be_clickable()
        self.files.send_keys('C:\\test.txt')

    # Создание маршрута согласования
    def creation_of_the_approval_route(self):

        # "Показать общую карточку" клик
        self.show.wait_until_not_visible()
        self.show.wait_to_be_clickable()
        self.show.click()

        # "Согласование" вкладка
        self.soglasovanieWkladka.wait_to_be_clickable()
        self.soglasovanieWkladka.click()

        # "Создать маршрут" клик по кнопке
        self.createRuleBtn.wait_to_be_clickable()
        self.createRuleBtn.click()

        # Выберем "Индивидуальный маршрут"
        self.createRuleIndivid.wait_to_be_clickable()
        self.createRuleIndivid.click()

        # Появилась форма "Редактирование маршрута" нажмем "ОК"
        self.btnOKform.wait_to_be_clickable()
        self.btnOKform.click()

        # Нажмем кнопку "Добавить этап"
        self.addEtap.wait_to_be_clickable()
        self.addEtap.click()

        # Заполним "Вид этапа"
        self.tipeEtap.wait_until_not_visible()
        self.tipeEtap.send_keys("Согласование" + Keys.RETURN)

        # Заполним "Согласующие"
        self.soglasuychie.wait_until_not_visible()
        self.soglasuychie.send_keys("Яцкин" + Keys.RETURN)

        # Нажмем кнопку "ОК" на форме
        self.btnOKformSogl.wait_to_be_clickable()
        self.btnOKformSogl.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()

    # Направление на исполнение
    def NapIspolnenie(self, ):

        self.sendFor_execution.wait_to_be_clickable()
        self.sendFor_execution.click()

        self.btnOKnaprNaIspoln.wait_to_be_clickable()
        self.btnOKnaprNaIspoln.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()

        # Проверим статус документа
        self.osnSvedeniya.wait_to_be_clickable()
        self.osnSvedeniya.click()

        self.status_Doc.wait_until_not_visible()
        assert "На исполнении" in self.status_Doc.text
