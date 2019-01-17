#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.pages import MPages




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocPorNSoglas(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)

    # Авторизация
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title


    # Открытие документа из прошлого ТК
    def getDoc(self):

        my_file = open("Tests/linkDocPoruchenie.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self._web_driver.get(my_string)
        my_file.close()

        self.wait_page_loaded()

    # Добавление вложения
    def attachment(self,):

        actions = ActionChains(self._web_driver)
        self.vlozheniya.wait_until_not_visible()
        actions.move_to_element(self.vlozheniya).perform()

        self.attachments.wait_to_be_clickable()
        self.attachments.click()

        self.fileUpload2.wait_to_be_clickable()
        self.fileUpload2.click()

        self.files.wait_to_be_clickable()
        self.files.send_keys('C:\\test.txt')

    # Создание маршрута согласования
    def creation_of_the_approval_route(self):

       # time.sleep(1)
        # "Показать общую карточку" клик
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

        #time.sleep(1.5)
        # Заполним "Вид этапа"
        self.tipeEtap.wait_to_be_clickable()
        self.tipeEtap.send_keys("Согласование" + Keys.RETURN)
        #time.sleep(1)

        # Заполним "Согласующие"
        self.soglasuychie.wait_to_be_clickable()
        self.soglasuychie.send_keys("Яцкин" + Keys.ENTER)
        #time.sleep(3)
        # Нажмем кнопку "ОК" на форме
        #time.sleep(1)
        self.btnOKformSogl.scroll_to_element()
        self.btnOKformSogl.wait_to_be_clickable()
        self.btnOKformSogl.click()
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        #self.wait_page_loaded()

    # Направление на согласование и проверка статуса документа
    def NapSoglasovanie(self, ):

        self.sendFor_approval.wait_to_be_clickable()
        self.sendFor_approval.click()

        self.wait_page_loaded()

        # Проверим статус документа
        self.osnSvedeniya.wait_to_be_clickable()
        self.osnSvedeniya.click()
        self.status_Doc.wait_until_not_visible()

        assert "На согласовании" in self.status_Doc.text
