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
# #.... allure generate ./allure_report && allure open allure-report
# # -s команда вывода всех print в консоль
#
#
#
import pytest
import allure



from KSED.Tests.tk15720 import KSEDCreatDocCS_RD
from KSED.Tests.tk15722 import KSEDCreatDocCS_LND


@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_15720(web_browser):

    """ Создание КС _ вид РД"""

    page = KSEDCreatDocCS_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    # saveLink = page.LinkDocWFile()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_15722(web_browser):

    """ Создание КС _ Вид ЛНД"""

    page = KSEDCreatDocCS_LND(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()