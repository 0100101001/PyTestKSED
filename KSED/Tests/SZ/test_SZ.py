#!/bin/sh
#!/usr/bin/python3
# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from KSED.Tests.SZ.tk11691 import KSEDCreatDocSZ
from KSED.Tests.SZ.tk11704 import KSEDnaprSZSoglas




@allure.feature('Создание Служебной записки')

@pytest.mark.KSED_smoke_test

@pytest.fixture(scope="session")
def test_11691(web_browser):

    """ Создание Служебной записки. """

    page = KSEDCreatDocSZ(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    Creat_doc  = page.Creat()

    LinkDocWFile = page.LinkDocWFile()

@pytest.fixture(scope="session")
@allure.feature('Направление СЗ на согласование')

@pytest.mark.KSED_smoke_test

def test_13862(web_browser):

    """ Направление СЗ на согласование. """

    page = KSEDnaprSZSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()