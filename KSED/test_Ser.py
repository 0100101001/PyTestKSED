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
# import pytest
# import allure
#
# # from KSED.Tests.tk12022 import KSEDallurInDoc
# # from KSED.Tests.tk12029 import KSEDallurReestr
# # from KSED.Tests.tk12030 import KSEDallurResolution
# # from KSED.Tests.tk12011 import KSEDStatAllureVidDic
# # from KSED.Tests.tk12006 import KSEDallur
# # from KSED.Tests.tk11656 import KSEDexpDoc
# from KSED.Tests.tk11639 import KSEDLogin
#
# @allure.feature('Авторизация')
# # #@pytest.fixture(scope="session")
# # @pytest.mark.parametrize('Ln', ['StroganovSN', 'tst_gid'])
# # @pytest.mark.parametrize('Ps', ['12345'])
# @pytest.mark.KSED_smoke_test
#
# # def test_11677(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreateZap(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#
# # def test_12022(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDallurInDoc(web_browser)
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#
# # def test_12029(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDallurReestr(web_browser)
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
#
#
# # def test_11639(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDLogin(web_browser)
# #     LogIn_page = page.LogIN('stroganovsn', '12345')
#
#
# # def test_12030(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDallurResolution(web_browser)
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #
# # def test_12011(web_browser):
# #
# #     page = KSEDStatAllureVidDic(web_browser)
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #
# # def test_12006(web_browser):
# #     page = KSEDallur(web_browser)
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
#
# #
# # def test_11702(web_browser):
# #     """ Check authorization. """
# #
# #     page = KSEDredZap(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# # def test_11705(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDdelZap(web_browser)
#
#     # LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# # @allure.feature('Создание Протокола')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11669(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocP(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание РД')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11674(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocRD(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Реестра')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11679(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocReestr(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Служебной записки')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11691(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocSZ(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Резолюции')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_12957(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocREZ(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Произвольного документа')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11664(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocPD(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Поручения')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11655(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocPor(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Пакет входящей корреспонденции')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11652(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocPVH(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Входящий документ')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11644(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocVH(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
# #
# # @allure.feature('Создание Исходящий документ')
# #
# # @pytest.mark.KSED_smoke_test
# #
# # def test_11645(web_browser):
# #
# #     """ Check authorization. """
# #
# #     page = KSEDCreatDocISH(web_browser)
# #
# #     LogIn_page = page.LogIN('StroganovSN', '12345')
# #
# #     Creat_doc  = page.Creat()
