#!/usr/bin/python3

# -*- encoding=utf8 -*-



import time



from selenium.webdriver import ActionChains

from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys





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

    protocol = PageElement(
        xpath='//a[@class="yuimenuitemlabel yuimenuitemlabel-hassubmenu"][contains(text(),"Протокол")]')

    btnCreate = PageElement(xpath='//button[contains(text(), "Создать")]')

    doc_type = PageElement(xpath='//span/button[@id="template_x002e_content_x002e_document-create_x0023_default'
                                 '_assoc_lecm-eds-document_document-type-assoc-cntrl-tree-picker-button-button"]')
    addEl = PageElement(xpath='(//span[@class="addIcon"])[7]')

    btnOKDT = PageElement(xpath='//button[@id="template_x002e_content_x002e_document'
                                '-create_x0023_default_assoc_lecm-eds-document_document-type-assoc-cntrl-ok-button"]')
    title = PageElement(name='prop_lecm-document_title')

    date = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default'
                              '_prop_lecm-protocol_meeting-date-cntrl-date"]')

    dateW = PageElement(xpath='//td[@id="template_x002e_content_x002e_document-create_x0023_default_prop_lecm-protocol'
                             '_meeting-date-cntrl_t_cell28"]//a[@class="selector"][contains(text(),"26")]')

    category = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default_assoc_'
                                 'lecm-protocol_category-assoc-cntrl-autocomplete-input"]')

    Chairman = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default_assoc_'
                                 'lecm-protocol_meeting-chairman-assoc-cntrl-autocomplete-input"]')
    Secretary = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default_assoc'
                                  '_lecm-protocol_secretary-assoc-cntrl-autocomplete-input"]')
    person_present = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default_assoc'
                                       '_lecm-protocol_attended-assoc-cntrl-autocomplete-input"]')
    category_doc = PageElement(xpath='//input[@id="template_x002e_content_x002e_document-create_x0023_default_assoc'
                                     '_lecm-eds-aspect_document-category-assoc-cntrl-autocomplete-input"]')
    btnCreateDoc = PageElement(xpath='//button[@id="template_x002e_content_x002e_document-create_x0023_default'
                                     '-form-submit-button"]')
    Document_title = PageElement(id_='document-title')

    SearchBox = PageElement(id_='HEADER_SEARCHBOX_FORM_FIELD')

    www = PageElement(xpath='//button[contains(@id, "default-cntrl-split-panel-button-button")]')
    eee = PageElement(xpath='//button[contains(@id, "fileUpload-button-button")]')

    sss = PageElement(xpath='//input[@type="file"]')






    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)

        self.get('http://213.128.208.34/share/page/arm?code=SED')

        wait_page_loaded(self.w)



    def LogIN(self, username, password):

        self.username_text = username

        self.password_text = password

        self.authorization_button.click()



        wait_page_loaded(self.w)

        assert "АРМ" in self.w.title

#    def Create_doc(self, DOC):

        self.btnCreate.click()

        self.protocol.click()

        assert "Страница создания документа" in self.w.title

        time.sleep(1)
        # Атрибуты документа

        # Вид документа
        self.doc_type.click()

        time.sleep(1)

        self.addEl.click()

        time.sleep(1)
        self.btnOKDT.click()

        time.sleep(1)
        # Заголовок
        self.title.send_keys(u'Документ')

        # Дата совещания
        self.date.click()
        time.sleep(0.5)
        self.dateW.click()
        # Категория
        self.category.send_keys(u'Оперативное')
        self.category.send_keys(Keys.RETURN)
        # Председатель
        self.Chairman.send_keys(u'Строганов')
        self.Chairman.send_keys(Keys.RETURN)
        # Секретарь
        self.Secretary.send_keys(u'Строганов')
        self.Secretary.send_keys(Keys.RETURN)
        # Присутствовали
        self.person_present.send_keys(u'Строганов')
        self.person_present.send_keys(Keys.RETURN)
        # Категория документа
        self.category_doc.send_keys(u'Открытый')
        self.category_doc.send_keys(Keys.RETURN)
        # Кнопка "Создать"
        self.btnCreateDoc.click()

        wait_page_loaded(self.w)
        time.sleep(3)
        assert "Документ" in self.w.title

        self.www.click()
        time.sleep(3)
        self.eee.click()
        time.sleep(2)
        self.sss.send_keys('C://logo.png')


        #dd = self.Document_title.text
        #print('Тра та та'+ dd)

#        f = open('text.txt', 'w')
#        f.write(dd)
#        f.close()

        #self.SearchBox.send_keys(dd)

        time.sleep(4)


class Document_agreement(PageObject):


    Point_agreement = PageElement(xpath='//div[contains(text(), "Направить на согласование")]')

#    mode = PageElement(xpath='//a[@title="Показать общую карточку"]')

#    agreement = PageElement(xpath='//em[contains(text(), "Согласование")]')



#    def __init__(self, web_driver, uri=''):
#
#        super().__init__(web_driver, uri)


     #   return ProductsListPage(self.w)





#class ProductsListPage(PageObject):



#    results = MultiPageElement(xpath='//div[@class="n-snippet-cell2__title"]/a')



#    def results_count(self):

#        return len(self.results)