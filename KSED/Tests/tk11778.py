#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time

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




class KSEDCreatDocPorSoglas(MPages, dataTest, KSEDLocators):


    def __init__(self, web_driver, uri=dataTest.baseURL):

        super().__init__(web_driver, uri)

    @allure.step("Авторизация")
    def LogIN(self, username, password):

        self.username_text = username
        self.password_text = password

        self.LogIn_button.click()

        self.wait_page_loaded()
        #wait_page_loaded(self._web_driver)

        assert "АРМ" in self._web_driver.title or "Документ" in self._web_driver.title


    # Открытие документа из прошлого ТК
    def getDoc(self):
        my_file = open("Tests/linkDocPoruchenie.txt", "r")
        my_string = my_file.read()
        my_string.strip()
        self._web_driver.get(my_string)
        my_file.close()

        self.wait_page_loaded()

    def Soglasovanie(self, ):

        self.APPROVED_button.wait_to_be_clickable()
        self.APPROVED_button.click()

        # self.prop_bpm_comment.wait_until_not_visible()
        # self.prop_bpm_comment.send_keys('я так хотю')

        self.apply_button_button2.click()

        self.wait_page_loaded(wait_for_xpath_to_disappear='//div[@id="confirm-edit-fields-form-container_mask"]')
        self.wait_page_loaded()

       # открыть согласование вкладку

        self.soglasovanieWkladka2.wait_to_be_clickable()
        self.soglasovanieWkladka2.click()
        # выпадающий список согласований
        self.dropBtn.wait_to_be_clickable()
        self.dropBtn.click()

        self.status_Doc.wait_until_not_visible()
        assert "Согласовано" in self.resultSogl.get_text()


