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
from Tests.tk11652 import KSEDCreatDocPVH
from Tests.tk11644 import KSEDCreatDocVH
from Tests.tk11645 import KSEDCreatDocISH
from Tests.tk13756 import KSEDCreatDocPSoglas







# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])


# @allure.feature('Направление Протокола на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_13756(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocPSoglas(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
#     Attach = page.attachment()
#
#     addPoruch = page.addPoruchenie()
#
#     NaprNaSogl = page.NapSoglasovanie()

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

# @allure.feature('Создание Поручения')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11655(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocPor(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Пакет входящей корреспонденции')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11652(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocPVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

# @allure.feature('Создание Входящий документ')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11644(web_browser):
#
#     """ Check authorization. """
#
#     page = KSEDCreatDocVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()

@allure.feature('Создание Исходящий документ')

@pytest.mark.KSED_smoke_test

def test_11645(web_browser):

    """ Check authorization. """

    page = KSEDCreatDocISH(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()
