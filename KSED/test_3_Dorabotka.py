#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from Tests.tk11952 import KSEDCreatDocP_sendDorab
from Tests.tk11955 import KSEDCreatDocPDSoglas_sendDorab
from Tests.tk11943 import KSEDCreatDocPorDorab



#
# @allure.feature('Возврат протокола на доработку при согласовании.')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11952(web_browser):
#
#     """ Возврат протокола на доработку при согласовании. """
#
#     page = KSEDCreatDocP_sendDorab(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345') # Авторизуемся
#
#     Creat_doc  = page.Creat() # Создадим документ
#
#     Attach = page.attachment() # Добавим вложение
#
#     addPoruch = page.addPoruchenie() # Добавим пункт поручение
#
#     NaprNaSogl = page.NapSoglasovanie() # Направим на согласование
#
#     Logout = page.USER_LOGOUTs() # Выйдем из системы
#
#     LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа
#
#     notification = page.notificationOpen() # Откроем уведомления и перейдем в документ
#
#     REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку

# @allure.feature('Возврат произвольного документа на доработку при согласовании.')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11955(web_browser):
#
#     """ Возврат произвольного документа на доработку при согласовании.
#      Тест падает, причина - не приходит уведомление согласующему (БАГ!)"""
#
#     page = KSEDCreatDocPDSoglas_sendDorab(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345') # Авторизуемся
#
#     Creat_doc  = page.Creat() # Создадим документ
#
#     Attach = page.attachment() # Добавим вложение
#
# #    addPoruch = page.addPoruchenie() # Добавим пункт поручение
#
#     NaprNaSogl = page.NapSoglasovanie() # Направим на согласование
#
#     Logout = page.USER_LOGOUTs() # Выйдем из системы
#
#     LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа
#
#     #notification = page.notificationOpen() # Откроем уведомления и перейдем в документ
#
#     REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку



# @allure.feature('Возврат произвольного документа на доработку при согласовании.')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11943(web_browser):
#
#     """ Возврат произвольного документа на доработку при согласовании.
#      Тест падает, причина - не приходит уведомление согласующему (БАГ!)"""
#
#     page = KSEDCreatDocPorDorab(web_browser)
#
#     LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа
#
#     getDoc = page.getDoc()
#
#     REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку