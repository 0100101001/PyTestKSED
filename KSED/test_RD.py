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



@allure.feature('Создание РД')

@pytest.mark.KSED_smoke_test

@pytest.fixture(scope="session")
def test_11674(web_browser):

    """ Создание Распорядительного документа. """

    page = KSEDCreatDocRD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()


@allure.feature('Направление РД на согласование')

@pytest.mark.KSED_smoke_test

@pytest.fixture(scope="session")
def test_11706(web_browser):

    """ Направление РД на согласование. """

    page = KSEDDocPDNapSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

    Attach = page.attachment()

    addPunkt = page.addPunkt()

    create_route = page.creation_of_the_approval_route()

    adDrassilka = page.rassilka()

 #   Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()