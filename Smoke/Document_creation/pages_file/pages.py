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





def wait_page_loaded(driver):

    time.sleep(2)

    page_loaded = False



    while not page_loaded:

        page_loaded = driver.execute_script("return document.readyState == 'complete';")

        time.sleep(0.1)




class KSEDCreatDoc(PageObject):

    btnCreate = PageElement(xpath='//button[contains(text(), "Создать")]')

    protocol = PageElement(xpath='(//a[contains(text(), "Протокол")])[1]')

    # Форма создания документа
    doc_type = PageElement(xpath='//button[contains(@id, "type-assoc-cntrl-tree-picker-button-button")]')

    addEl = PageElement(xpath='(//span[@class="addIcon"])[7]')

    btnOKDT = PageElement(xpath='//button[contains(@id, "type-assoc-cntrl-ok-button")]')

    title = PageElement(name='prop_lecm-document_title')

    date = PageElement(xpath='//input[contains(@id, "_meeting-date-cntrl-date")]')

    category = PageElement(xpath='//input[contains(@id, "_category-assoc-cntrl-autocomplete-input")]')

    Chairman = PageElement(xpath='//input[contains(@id, "chairman-assoc-cntrl-autocomplete-input")]')

    Secretary = PageElement(xpath='//input[contains(@id, "_secretary-assoc-cntrl-autocomplete-input")]')

    person_present = PageElement(xpath='//input[contains(@id, "_attended-assoc-cntrl-autocomplete-input")]')

    category_doc = PageElement(xpath='//input[contains(@id, "-category-assoc-cntrl-autocomplete-input")]')

    btnCreateDoc = PageElement(xpath='//button[contains(@id, "_default-form-submit-button")]')






    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)



    def Creat(self,):
        # wait = WebDriverWait(self.w, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        wait = WebDriverWait(self.w, 10)

        self.btnCreate.click()

        self.protocol.click()

        assert "Страница создания документа" in self.w.title

 #       time.sleep(1)
        # Атрибуты документа

        # Вид документа
        self.doc_type.click()

#        time.sleep(1)

        self.addEl.click()

 #       time.sleep(1)
        self.btnOKDT.click()

#        time.sleep(1)
        # Заголовок
        self.title.send_keys(u'Документ')

        # Дата совещания
        dd = datetime.date.today().strftime('%d%m%Y')
        self.date.send_keys(dd)
 #       time.sleep(0.5)
        # Категория
        self.category.send_keys(u'Оперативное')
        self.category.send_keys(Keys.RETURN)
        # Председатель
        self.Chairman.send_keys(u'Строганов')
        self.Chairman.send_keys(Keys.RETURN)
        # Секретарь
        self.Secretary.send_keys(u'Главный')
        self.Secretary.send_keys(Keys.RETURN)
        # Присутствовали
        self.person_present.send_keys(u'Яцкин')
        self.person_present.send_keys(Keys.RETURN)
        # Категория документа
        self.category_doc.send_keys(u'Открытый')
        self.category_doc.send_keys(Keys.RETURN)
#        time.sleep(0.5)
        # Кнопка "Создать"
        self.w.execute_script("arguments[0].scrollIntoView();", self.btnCreateDoc)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@id, "_default-form-submit-button")]')))
        self.btnCreateDoc.click()

#        wait.until(EC.number_of_windows_to_be(2))

        wait_page_loaded(self.w)
        self.w.set_page_load_timeout(30)
#        time.sleep(2)

#
        wait.until(EC.title_is(self.w.title))

        assert "Документ" in self.w.title

        # self.mode.click()
        # time.sleep(3)
        # self.fileUpload.click()
        # time.sleep(2)
        # self.files.send_keys('C://test.txt')


        #dd = self.Document_title.text
        #print('Тра та та'+ dd)

#        f = open('text.txt', 'w')
#        f.write(dd)
#        f.close()

        #self.SearchBox.send_keys(dd)

#        time.sleep(4)
