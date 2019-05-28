#!/bin/sh
#!/usr/bin/python3

# -*- encoding=utf8 -*-

# How to run:

#.... python -m pytest -v --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
#.... allure generate ./allure_report && allure open allure-report
# -s команда вывода всех print в консоль

import pytest
import allure

from KSED.Tests.tk11645 import KSEDCreatDocISH
from KSED.Tests.tk11644 import KSEDCreatDocVH
from KSED.Tests.tk11679 import KSEDCreatDocReestr
from KSED.Tests.tk11691 import KSEDCreatDocSZ
from KSED.Tests.tk12929 import KSEDRD_sendPodpis
from KSED.Tests.tk18361 import KSEDreturnDisAfterTakeTask
from KSED.Tests.tk18362 import KSEDsoftDisFromDelegatAfterReject_RD
from KSED.Tests.tk18363 import KSEDsoftDisAfterTakeTask




# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
#
# def test_11645(web_browser):
#
#     """ Создание Исходящий документ. """
#
#     page = KSEDCreatDocISH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     Creat_doc  = page.Creat()
#
# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
#
# def test_11644(web_browser):
#
#     """ Создание Исходящий документ. """
#
#     page = KSEDCreatDocVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     Creat_doc = page.Creat()
#
# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
# def test_11679(web_browser):
#
#     """ Создание реестра """
#
#     page = KSEDCreatDocReestr(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     Creat_doc = page.Creat()
#
# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
# def test_11691(web_browser):
#
#     """ Создание Исходящий документ. """
#
#     page = KSEDCreatDocSZ(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     Creat_doc = page.Creat()
#
# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
#
#
# def test_12929(web_browser):
#
#     """ Направление на согласование РД """
#
#     page = KSEDRD_sendPodpis(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     getDoc = page.getDoc()
#
#     NaprNaSogl = page.NapPodpis()
#
# @allure.feature('Создание Исходящий документ')
# @pytest.mark.KSED_smoke_test
# #@pytest.fixture(scope="session")
#
#
# def test_11644(web_browser):
#
#     """ Создание Исходящий документ. """
#
#     page = KSEDCreatDocVH(web_browser)
#
#     LogIn_page = page.LogIN('StroganovSN', 'Changeme!')
#
#     Creat_doc = page.Creat()


@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_18361(web_browser):

    """ Отзыв решения после согласования делегата"""
    # Шаг 1 создание документа
    page = KSEDreturnDisAfterTakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDreturnDisAfterTakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 забрать задачу

    page2 = KSEDreturnDisAfterTakeTask(web_browser)

    LogIn_page = page2.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    take = page2.takeTask_RD()

    reject = page2.rejectDoc()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    page3 = KSEDreturnDisAfterTakeTask(web_browser)

    LogIn_page = page3.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    returnDis = page3.returnDecision_RD()

@pytest.mark.KSED_smoke_test
# @pytest.fixture(scope="session")
def test_18362(web_browser):
    """  Отзыв решения делегата после отклонения согласования основного согласующего"""
    # Шаг 1 создание документа
    page = KSEDsoftDisFromDelegatAfterReject_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Шаг 2 создание маршрута

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDsoftDisFromDelegatAfterReject_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    page3 = KSEDsoftDisFromDelegatAfterReject_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    returnDis = page3.softDecision_RD()




@pytest.mark.KSED_smoke_test
# @pytest.fixture(scope="session")
def test_18363(web_browser):
    """ Смягчение решения после согласования делегата"""
    # Шаг 1 создание документа
    page = KSEDsoftDisAfterTakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDsoftDisAfterTakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 забрать задачу

    page2 = KSEDsoftDisAfterTakeTask(web_browser)

    LogIn_page = page2.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    take = page2.takeTask_RD()

    reject = page2.rejectDoc()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    page3 = KSEDsoftDisAfterTakeTask(web_browser)

    LogIn_page = page3.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    returnDis = page3.softDecision_RD()