#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... H:\Мои документы\ФАЙЛЫ\PyTestKSED\test-tasks-example>python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-result #allure-report
#



import pytest

import allure

from pages import KSEDMainPage





@allure.feature('Document creation')

#@pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
#@pytest.mark.parametrize('Ps', ['12345'])
@pytest.mark.KSED_smoke_test_Protokol_creations

def test_LogInKSED(web_browser):

    """ Check authorization. """

    page = KSEDMainPage(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')


#@pytest.mark.KSED_smoke_test_Protokol_Agreement
#def test_Direction_for_approval(web_browser):

#    test_LogInKSED(web_browser)

#    assert "АРМ" in web_browser.title

 #   Create_New_Prot = page.Create_doc(protokol)


#    def test_Protokol_creation(web_browser, protocol):

#        """ Protokol creation """

#        page = KSEDMainPage(web_browser)

#        Create_New_Prot = page.Create_doc(protocol)