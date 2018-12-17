#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from Tests.tk13799 import KSEDCreatDocPDSoglas
from Tests.tk13756 import KSEDCreatDocPSoglas
from Tests.tk13862 import KSEDCreatDocPorNSoglas
from Tests.tk11706 import KSEDDocPDNapSoglas






# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])


# @allure.feature('Направление Протокола на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_13756(web_browser):
#
#     """ Создание и Направление Протокола на согласование. """
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

# @allure.feature('Направление Произвольного документа на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_13799(web_browser):
#
#     """ Создание и Направление Протокола на согласование. """
#
#     page = KSEDCreatDocPDSoglas(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     Creat_doc  = page.Creat()
#
#     Attach = page.attachment()
#
#     NaprNaSogl = page.NapSoglasovanie()

# @allure.feature('Направление Поручения на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_13862(web_browser):
#
#     """ Направление Поручения на согласование. """
#
#     page = KSEDCreatDocPorNSoglas(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     getDoc = page.getDoc()
#
#     create_route = page.creation_of_the_approval_route()
#
#     Attach = page.attachment()
#
#     NaprNaSogl = page.NapSoglasovanie()

# @allure.feature('Направление РД на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_11706(web_browser):
#
#     """ Направление РД на согласование. """
#
#     page = KSEDDocPDNapSoglas(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     getDoc = page.getDoc()
#
#     Attach = page.attachment()
#
#     addPunkt = page.addPunkt()
#
#     create_route = page.creation_of_the_approval_route()
#
#     adDrassilka = page.rassilka()
#
#  #   Attach = page.attachment()
#
#     NaprNaSogl = page.NapSoglasovanie()

# @allure.feature('Направление Протокола на согласование')
#
# @pytest.mark.KSED_smoke_test
#
# def test_13756(web_browser):
#
#     """ Создание и Направление Протокола на согласование. """
#
#     page = KSEDLogin(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')