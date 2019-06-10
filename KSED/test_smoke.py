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
# #.... python -m pytest -v test_CardSoglas.py::test_15772 --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report
# #.... python -m pytest -v test_CardSoglas.py --driver Chrome --driver-path WebDriver\chromedriver --alluredir ./allure_report

# #.... python -m pytest -v --driver FireFox --driver-path WebDriver\geckodriver --alluredir ./allure_report
# #.... python -m pytest -v test_CardSoglas.py --driver FireFox --driver-path WebDriver\geckodriver --alluredir ./allure_report
# #.... python -m pytest -v test_CardSoglas.py::test_18338 --driver FireFox --driver-path WebDriver\geckodriver --alluredir ./allure_report
# #.... python -m pytest -v --driver IE --driver-path WebDriver\IEDriverServer --alluredir ./allure_report

#IEDriver
# #.... allure generate ./allure_report && allure open allure-report
# # -s команда вывода всех print в консоль
#
#
#
import pytest
import allure



from KSED.Tests.t681 import KSEDCreatDocCS_RD
from KSED.Tests.t682 import KSEDCreatDocCS_LND
from KSED.Tests.tk15723 import KSEDCreatDocCS_ETC
from KSED.Tests.tk15745 import KSEDCreatWaySogl
from KSED.Tests.tk15750 import KSEDCreatWaySogl_RD
from KSED.Tests.tk15744 import KSEDaddPerson
from KSED.Tests.tk15755 import KSEDNaprSogl_RD
from KSED.Tests.tk15758 import KSEDaddNewVersion
from KSED.Tests.tk15759 import KSEDaddNewAtt
from KSED.Tests.tk15765 import KSEDreject_RD
from KSED.Tests.tk15764 import KSEDacceptSogl_RD
from KSED.Tests.tk15767 import KSEDinnerSogl_RD
from KSED.Tests.tk15772 import KSEDrejectInnerSogl_RD
from KSED.Tests.tk15777 import KSEDrejectTaskInnerSogl_RD
from KSED.Tests.tk15779 import KSEDrepeatInnerSogl_RD
from KSED.Tests.tk15780 import KSEDAcceptInnerSogl_RD
from KSED.Tests.tk15781 import KSEDaddComment
from KSED.Tests.tk15806 import KSEDtakeTask
from KSED.Tests.tk15807 import KSEDbackTask
from KSED.Tests.tk15810 import KSEDreturnDecision_RD
from KSED.Tests.tk15812 import KSEDsoftDecision_RD
from KSED.Tests.tk18300 import KSEDchangeAfterRejectInnerSogl_RD
from KSED.Tests.tk18302 import KSEDsoftDesAfterRejectInnerSogl_RD
from KSED.Tests.tk18327 import KSEDchangeAfterAcceptInnerSogl_RD
from KSED.Tests.tk18329 import KSEDchangeAfterAcceptWithRemarkInnerSogl_RD
from KSED.Tests.tk18330 import KSEDsoftDisAfterAcceptWithRemarkInnerSogl_RD
from KSED.Tests.tk18332 import KSEDaddCommentInnerSogl_RD
from KSED.Tests.tk18334 import KSEDInnerSoglAfterAddComment_RD
from KSED.Tests.tk18336 import KSEDacceptSoglwithRemark_RD
from KSED.Tests.tk18337 import KSEDrejectAfterAcceptSoglwithRemark_RD
from KSED.Tests.tk18338 import KSEDsoftDisAfterAcceptSoglwithRemark_RD
from KSED.Tests.tk18360 import KSEDreturnDisFromDelegatAfterReject_RD
from KSED.Tests.tk18361 import KSEDreturnDisAfterTakeTask
from KSED.Tests.tk18362 import KSEDsoftDisFromDelegatAfterReject_RD
from KSED.Tests.tk18363 import KSEDsoftDisAfterTakeTask

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_681(web_browser):

    """ Создание КС _ вид РД"""

    page = KSEDCreatDocCS_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()
