#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from Tests.tk13799 import KSEDCreatDocPDSoglas
from Tests.tk13756 import KSEDCreatDocPSoglas
from Tests.tk11778 import KSEDCreatDocPorSoglas







# @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# @pytest.mark.parametrize('Ps', ['12345'])



@allure.feature('Направление Cогласование поручения')

@pytest.mark.KSED_smoke_test

def test_11778(web_browser):

    """ Направление Cогласование поручения. """

    page = KSEDCreatDocPorSoglas(web_browser)

    LogIn_page = page.LogIN('StroganovSN', '12345')

    getDoc = page.getDoc()

