#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk12011 import KSEDStatAllureVidDic
from KSED.Tests.tk12013 import KSEDStatAllureTipDoc


@allure.feature('Статический отчет "Сводка по видам документов')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12011(web_browser):

    """ Статический отчет "Сводка по видам документов """

    page = KSEDStatAllureVidDic(web_browser)

    LogIn_page = page.LogIN('stroganovsn', '12345') # Авторизуемся

    getDoc = page.StatAllureVidDic()



@allure.feature('Статический отчет "Сводка по типам документов')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12013(web_browser):

    """ Статический отчет "Сводка по типам документов """

    page = KSEDStatAllureTipDoc(web_browser)

    LogIn_page = page.LogIN('stroganovsn', '12345') # Авторизуемся

    getDoc = page.StatAllureTipDoc()