@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_682(web_browser):

    """ Создание КС _ Вид ЛНД"""

    page = KSEDCreatDocCS_LND(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_683(web_browser):

    """ Создание КС _ вид Прочие"""

    page = KSEDCreatDocCS_ETC(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc  = page.Creat()

    saveLink = page.LinkDocWFile()




@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_684(web_browser):

    """ Добавление сотрудника в этап """

    page = KSEDaddPerson(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    create_route = page.creation_of_the_approval_route()

    # create_route = page.creation_of_the_approval_route()
    #
    # Attach = page.attachment()
    #
    # NaprNaSogl = page.NapSoglasovanie()

    # saveLink = page.LinkDocWFile()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_685(web_browser):

    """ Создание нетипового маршрута """

    page = KSEDCreatWaySogl(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    create_route = page.creation_of_the_approval_route()

    # Attach = page.attachment()

    # NaprNaSogl = page.NapSoglasovanie()

    # saveLink = page.LinkDocWFile()
@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_686(web_browser):

    """ Создание типового маршрута """
    # Шаг 1 создание документа
    page = KSEDCreatWaySogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDCreatWaySogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_687(web_browser):

    """ Направление на согласование """

    # Шаг 1 создание документа
    page = KSEDNaprSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Шаг 2 создание маршрута

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()





@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_688(web_browser):

    """ Добавление новой версии """

    # Шаг 1 создание документа
    page = KSEDaddNewVersion(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDaddNewVersion(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    # Шаг 4 возврат с согласования
    reject = page.rejectYourself()

    # Шаг 5 загрузка новой версии файла
    attach = page.attachment_docReady()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_689(web_browser):

    """ Добавление новой версии """

    # Шаг 1 создание документа
    page = KSEDaddNewAtt(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDaddNewAtt(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    # Шаг 4 возврат с согласования
    reject = page.rejectYourself()

    # Шаг 5 загрузка нового файла
    attach = page.attachment_NewDoc()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_690(web_browser):

    """ Основное согласование """
    # Шаг 1 создание документа
    page = KSEDacceptSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDacceptSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDacceptSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    accept = page2.acceptDoc()



@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_691(web_browser):

    """ Отклонение согласования """
    # Шаг 1 создание документа
    page = KSEDreject_RD(web_browser)

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

    page2 = KSEDreject_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()



@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_692(web_browser):

    """ Внутреннее согласование """
    # Шаг 1 создание документа
    page = KSEDinnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDinnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_693(web_browser):

    """ Возврат с внутреннеего согласования """
    # Шаг 1 создание документа
    page = KSEDrejectInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDrejectInnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 направление на внутреннее согласования

    page2 = KSEDrejectInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    # Шаг 5 отзыв внутреннего согласования

    rejectInnerSogl = page2.rejectInnerSogl()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_694(web_browser):

    """ Отзыв задачи внутренеего согласования """
    # Шаг 1 создание документа
    page = KSEDrejectTaskInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDrejectTaskInnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDrejectTaskInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    rejectTaskInnerSogl = page2.rejectTaskInnerSogl()


@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_695(web_browser):

    """ Повторная отправка на внутрненнее согласование """
    # Шаг 1 создание документа
    page = KSEDrepeatInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Шаг 2 создание маршрута

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDrepeatInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    rejectTaskInnerSogl = page2.rejectTaskInnerSogl()

    repeatInnerApp = page2.repeatInnerSogl()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_696(web_browser):

    """ Внутреннее согласование - вынесение решения"""
    # Шаг 1 создание документа
    page = KSEDAcceptInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDAcceptInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 согласование на внутреннее согласование

    page3 = KSEDAcceptInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('tst_user11', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.AcceptInnerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_697(web_browser):

    """ Основное согласование - внесение замечаний """
    # Шаг 1 создание документа
    page = KSEDaddComment(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDacceptSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDaddComment(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    addComment = page2.addComment()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_700(web_browser):

    """ Забрать задачу согласования"""
    # Шаг 1 создание документа
    page = KSEDtakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDtakeTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 забрать задачу

    page2 = KSEDtakeTask(web_browser)

    LogIn_page = page2.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    take = page2.takeTask_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_701(web_browser):

    """ Возврат задачи согласования """
    # Шаг 1 создание документа
    page = KSEDbackTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDbackTask(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 забрать задачу

    page2 = KSEDbackTask(web_browser)

    LogIn_page = page2.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    take = page2.takeTask_RD()

    # Шаг 5 вернуть задачу

    take = page2.backTask_RD()


@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_702(web_browser):

    """ Отзыв решения """
    # Шаг 1 создание документа
    page = KSEDreturnDecision_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDreturnDecision_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDreturnDecision_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()

    # Шаг 4 отзыв решения

    returnDecision = page2.returnDecision_RD()

@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_703(web_browser):

    """ Смягчение решения """
    # Шаг 1 создание документа
    page = KSEDsoftDecision_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    page = KSEDsoftDecision_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDsoftDecision_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()

    # Шаг 4 отзыв решения

    returnDecision = page2.softDecision_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_704(web_browser):

    """ Внутреннее согласование - отзыв решения после отклонения"""
    # Шаг 1 создание документа
    page = KSEDchangeAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDchangeAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 Отклонение и отзыв решения на внутреннем согласовании

    page3 = KSEDchangeAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user11', 'Changeme!')

    getDoc = page3.getDoc()

    innerSogl = page3.RejectInnerSogl()

    innerSogl = page3.returnDecision_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_705(web_browser):

    """ Внутреннее согласование - смягчение решения после отклонения"""
    # Шаг 1 создание документа
    page = KSEDsoftDesAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDsoftDesAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 Отклонение и отзыв решения на внутреннем согласовании

    page3 = KSEDsoftDesAfterRejectInnerSogl_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user11', 'Changeme!')

    getDoc = page3.getDoc()

    innerSogl = page3.RejectInnerSogl()

    innerSogl = page3.softDecision_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_706(web_browser):

    """ Внутреннее согласование - отзыв решения после согласования"""
    # Шаг 1 создание документа
    page = KSEDchangeAfterAcceptInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDchangeAfterAcceptInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 Отклонение и отзыв решения на внутреннем согласовании

    page3 = KSEDchangeAfterAcceptInnerSogl_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user11', 'Changeme!')

    getDoc = page3.getDoc()

    innerSogl = page3.AcceptInnerSogl()

    innerSogl = page3.returnDecision_RD()


@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_707(web_browser):

    """ Внутреннее согласование - отзыв решения после согласования с замечаниями"""
    # Шаг 1 создание документа
    page = KSEDchangeAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDchangeAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 Отклонение и отзыв решения на внутреннем согласовании

    page3 = KSEDchangeAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user11', 'Changeme!')

    getDoc = page3.getDoc()

    innerSogl = page3.AcceptInnerSogl()

    innerSogl = page3.returnDecision_RD()



@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_708(web_browser):

    """ Внутреннее согласование - смягчение решения после согласования с замечаниями"""
    # Шаг 1 создание документа
    page = KSEDsoftDisAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDsoftDisAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 Отклонение и отзыв решения на внутреннем согласовании

    page3 = KSEDsoftDisAfterAcceptWithRemarkInnerSogl_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user11', 'Changeme!')

    getDoc = page3.getDoc()

    innerSogl = page3.AcceptInnerSogl()

    innerSogl = page3.softDecision_RD()


@pytest.mark.KSED_smoke_test
@pytest.fixture(scope="session")
def test_709(web_browser):

    """ Внутреннее согласование - добавление комментариев"""
    # Шаг 1 создание документа
    page = KSEDaddCommentInnerSogl_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDaddCommentInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 согласование на внутреннее согласование

    page3 = KSEDaddCommentInnerSogl_RD(web_browser)

    LogIn_page = page2.LogIN('tst_user11', 'Changeme!')

    getDoc = page2.getDoc()

    addComment = page2.addComment()



@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_710(web_browser):

    """ Внутреннее согласование после удаления добавленого комментария"""
    # Шаг 1 создание документа
    page = KSEDInnerSoglAfterAddComment_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    #Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    #page = KSEDinnerSogl_RD(web_browser)

    #LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    #getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 на правление на внутреннее согласование

    page2 = KSEDInnerSoglAfterAddComment_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    innerSogl = page2.innerSogl()

    Logout = page2.USER_LOGOUTs()  # Выход из системы

    # Шаг 5 согласование на внутреннее согласование

    page3 = KSEDInnerSoglAfterAddComment_RD(web_browser)

    LogIn_page = page2.LogIN('tst_user11', 'Changeme!')

    getDoc = page2.getDoc()

    addComment = page2.addComment()

    accept = page2.AcceptInnerSoglWithComment()

    accept2 = page2.AcceptInnerSogl()


@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_711(web_browser):

    """ Основное согласование c комментариями """
    # Шаг 1 создание документа
    page = KSEDacceptSoglwithRemark_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    # page = KSEDacceptSoglwithRemark_RD(web_browser)

    # LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    # getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDacceptSoglwithRemark_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    accept = page2.acceptDoc()



@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_712(web_browser):

    """ Основное согласование c комментариями и отзыв решения"""
    # Шаг 1 создание документа
    page = KSEDrejectAfterAcceptSoglwithRemark_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    # page = KSEDacceptSoglwithRemark_RD(web_browser)

    # LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    # getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDrejectAfterAcceptSoglwithRemark_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    accept = page2.acceptDoc()

    returnDis = page2.returnDecision_RD()



@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_713(web_browser):

    """ Основное согласование c комментариями и смягчение решения"""
    # Шаг 1 создание документа
    page = KSEDsoftDisAfterAcceptSoglwithRemark_RD(web_browser)

    LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    Creat_doc = page.Creat()

    saveLink = page.LinkDocWFile()

    # Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 2 создание маршрута
    # page = KSEDacceptSoglwithRemark_RD(web_browser)

    # LogIn_page = page.LogIN('StroganovSN', 'Changeme!')

    # getDoc = page.getDoc()

    create_route = page.creation_of_the_approval_route()

    # Шаг 3 вложение и направление на созгаласование

    attach = page.attachment()

    NapSoglasovanie = page.NapSoglasovanie()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    # Шаг 4 отклонение созгаласования

    page2 = KSEDsoftDisAfterAcceptSoglwithRemark_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    accept = page2.acceptDoc()

    softDis = page2.softDecision_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_714(web_browser):

    """  Отзыв решения делегата после отклонения согласования основного согласующего"""
    # Шаг 1 создание документа
    page = KSEDreturnDisFromDelegatAfterReject_RD(web_browser)

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

    page2 = KSEDreturnDisFromDelegatAfterReject_RD(web_browser)

    LogIn_page = page2.LogIN('YatskinRS', 'Changeme!')

    getDoc = page2.getDoc()

    reject = page2.rejectDoc()

    Logout = page.USER_LOGOUTs()  # Выход из системы

    page3 = KSEDreturnDisFromDelegatAfterReject_RD(web_browser)

    LogIn_page = page3.LogIN('tst_user1', 'Changeme!')

    getDoc = page2.getDoc()

    returnDis = page3.returnDecision_RD()

@pytest.mark.KSED_smoke_test
#@pytest.fixture(scope="session")
def test_715(web_browser):

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
def test_716(web_browser):
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
def test_717(web_browser):
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
