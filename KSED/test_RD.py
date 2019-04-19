#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11674 import KSEDCreatDocRD
from KSED.Tests.tk11706 import KSEDDocPDNapSoglas
from KSED.Tests.tk12915 import KSEDRDSoglas_sendDorab
from KSED.Tests.tk12929 import KSEDRD_sendPodpis
from KSED.Tests.tk12907 import KSEDRD_DorabPodpis
from KSED.Tests.tk12934 import KSEDRD_Podpis


@allure.feature('Создание РД')
@pytest.mark.KSED_smoke_test_prior
@pytest.fixture(scope="session")
def test_11674(web_browser):

    """ Создание Распорядительного документа. """

    page = KSEDCreatDocRD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()


@allure.feature('Направление РД на согласование')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_11706(web_browser):

    """ Направление РД на согласование. """

    page = KSEDDocPDNapSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    Attach = page.attachment()

    addPunkt = page.addPunkt()

    create_route = page.creation_of_the_approval_route()

    adDrassilka = page.rassilka()

 #   Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()


@allure.feature('Возврат РД на доработку с согласования')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12915(web_browser):

    """ Возврат РД на доработку с согласования. """

    page = KSEDRDSoglas_sendDorab(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    REJECTED = page.REJECTED()



@allure.feature('Направление РД на подписание')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12929(web_browser):

    """ Направление РД на подписание. """

    page = KSEDRD_sendPodpis(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    REJECTED = page.NapPodpis()


@allure.feature('Возврат РД на доработку с подписания')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12907(web_browser):

    """ Возврат РД на доработку с подписания. """

    page = KSEDRD_DorabPodpis(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    Podpisanie_Otklon = page.Podpisanie_Otklon()

    REJECTED = page.NapPodpis()


@allure.feature('Подписание РД')
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_12934(web_browser):

    """ Подписание РД. """

    page = KSEDRD_Podpis(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    Podpis = page.Podpis()
