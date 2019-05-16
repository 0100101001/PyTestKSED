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
@pytest.mark.KSED_smoke_test_prior
#@pytest.fixture(scope="session")
def test_11655(web_browser):

    """ Создание Поручения. """

    page = KSEDCreatDocPor(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()


@allure.feature('Направление Поручения на согласование')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_13862(web_browser):

    """ Направление Поручения на согласование. """

    page = KSEDCreatDocPorNSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()




@allure.feature('Cогласование поручения')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11778(web_browser):

    """ Cогласование поручения. """

    page = KSEDCreatDocPorSoglas(web_browser)

    LogIn_page = page.LogIN('YatskinRS', 'Changeme!')

    getDoc = page.getDoc()

    Soglasovanie = page.Soglasovanie()


@allure.feature('Отправка отчета в поручении после согласования')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12936(web_browser):

    """ Отправка отчета в поручении после согласования. """

    page = KSEDDocPorSendAllure(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    sendAllure = page.sendAllure()


@allure.feature('Направление Поручения на исполнение')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_12935(web_browser):

    """ Направление Поручения на исполнение. """

    page = KSEDCreatDocPorNIspoln(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NapIspolnenie = page.NapIspolnenie()



@allure.feature('Возврат поручения на доработку при согласовании.')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11943(web_browser):
    """ Возврат поручения на доработку при согласовании. """

    #""" ШАГ 1. Создание Поручения """

    page1 = KSEDCreatDocPor(web_browser)

    LogIn_page = page1.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page1.Creat()

    saveLink = page1.LinkDocWFile()

    # """ ШАГ 2. Направление на согласование """

    page2 = KSEDCreatDocPorNSoglas(web_browser)

    #LogIn_page = page2.LogIN('StroganovSN', 'Changeme!')

    getDoc = page2.getDoc()

    create_route = page2.creation_of_the_approval_route()

    Attach = page2.attachment()

    NaprNaSogl = page2.NapSoglasovanie()

    Logout = page2.USER_LOGOUTs()  # Выйдем из системы

    # """ ШАГ 3. Отклонение согласования """

    page3 = KSEDCreatDocPorDorab(web_browser)

    LogIn_page = page3.LogIN('YatskinRS', 'Changeme!')  # Авторизуемся согласующим созданного документа

    getDoc = page3.getDoc()

    REJECTED = page3.REJECTED()  # Отклоним и вернем документ на доработку

    # Logout = page.USER_LOGOUTs()  # Выйдем из системы
    #
    # LogIn_page = page.LogIN('StroganovSN', 'Changeme!')  # Авторизуемся инициатором
    #
    # getDoc = page.getDoc()  # Откроем документ
    #
    # NaprNaSogl = page.NapSoglasovanie()  # Снова направим на согласование для последовательного выполнения следующего ТК