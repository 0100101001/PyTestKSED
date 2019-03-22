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
from KSED.Tests.tk12012_1 import KSEDStatAllureTemDoc
from KSED.Tests.tk12012_2 import KSEDStatAllureTemDocO
from KSED.Tests.tk12030 import KSEDallurResolution
from KSED.Tests.tk12006 import KSEDallur
from KSED.Tests.tk12022 import KSEDallurInDoc
from KSED.Tests.tk12025 import KSEDallurIsp
from KSED.Tests.tk12026 import KSEDallurDeadLine
from KSED.Tests.tk12027 import KSEDallurEffPodr
from KSED.Tests.tk12029 import KSEDallurReestr


@allure.feature('Статический отчет "Сводка по видам документов')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12011(web_browser):

    """ Статический отчет "Сводка по видам документов """

    page = KSEDStatAllureVidDic(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

    getDoc = page.StatAllureVidDic()


@allure.feature('Статический отчет "Сводка по типам документов')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12013(web_browser):

    """ Статический отчет "Сводка по типам документов """

    page = KSEDStatAllureTipDoc(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

    getDoc = page.StatAllureTipDoc()


@allure.feature('Статический отчет "Сводка по тематикам документов')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12012_1(web_browser):

    """ Статический отчет "Сводка по тематикам документов """

    page = KSEDStatAllureTemDoc(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

    getDoc = page.StatAllureTemDoc()


@allure.feature('Статический отчет "Сводка по тематикам документов (Объедин.)')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12012_2(web_browser):

    """ Статический отчет "Сводка по тематикам документов(Объедин.) """

    page = KSEDStatAllureTemDocO(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

    getDoc = page.StatAllureTemDocO()

  #  closeWindow = page.closeWindow()

  #  getDoc = page.StatAllureTemDocO()

@allure.feature('Статический отчет "Сводка по тематикам документов (Объедин.)')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12030(web_browser):

    """  """

    page = KSEDallurResolution(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

 #   getDoc = page.StatAllureTemDocO()

  #  closeWindow = page.closeWindow()

  #  getDoc = page.StatAllureTemDocO()

#****Сергей
@allure.feature('Проверка отчетов в узле "Журналы" раздела "Отчеты"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12006(web_browser):

    """  """

    page = KSEDallur(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')


@allure.feature('Отчет "Исполнение входящих документов"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12022(web_browser):

    """  """

    page = KSEDallurInDoc(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@allure.feature('Отчет "Исполнительская дисциплина по авторам"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12025(web_browser):

    """  """

    page = KSEDallurIsp(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@allure.feature('Отчет "Неисполненные поручения с истекшим сроком"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12026(web_browser):

    """  """

    page = KSEDallurDeadLine(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@allure.feature('Отчет "Продуктивность по исполнителям"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12027(web_browser):

    """  """

    page = KSEDallurEffPodr(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@allure.feature('Отчет "Реестр для закрытия неактуальных контрольных поручений"')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12029(web_browser):

    """  """

    page = KSEDallurReestr(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
