#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure


from KSED.Tests.tk12957 import KSEDCreatDocREZ



@allure.feature('Создание Резолюции')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12957(web_browser):

    """ Создание Резолюции. """

    page = KSEDCreatDocREZ(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()



