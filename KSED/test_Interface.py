#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11690 import KSEDsubordinate_doc
from KSED.Tests.tk11689 import KSEDViewTheDocumentCard


@allure.feature('Просмотр связанных документов в области просмотра разделов (Навигатор)')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11690(web_browser):

    """ Просмотр связанных документов в области просмотра разделов (Навигатор) """

    page = KSEDsubordinate_doc(web_browser)

    LogIn_page = page.LogIN('stroganovsn', '12345') # Авторизуемся

    getDoc = page.subordinate_doc()



@allure.feature('Переход в карточку документа из области просмотра разделов (Навигатор)')
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11689(web_browser):

    """ Переход в карточку документа из области просмотра разделов (Навигатор) """

    page = KSEDViewTheDocumentCard(web_browser)

    LogIn_page = page.LogIN('stroganovsn', '12345') # Авторизуемся

    ViewTheDocumentCard = page.ViewTheDocumentCard()




