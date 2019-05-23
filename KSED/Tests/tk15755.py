#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time, datetime

from selenium.webdriver.support.ui import WebDriverWait

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

class KSEDNaprSogl_RD(MPages, dataTest, KSEDLocators):

    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)


    @allure.step("Авторизация")
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password
        self.LogIn_button.click()
        self.wait_page_loaded()

        assert "АРМ" in self._web_driver.title

    @allure.step("Создание документа")
    def Creat(self,):

        wait = WebDriverWait(self._web_driver, 10)

        self.newDoc_button.click()

        self.cardSogl.click()

        self.wait_page_loaded()

        assert "Страница создания документа" in self._web_driver.title

        # Атрибуты документа
        self.wait_page_loaded()
        # Куратор
        self.kurator.wait_until_not_visible()
        self.kurator.scroll_to_element()
        self.kurator.send_keys(u'Яцкин' + Keys.ENTER)


        # Вид документа
        self.viewSelecton.wait_until_not_visible()
        self.viewSelecton.wait_to_be_clickable()
        self.viewSelecton.click()

        # Выбор РД
        self.viewSelecton.wait_until_not_visible()
        self.rdSelecton.wait_to_be_clickable()
        self.rdSelecton.click()

        # Выбор раздела из РД
        self.btnSelection4.wait_to_be_clickable()
        self.btnSelection4.click()

        # кнопка подтвердить
        self.confirm_6.wait_to_be_clickable()
        self.confirm_6.click()

        # Подписант
        self.podpisanti.wait_until_not_visible()
        self.podpisanti.scroll_to_element()
        self.podpisanti.send_keys(u'Иванов2' + Keys.ENTER)

        # заголовок
        dt = datetime.datetime.today().strftime("%m-%d-%H.%M.%S")
        self.titleCS.scroll_to_element()
        self.titleCS.send_keys(u'Auto РД 15755 ' + dt)

        # кнопка сохранить проект
        self.saveProject.wait_to_be_clickable()
        self.saveProject.click()
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id = "message"]//span[@class = "wait"]')

        assert "Документ" in self._web_driver.title

    def USER_LOGOUTs(self, ):
        # page = Locator(self.w)

        # wait = WebDriverWait(self.w, 10)

        self.user_menu.click()

        self.USER_LOGOUT.click()

        wait_page_loaded(self._web_driver)

        assert "Войти" in self._web_driver.title

    #открытие документа
    def getDoc(self):

        my_file = open("Tests/linkDocCS.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self._web_driver.get(my_string)
        my_file.close()

    # @allure.step("Создание маршрута согласования")
    # def creation_of_the_approval_route(self):
    #
    #     # "Согласование" вкладка
    #     self.soglasovanieWkladka.wait_to_be_clickable()
    #     self.soglasovanieWkladka.click()
    #
    #     # "Создать маршрут" клик по кнопке
    #     self.createRuleBtn.wait_to_be_clickable()
    #     self.createRuleBtn.click()
    #
    #     # Выберем "Типовой маршрут"
    #     self.createRuleTypical.wait_to_be_clickable()
    #     self.createRuleTypical.click()
    #
    #     # Кнопка "Продолжить"
    #     self.btnContinium.wait_to_be_clickable()
    #     self.btnContinium.click()
    #
    #     self.btnSelection_3.wait_to_be_clickable()
    #     self.btnSelection_3.click()  # кнопка + третий выбор
    #
    #     self.confirm_5.wait_to_be_clickable()
    #     self.confirm_5.click()  # кнопка подтвердить
    #
    #
    #     # выпадающий список согласований
    #     self.dropBtn_2.scroll_to_element()
    #     self.dropBtn_2.wait_to_be_clickable()
    #     self.dropBtn_2.click()
    #     # Добавление сотрудника
    #     self.btnAddPerson.wait_to_be_clickable()
    #     self.btnAddPerson.click()
        self.wait_page_loaded()  #
    #     self.reserchInput.send_keys(u'Яцкин' + Keys.ENTER)
    #
    #
    #     self.btnSelection1.wait_to_be_clickable()
    #     self.btnSelection1.click()  # кнопка + третий выбор
    #
    #     self.confirm_5.wait_to_be_clickable()
    #     self.confirm_5.click()  # кнопка подтвердить
    #
    #     # выпадающий список согласований
    #     self.dropBtn_2.wait_to_be_clickable()
    #     self.dropBtn_2.scroll_to_element()
    #     self.dropBtn_2.click()
    #
    #     self.status_Doc.wait_until_not_visible()
    #     assert "Не начато" in self.resultSogl.get_text()
    # @allure.step("Создание маршрута согласования")
    # def creation_of_the_approval_route(self):
    #     # "Согласование" вкладка
    #     self.soglasovanieWkladka.wait_to_be_clickable()
    #     self.soglasovanieWkladka.click()
    #
    #     # "Создать маршрут" клик по кнопке
    #     self.createRuleBtn.wait_to_be_clickable()
    #     self.createRuleBtn.click()
    #
    #     # Выберем "Типовой маршрут"
    #     self.createRuleTypical.wait_to_be_clickable()
    #     self.createRuleTypical.click()
    #
    #     # Кнопка "Продолжить"
    #     self.btnContinium.wait_to_be_clickable()
    #     self.btnContinium.click()
    #
    #     self.btnSelection_3.wait_to_be_clickable()
    #     self.btnSelection_3.click()  # кнопка + третий выбор
    #
    #     self.confirm_5.wait_to_be_clickable()
    #     self.confirm_5.click()  # кнопка подтвердить
    #     self.wait_page_loaded()
    #
    #     # выпадающий список согласований
    #     self.dropBtn_2.scroll_to_element()
    #     self.dropBtn_2.wait_to_be_clickable()
    #     self.dropBtn_2.click()
    #     # Добавление сотрудника
    #     self.btnAddPerson.wait_to_be_clickable()
    #     self.btnAddPerson.click()
        self.wait_page_loaded()  #
    #     self.reserchInput.send_keys(u'Яцкин' + Keys.ENTER)
    #
    #     self.btnSelection1.wait_to_be_clickable()
    #     self.btnSelection1.click()  # кнопка + третий выбор
    #
    #     self.confirm_5.wait_to_be_clickable()
    #     self.confirm_5.click()  # кнопка подтвердить
    #
    #     # выпадающий список согласований
    #     self.dropBtn_2.wait_to_be_clickable()
    #     self.dropBtn_2.scroll_to_element()
    #     self.dropBtn_2.click()
    #
    #     self.resultSogl.wait_to_be_clickable()
    #     assert "Не начато" in self.resultSogl.get_text()
    @allure.step("Создание маршрута согласования")
    def creation_of_the_approval_route(self):
        # "Согласование" вкладка
        self.soglasovanieWkladka.wait_to_be_clickable()
        self.soglasovanieWkladka.click()

        # "Создать маршрут" клик по кнопке
        self.createRuleBtn.wait_to_be_clickable()
        self.createRuleBtn.click()

        # Выберем "Типовой маршрут"
        self.createRuleTypical.wait_to_be_clickable()
        self.createRuleTypical.click()

        # Кнопка "Продолжить"
        self.btnContinium.wait_to_be_clickable()
        self.btnContinium.click()

        self.btnSelection_3.wait_to_be_clickable()
        self.btnSelection_3.click()  # кнопка + третий выбор

        self.confirm_5.wait_to_be_clickable()
        self.confirm_5.click()  # кнопка подтвердить
        self.wait_page_loaded()

        # выпадающий список согласований
        self.dropBtn_2.scroll_to_element()
        self.dropBtn_2.wait_to_be_clickable()
        self.dropBtn_2.click()
        # Добавление сотрудника
        self.btnAddPerson.wait_to_be_clickable()
        self.btnAddPerson.click()
        self.wait_page_loaded()
        self.reserchInput.send_keys(u'Яцкин' + Keys.ENTER)

        self.btnSelection1.wait_to_be_clickable()
        self.btnSelection1.click()  # кнопка + третий выбор

        self.confirm_5.wait_to_be_clickable()
        self.confirm_5.click()  # кнопка подтвердить
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id = "message"]//span[@class = "wait"]')
        # # выпадающий список согласований
        # self.dropBtn_2.wait_to_be_clickable()
        # self.dropBtn_2.scroll_to_element()
        # self.dropBtn_2.click()

        self.resultSogl.wait_to_be_clickable()
        assert "Не начато" in self.resultSogl.get_text()

    # Сохраним ссылку на документ в файл
    def LinkDocWFile(self):

        url = self._web_driver.current_url
        my_file = open("Tests/linkDocCS.txt", "w")
        my_file.write(str(url))
        my_file.close()

    @allure.step("Загрузка вложения")
    def attachment(self, ):
        time.sleep(2)
        self.vlozheniya.move_to_element()
        self.attachments.wait_to_be_clickable()
        self.attachments.click()

        self.fileUpload.wait_to_be_clickable()
        self.fileUpload.click()

        self.files.wait_to_be_clickable()
        self.files.send_keys('D:\\test.txt')
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id = "message"]//span[@class = "wait"]')


    @allure.step("Направление на согласование")
    def NapSoglasovanie(self):
        self.sendFor_approval.wait_to_be_clickable()
        self.sendFor_approval.click()
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id = "message"]//span[@class = "wait"]')
        self.wait_page_loaded()
        # Проверим статус документа
        self.osnSvedeniya.wait_to_be_clickable()
        self.osnSvedeniya.click()

        assert "На согласовании" in self.status_Doc_1.get_text()