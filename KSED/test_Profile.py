#!/bin/sh
#!/usr/bin/python3
# -*- encoding=utf8 -*-



# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль



import pytest
import allure

from KSED.Tests.tk11775 import KSEDuser_LOGOUT
from KSED.Tests.tk11774 import Edit_Password
from KSED.Tests.tk11772 import KSEDmyprofile
from KSED.Tests.tk11773 import KSEDlogicESM
from KSED.Tests.tk11728 import Edit_Profile
from KSED.Tests.tk11727 import KSEDAbsence




@allure.feature('Выход из системы')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11775(web_browser):

    """ Выход из системы. """

    page = KSEDuser_LOGOUT(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    logout = page.USER_LOGOUTs()

@allure.feature('Изменение пароля пользователя')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11774(web_browser):

    """ Изменение пароля пользователя. """

    page = Edit_Password(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    edit_password = page.edit_password('12345', '12345') # введем старый пароль и новый пароль

    # Проверим изменился ли пароль (выйдем из системы и авторизуемся с новым паролем)
    logout = page.USER_LOGOUTs()

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

@allure.feature('Страница профиля пользователя')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11772(web_browser):

    """ Страница профиля пользователя. """

    page = KSEDmyprofile(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getMyprofile = page.getMyprofile()


@allure.feature('Страница Логика ECM.Мой профиль')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11773(web_browser):

    """ Страница Логика ECM.Мой профиль. """

    page = KSEDlogicESM(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getMyprofile = page.getLogicESM()


@allure.feature('Изменение профиля')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11728(web_browser):

    """ Изменение профиля """

    page = Edit_Profile(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getMyprofile = page.edit_profile()


@allure.feature('Включить отсутствие: "Меня нет в офисе"')

@pytest.mark.KSED_smoke_test

#@pytest.fixture(scope="session")
def test_11773(web_browser):

    """ Включить отсутствие: "Меня нет в офисе". """

    page = KSEDAbsence(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getMyprofile = page.getLogicESM()

    Absence = page.Absence()


