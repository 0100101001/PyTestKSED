#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11645 import KSEDCreatDocISH
from KSED.Tests.tk11644 import KSEDCreatDocVH
from KSED.Tests.tk11679 import KSEDCreatDocReestr
from KSED.Tests.tk11691 import KSEDCreatDocSZ
from KSED.Tests.tk12929 import KSEDRD_sendPodpis




@allure.feature('Создание Исходящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")


def test_11645(web_browser):

    """ Создание Исходящий документ. """

    page = KSEDCreatDocISH(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

@allure.feature('Создание Исходящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")


def test_11644(web_browser):

    """ Создание Исходящий документ. """

    page = KSEDCreatDocVH(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc = page.Creat()

@allure.feature('Создание Исходящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")

def test_11679(web_browser):

    """ Создание реестра """

    page = KSEDCreatDocReestr(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc = page.Creat()

@allure.feature('Создание Исходящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")

def test_11691(web_browser):

    """ Создание Исходящий документ. """

    page = KSEDCreatDocSZ(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc = page.Creat()

@allure.feature('Создание Исходящий документ')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")



def test_12929(web_browser):

    """ Направление на согласование РД """

    page = KSEDRD_sendPodpis(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

    NaprNaSogl = page.NapPodpis()