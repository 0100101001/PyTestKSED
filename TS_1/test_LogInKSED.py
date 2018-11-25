#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-



# How to run:

#.... H:\Мои документы\ФАЙЛЫ\PyTestKSED\test-tasks-example>python -m pytest -v --driver Chrome --driver-path C:\path\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
#



import pytest

import allure

from pages import KSEDMainPage





@allure.feature('Authorization in the KSED system')

@pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
@pytest.mark.parametrize('Ps', ['12345'])

def test_LogInKSED(web_browser, Ln, Ps):

    """ Check authorization. """



    page = KSEDMainPage(web_browser)

    LogIn_page = page.LogIN(Ln, Ps)



    # Verify that default search page shows 48 results:

#    assert results_page.results_count() == 48, 'No results found!'