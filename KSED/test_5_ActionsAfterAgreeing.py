#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# Здесь выполняются действия после согласования документа

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from Tests.tk12936 import KSEDDocPorSendAllure




# @allure.feature('Отправка отчета в поручении после согласования')
#
# # @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# # @pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# def test_12936(web_browser):
#
#     """ Отправка отчета в поручении после согласования. """
#
#     page = KSEDDocPorSendAllure(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#     getDoc = page.getDoc()
#
#     sendAllure = page.sendAllure()



