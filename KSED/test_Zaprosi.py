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



from KSED.Tests.tk12022 import KSEDallurInDoc
from KSED.Tests.tk12029 import KSEDallurReestr
from KSED.Tests.tk12030 import KSEDallurResolution
from KSED.Tests.tk12011 import KSEDStatAllureVidDic
from KSED.Tests.tk12006 import KSEDallur

from KSED.Tests.tk11677 import KSEDCreateZap
from KSED.Tests.tk11702 import KSEDredZap
from KSED.Tests.tk11742 import KSEDexpZap
from KSED.Tests.tk11744 import KSEDexp_Zap
from KSED.Tests.tk11705 import KSEDdelZap


@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11677(web_browser):

    """  создание запроса """

    page = KSEDCreateZap(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11702(web_browser):
    """  редактирование запроса """

    page = KSEDredZap(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11742(web_browser):
    """  действия с выбранными документами в запросе """

    page = KSEDexpZap(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11744(web_browser):
    """  экспорт документов """

    page = KSEDexp_Zap(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_11705(web_browser):
    """  удаление запроса """

    page = KSEDdelZap(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')


