#!/bin/sh
#!/usr/bin/python3
# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from KSED.Tests.tk11691 import KSEDCreatDocSZ
from KSED.Tests.tk11704 import KSEDnaprSZSoglas
from KSED.Tests.tk12913 import KSEDPrintAttach
from KSED.Tests.tk12912 import KSEDPrintForm



@allure.feature('Создание Служебной записки')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11691(web_browser):

    """ Создание Служебной записки. """

    page = KSEDCreatDocSZ(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    LinkDocWFile = page.LinkDocWFile()


#@pytest.fixture(scope="session")
@allure.feature('Направление СЗ на согласование')

@pytest.mark.KSED_smoke_test

def test_11704(web_browser):

    """ Направление СЗ на согласование. """

    page = KSEDnaprSZSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    Attach = page.attachment()

    NaprNaSogl = page.NapSoglasovanie()


#@pytest.fixture(scope="session")
@allure.feature('Печать вложений документа')

@pytest.mark.KSED_smoke_test

def test_12913(web_browser):

    """ Печать вложений документа. """

    page = KSEDPrintAttach(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    printAttach = page.printAttach()

    #is_element_present = page.is_element_present()

#@pytest.fixture(scope="session")
@allure.feature('Печать в разделе "Печатные формы"')

@pytest.mark.KSED_smoke_test

def test_12912(web_browser):

    """ Печать в разделе "Печатные формы". """

    page = KSEDPrintForm(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    printForm = page.printForm()

    #is_element_present = page.is_element_present()