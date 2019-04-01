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

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15720(web_browser):

    """ Создание КС _ вид РД"""

    page = KSEDCreatDocCS_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_15750(web_browser):

    """ Создание нетипового маршрута """

    page = KSEDCreatWaySogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()



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

    """ Создание нетипового маршрута """

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