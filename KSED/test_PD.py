#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure


from KSED.Tests.tk11664 import KSEDCreatDocPD
from KSED.Tests.tk13799 import KSEDCreatDocPDSoglas
from KSED.Tests.tk11955 import KSEDCreatDocPDSoglas_sendDorab


@allure.feature('Создание Произвольного документа')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11664(web_browser):

    """ Создание Произвольного документа. """

    page = KSEDCreatDocPD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()


@allure.feature('Направление Произвольного документа на согласование')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_13799(web_browser):

    """ Создание и Направление Протокола на согласование. """

    page = KSEDCreatDocPDSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

    Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()


@allure.feature('Возврат произвольного документа на доработку при согласовании.')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11955(web_browser):

    """ Возврат произвольного документа на доработку при согласовании.
     Тест падает, причина - не приходит уведомление согласующему (БАГ!)"""

    page = KSEDCreatDocPDSoglas_sendDorab(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345') # Авторизуемся

    Creat_doc  = page.Creat() # Создадим документ

    Attach = page.attachment() # Добавим вложение

#    addPoruch = page.addPoruchenie() # Добавим пункт поручение

    NaprNaSogl = page.NapSoglasovanie() # Направим на согласование

    Logout = page.USER_LOGOUTs() # Выйдем из системы

    LogIn_page = page.LogIN('YatskinRS', '12345') # Авторизуемся согласующим созданного документа

    #notification = page.notificationOpen() # Откроем уведомления и перейдем в документ

    REJECTED = page.REJECTED() # Отклоним и вернем документ на доработку


