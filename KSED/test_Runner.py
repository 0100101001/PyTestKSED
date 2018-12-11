#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from Tests.tk11639 import KSEDLogin
from Tests.tk11669 import KSEDCreatDocP
from Tests.tk11674 import KSEDCreatDocRD
from Tests.tk11679 import KSEDCreatDocReestr
from Tests.tk11691 import KSEDCreatDocSZ
from Tests.tk12957 import KSEDCreatDocREZ
from Tests.tk11664 import KSEDCreatDocPD
from Tests.tk11655 import KSEDCreatDocPor







# @allure.feature('Authorization')

# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# def test_11639(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDLogin(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')

# @allure.feature('Создание Протокола')

# @pytest.mark.KSED_smoke_test
#
# def test_11639(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocP(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание РД')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11674(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocRD(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Реестра')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11679(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocReestr(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Служебной записки')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11691(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocSZ(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Резолюции')
#
# @pytest.mark.KSED_smoke_test
#
# def test_12957(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocREZ(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Произвольного документа')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11664(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocPD(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

@allure.feature('Создание Поручения')

@pytest.mark.KSED_smoke_test

def test_11655(web_browser):

    """ Check authorization. """

    page = KSEDCreatDocPor(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()
