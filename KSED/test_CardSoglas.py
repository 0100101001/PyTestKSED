# #!/bin/sh
# #!/usr/bin/python3
#
# # -*- encoding=utf8 -*-
#
#
#
# # How to run:
#
# #.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
# #.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report

#IEDriver
# #.... allure generate ./allure_report && allure open allure-report
# # -s команда вывода всех print в консоль
#
#
#
import pytest
import allure



from KSED.Tests.tk15720 import KSEDCreatDocCS_RD
from KSED.Tests.tk15722 import KSEDCreatDocCS_LND
from KSED.Tests.tk15723 import KSEDCreatDocCS_ETC
from KSED.Tests.tk15745 import KSEDCreatWaySogl
from KSED.Tests.tk15750 import KSEDCreatWaySogl_RD
from KSED.Tests.tk15744 import KSEDaddPerson
from KSED.Tests.tk15755 import KSEDNaprSogl_RD
from KSED.Tests.tk15758 import KSEDaddNewVersion
from KSED.Tests.tk15765 import KSEDreject_RD


@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15720(web_browser):

    """ Создание КС _ вид РД"""

    page = KSEDCreatDocCS_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15750(web_browser):

    """ Создание типового маршрута """
    # Шаг 1 создание документа
    page = KSEDCreatWaySogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDCreatWaySogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_15755(web_browser):

    """ Направление на согласование """

    # Шаг 1 создание документа
    page = KSEDNaprSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDNaprSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_15765(web_browser):

    """ Отклонение согласования """
    # Шаг 1 создание документа
    page = KSEDreject_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDreject_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDreject_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()




@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15758(web_browser):

    """ Добавление новой версии """

    # Шаг 1 создание документа
    page = KSEDaddNewVersion(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDaddNewVersion(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    # Шаг 4 возврат с согласования


    # Шаг 5 загрузка новой версии файла




@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15722(web_browser):

    """ Создание КС _ Вид ЛНД"""

    page = KSEDCreatDocCS_LND(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15723(web_browser):

    """ Создание КС _ вид Прочие"""

    page = KSEDCreatDocCS_ETC(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()


@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15745(web_browser):

    """ Создание нетипового маршрута """

    page = KSEDCreatWaySogl(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Attach = page.attachment()

    # NaprNaSogl = page.NapSoglasovanie()

    # saveLink = page.LinkDocWFile()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15744(web_browser):

    """ Добавление сотрудника в этап """

    page = KSEDaddPerson(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # create_route = page.creation_of_the_approval_route()
    #
    # Attach = page.attachment()
    #
    # NaprNaSogl = page.NapSoglasovanie()

    # saveLink = page.LinkDocWFile()