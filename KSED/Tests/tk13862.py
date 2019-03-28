#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from KSED.Pages.PageObject import Locator
from KSED.TestData.data import dataTest
from KSED.TestData.locators import KSEDLocators
from KSED.pages import MPages




def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDocPorNSoglas(MPages, Locator, dataTest, KSEDLocators):


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
        # page = Locator(self.w)
        #
        # actions = ActionChains(self.w)
        # actions.move_to_element(page.vlozheniya).perform()
        # time.sleep(0.5)
        # page.attachments.click()

        # actions = ActionChains(self.w)
        # self.vlozheniya.wait_until_not_visible()
        # actions.move_to_element(self.vlozheniya).perform()

        self.vlozheniya.move_to_element()
        self.attachments.wait_to_be_clickable()
        self.attachments.click()

        self.fileUpload2.wait_to_be_clickable()
        self.fileUpload2.click()

        # self.fileUpload3.wait_to_be_clickable()
        # self.fileUpload3.click()

        self.files.wait_to_be_clickable()
        self.files.send_keys('D:\\test.txt')

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


        # Заполним "Вид этапа"
        # self.tipeEtap.wait_until_not_visible()
        # self.tipeEtap.send_keys("Согласование" + Keys.RETURN)
        # self.tipeEtap.send_keys(Keys.RETURN)

        self.btnTree.wait_to_be_clickable()
        self.btnTree.click() # нажать на кнопку ...

        self.btnSelection3.wait_to_be_clickable()
        self.btnSelection3.click() # кнопка + третий выбор

        self.confirm_5.wait_to_be_clickable()
        self.confirm_5.click()  # кнопка + третий выбор

        # Заполним "Согласующие"
        self.soglasuychie.wait_until_not_visible()
        self.soglasuychie.send_keys("Яцкин" + Keys.RETURN)



        #time.sleep(3)
        # Нажмем кнопку "ОК" на форме
        #time.sleep(1)
        self.btnOKformSogl.scroll_to_element()
        self.btnOKformSogl.wait_to_be_clickable()
        self.btnOKformSogl.click()
        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        #self.wait_page_loaded()

    # Направление на согласование и проверка статуса документа
    def NapSoglasovanie(self):

        self.sendFor_approval.wait_to_be_clickable()
        self.sendFor_approval.click()
        #self.wait_page_loaded()
        time.sleep(4)
        # Проверим статус документа
        self.osnSvedeniya.wait_to_be_clickable()
        self.osnSvedeniya.click()


        assert "На согласовании" in self.status_Doc.get_text()

    def USER_LOGOUTs(self, ):
        # page = Locator(self.w)

        # wait = WebDriverWait(self.w, 10)

        self.user_menu.click()

        self.USER_LOGOUT.click()

        wait_page_loaded(self._web_driver)

        assert "Войти" in self._web_driver.title