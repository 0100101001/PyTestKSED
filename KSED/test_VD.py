#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11644 import KSEDCreatDocVH



@allure.feature('Создание Входящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11644(web_browser):

    """ Создание Входящий документ. """

    page = KSEDCreatDocVH(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()






