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



@allure.feature('Авторизация')
# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11639(web_browser):

    """ Проверка авторизации. """

    page = KSEDLogin(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')






