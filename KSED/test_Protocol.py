#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11669 import KSEDCreatDocP
from KSED.Tests.tk13756 import KSEDCreatDocPSoglas
from KSED.Tests.tk11952 import KSEDCreatDocP_sendDorab




@allure.feature('Создание Протокола')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11669(web_browser):

    """ Создание протокола. """

    page = KSEDCreatDocP(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()


@allure.feature('Направление Протокола на согласование')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_13756(web_browser):

    """ Создание и Направление Протокола на согласование. """

    page = KSEDCreatDocPSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    Attach = page.attachment()

    addPoruch = page.addPoruchenie()

    NaprNaSogl = page.NapSoglasovanie()


@allure.feature('Возврат протокола на доработку при согласовании.')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11952(web_browser):

    """ Возврат протокола на доработку при согласовании. """

    page = KSEDCreatDocP_sendDorab(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!') # Авторизуемся

    Creat_doc  = page.Creat() # Создадим документ

    Attach = page.attachment() # Добавим вложение

    addPoruch = page.addPoruchenie() # Добавим пункт поручение

    NaprNaSogl = page.NapSoglasovanie() # Направим на согласование

    Logout = page.USER_LOGOUTs() # Выйдем из системы

    LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа

    notification = page.notificationOpen() # Откроем уведомления и перейдем в документ

    REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку



