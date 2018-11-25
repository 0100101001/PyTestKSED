#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time



from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement





def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)





class KSEDMainPage(PageObject):



    username_text = PageElement(name='username')

    password_text = PageElement(name='password')

    authorization_button = PageElement(xpath='//span/button')



    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get('http://213.128.208.34/share/page/arm?code=SED')

        wait_page_loaded(self.w)



    def LogIN(self, username, password):

        self.username_text = username

        self.password_text = password

        self.authorization_button.click()



        wait_page_loaded(self.w)



     #   return ProductsListPage(self.w)





#class ProductsListPage(PageObject):



#    results = MultiPageElement(xpath='//div[@class="n-snippet-cell2__title"]/a')



#    def results_count(self):

#        return len(self.results)