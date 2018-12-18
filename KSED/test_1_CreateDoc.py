#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from KSED.Tests.tk11639 import KSEDLogin
from KSED.Tests.tk11669 import KSEDCreatDocP
from KSED.Tests.tk11674 import KSEDCreatDocRD
from KSED.Tests.tk11679 import KSEDCreatDocReestr
#from Tests.SZ.tk11691 import KSEDCreatDocSZ
from KSED.Tests.tk12957 import KSEDCreatDocREZ
from KSED.Tests.tk11664 import KSEDCreatDocPD
from KSED.Tests.tk11655 import KSEDCreatDocPor
from KSED.Tests.tk11652 import KSEDCreatDocPVH
from KSED.Tests.tk11644 import KSEDCreatDocVH
from KSED.Tests.tk11645 import KSEDCreatDocISH
from KSED.Tests.tk11705 import KSEDCreatDocPa







# @allure.feature('Авторизация')
#
# # @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# # @pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# def test_11639(web_browser):
#
#     """ Проверка авторизации. """
#
#     page = KSEDLogin(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
# @allure.feature('Создание Протокола')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11669(web_browser):
#
#     """ Создание протокола. """
#
#     page = KSEDCreatDocP(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание РД')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11674(web_browser):
#
#     """ Создание Распорядительного документа. """
#
#     page = KSEDCreatDocRD(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
#     saveLink = page.LinkDocWFile()

#
# @allure.feature('Создание Реестра')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11679(web_browser):
#
#     """ Создание реестра. """
#
#     page = KSEDCreatDocReestr(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Служебной записки')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11691(web_browser):
#
#     """ Создание Служебной записки. """
#
#     page = KSEDCreatDocSZ(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Резолюции')
#
# @pytest.mark.KSED_smoke_test
#
# def test_12957(web_browser):
#
#     """ Создание Резолюции. """
#
#     page = KSEDCreatDocREZ(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Произвольного документа')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11664(web_browser):
#
#     """ Создание Произвольного документа. """
#
#     page = KSEDCreatDocPD(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Поручения')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11655(web_browser):
#
#     """ Создание Поручения. """
#
#     page = KSEDCreatDocPor(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
#     saveLink = page.LinkDocWFile()

#
# @allure.feature('Создание Пакет входящей корреспонденции')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11652(web_browser):
#
#     """ Создание Пакет входящей корреспонденции. """
#
#     page = KSEDCreatDocPVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Входящий документ')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11644(web_browser):
#
#     """ Создание Входящий документ. """
#
#     page = KSEDCreatDocVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Исходящий документ')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11645(web_browser):
#
#     """ Создание Исходящий документ. """
#
#     page = KSEDCreatDocISH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()


@allure.feature('Создание Исходящий документ')

@pytest.mark.KSED_smoke_test

def test_11645(web_browser):

    """ Создание Исходящий документ. """

    page = KSEDCreatDocPa(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')