#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
#



import pytest

import allure

from pages_file.pages import KSEDCreatDoc
from pages_file.pagesLogIn import KSEDLoginPage
from pages_file.pagesAgreement import KSEDAgreement
from pages_file.pagesCheckNotificationAndAgreement import KSEDNotification
from pages_file.pagesCheckNotification import KSEDNotificationOfDecision
from pages_file.allureTest import KSEDallureTest





#@allure.feature('Authorization')

# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# def test_LogInKSED(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDLoginPage(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')



# @allure.feature('Creation_Protocol')
# @pytest.mark.KSED_smoke_test
# def test_CreatDoc(web_browser):
#
#     # Авторизуемся
#     page = KSEDLoginPage(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     # Создадим документ
#     page = KSEDCreatDoc(web_browser)
#
#     page.Creat()
#
#
#
# @allure.feature('Agreement')
# @pytest.mark.KSED_smoke_test
# def test_AgreementDoc(web_browser):
#
#     # Авторизуемся
#     page = KSEDLoginPage(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     # Создадим документ
#     page = KSEDCreatDoc(web_browser)
#
#     page.Creat()
#
#     # Добавим пункт поручение к документу
#     page = KSEDAgreement(web_browser)
#     page.addPoruchenie()
#
#     # Добавим вложение
#     page.attachment()
#
#     # Направим на согласование
#
#     page.Agreement()

# @allure.feature('Check notification and agreement')
# @pytest.mark.KSED_smoke_test
#
# def test_Notification_And_Agreement(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDNotification(web_browser)
#
#     LogIn_page = page.LogIN('YatskinRS', '12345')
#
#     page.NotificationAndAgreement()
#
#
# @allure.feature('Notification of decision')
# @pytest.mark.KSED_smoke_test
#
# def test_Notification(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDNotificationOfDecision(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     page.Notification()
#
#
#
# @allure.feature('AuthorizationFAIL')
#
# #@pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# #@pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# def test_LogInKSED(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDLoginPage(web_browser)
#
#     LogIn_page = page.LogIN('StrogSN', '12345')

@allure.feature('Agreement')
@pytest.mark.KSED_smoke_test
def test_allure(web_browser):

    # Авторизуемся
    page = KSEDLoginPage(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

 #   assert page.login_error_displayed()

    # Откроем отчет
    page = KSEDallureTest(web_browser)

    page.openAllure()




