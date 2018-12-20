#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure


from KSED.Tests.tk11655 import KSEDCreatDocPor
from KSED.Tests.tk13862 import KSEDCreatDocPorNSoglas
from KSED.Tests.tk11778 import KSEDCreatDocPorSoglas
from KSED.Tests.tk11943 import KSEDCreatDocPorDorab
from KSED.Tests.tk12936 import KSEDDocPorSendAllure
from KSED.Tests.tk12935 import KSEDCreatDocPorNIspoln


@allure.feature('Создание Поручения')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11655(web_browser):

    """ Создание Поручения. """

    page = KSEDCreatDocPor(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()


@allure.feature('Направление Поручения на согласование')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_13862(web_browser):

    """ Направление Поручения на согласование. """

    page = KSEDCreatDocPorNSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()


@allure.feature('Возврат поручения на доработку при согласовании.')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11943(web_browser):

    """ Возврат поручения на доработку при согласовании. """

    page = KSEDCreatDocPorDorab(web_browser)

    LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа

    getDoc = page.getDoc()

    REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку

    NaprNaSogl = page.NapSoglasovanie() # Снова направим на согласование для последовательного выполнения следующего ТК

@allure.feature('Cогласование поручения')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11778(web_browser):

    """ Cогласование поручения. """

    page = KSEDCreatDocPorSoglas(web_browser)

    LogIn_page = page.LogIN('YatskinRS', '12345')

    getDoc = page.getDoc()

    Soglasovanie = page.Soglasovanie()


@allure.feature('Отправка отчета в поручении после согласования')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12936(web_browser):

    """ Отправка отчета в поручении после согласования. """

    page = KSEDDocPorSendAllure(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

    sendAllure = page.sendAllure()


@allure.feature('Направление Поручения на исполнение')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12935(web_browser):

    """ Направление Поручения на исполнение. """

    page = KSEDCreatDocPorNIspoln(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc = page.Creat()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NapIspolnenie = page.NapIspolnenie()