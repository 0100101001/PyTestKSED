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
from Tests.tk11674 import KSEDCreatDoc







@allure.feature('Authorization')

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


@pytest.mark.KSED_smoke_test

def test_11639(web_browser):

    """ Check authorization. """

    page = KSEDCreatDoc(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

