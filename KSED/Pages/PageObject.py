from page_objects import PageObject, PageElement
from KSED.TestData.locators import KSEDLocators



class Locator(PageObject, KSEDLocators):


    # Форма авторизации
    username_text = PageElement(name=KSEDLocators.username_text) # Логин
    password_text = PageElement(name=KSEDLocators.password_text) # Пароль
    LogIn_button = PageElement(xpath=KSEDLocators.LogIn_button) # Кнопка "Войти"


    # *******СТРОКА МЕНЮ*******
    ksed = PageElement(xpath=KSEDLocators.ksed) #xpath  # КСЭД

    barcode_search = PageElement(id_=KSEDLocators.barcode_search) #id  # Поиск по ШК
    search_bc = PageElement(xpath=KSEDLocators.search_bc) # Строка поиска по ШК

    more_menu = PageElement(id_=KSEDLocators.more_menu)# Меню "Ещё"
    ksed_in_more_m = PageElement(id_=KSEDLocators.ksed_in_more_m) # КСЭД в меню "Ещё"
    Company_dir = PageElement(xpath=KSEDLocators.Company_dir)  # Справочник организации
    admin = PageElement(xpath=KSEDLocators.admin) # Администрирование
    transfer = PageElement(xpath=KSEDLocators.transfer) # Передача дел
    arm_arh = PageElement(xpath=KSEDLocators.arm_arh) # АРМ Архивное дело
    verify = PageElement(xpath=KSEDLocators.verify) # Верификация
    scanner = PageElement(xpath=KSEDLocators.scanner) # Работа со сканером ШК

    notification = PageElement(id_=KSEDLocators.notification) # Уведомления
    notificationProtokol = PageElement(xpath=KSEDLocators.notificationProtokol) # Первое в списке уведомление о протоколе
    notificationFirst = PageElement(xpath=KSEDLocators.notificationFirst)  # id  # Уведомление первое в списке
    # *******МЕНЮ ПОЛЬЗОВАТЕЛЯ*******
    user_menu = PageElement(id_=KSEDLocators.user_menu) # Меню пользователя
    USER_LOGOUT = PageElement(id_=KSEDLocators.USER_LOGOUT) # Выход из системы

    my_profile = PageElement(xpath=KSEDLocators.my_profile) # Пункт меню "Мой профиль"
    fieldlabel = PageElement(xpath=KSEDLocators.fieldlabel) # Должность в области краткой информации
    btnEdit_profile = PageElement(xpath=KSEDLocators.btnEdit_profile) # Кнопка "Изменить профиль"
    inputPosition = PageElement(xpath=KSEDLocators.inputPosition) # Поле ввода должности

    logic_ESM = PageElement(xpath=KSEDLocators.logic_ESM) # Пункт меню "Логика ECM. Мой профиль"
    autoAnswerText = PageElement(name=KSEDLocators.autoAnswerText) # Текст автоответа (Меня нет в офисе)
    btnCancelAbsence = PageElement(xpath=KSEDLocators.btnCancelAbsence) # Кнопка "Отменить отсутствие"
    btnYes = PageElement(xpath=KSEDLocators.btnYes) # Кнопка "Да" (отменить отсутствие)

    edit_password = PageElement(xpath=KSEDLocators.edit_password) # Пункт меню "Изменить пароль"
    inputOldPassword = PageElement(xpath=KSEDLocators.inputOldPassword) # Введите старый пароль
    inputNewPassword1 = PageElement(xpath=KSEDLocators.inputNewPassword1) # Введите старый пароль
    inputNewPassword2 = PageElement(xpath=KSEDLocators.inputNewPassword2) # Введите старый пароль
    btnOKchange = PageElement(xpath=KSEDLocators.btnOKchange) # Кнопка "Изменить пароль"

    # *******ЛЕВАЯ ЧАСТЬ СТРАНИЦЫ (Кнопка "Создать" и разделы)*******
    newDoc_button = PageElement(xpath=KSEDLocators.newDoc_button) # "Создать"

    protocol = PageElement(xpath=KSEDLocators.protocol) # Протокол
    rd = PageElement(xpath=KSEDLocators.rd) # РД
    reestr = PageElement(xpath=KSEDLocators.reestr) # Реестр
    poruchenie = PageElement(xpath=KSEDLocators.poruchenie) # Поручение
    resolution = PageElement(xpath=KSEDLocators.resolution) # Резолюция
    SZ = PageElement(xpath=KSEDLocators.SZ) # Служебная записка
    proizvDoc = PageElement(xpath=KSEDLocators.proizvDoc) # Произвольный документ
    paket_vh = PageElement(xpath=KSEDLocators.paket_vh) #Пакет Вх. кор.
    vhDoc = PageElement(xpath=KSEDLocators.vhDoc) # Входящий документ
    ishDoc = PageElement(xpath=KSEDLocators.ishDoc) # Исходящий документ

    # РАЗДЕЛЫ
    myWork = PageElement(xpath=KSEDLocators.myWork) # Моя работа

    expedition = PageElement(xpath=KSEDLocators.expedition) # Экспедиция

    navigation = PageElement(xpath=KSEDLocators.navigation) # Навигатор

    allur = PageElement(xpath=KSEDLocators.allur) # Отчеты

    workReg = PageElement(xpath=KSEDLocators.workReg) # Работа регистратора

    medo = PageElement(xpath=KSEDLocators.medo) # МЭДО

    mySearch = PageElement(xpath=KSEDLocators.mySearch) # Мои поисковые запросы
    poiskzapr = PageElement(xpath=KSEDLocators.poiskzapr) # Поисковые запросы
    myPoiskZapr = PageElement(xpath=KSEDLocators.myPoiskZapr) # Поисковые запросы
    ControlZapr = PageElement(xpath=KSEDLocators.ControlZapr) # Упарвление поисковыми запросами
    # ОБЛАСТЬ ПРОСМОТРА (КСЭД)
    oblProsm = PageElement(xpath=KSEDLocators.oblProsm) # Область просмотра
    oneDocInList = PageElement(xpath=KSEDLocators.oneDocInList) # Первый документ в списке

    # ОТЧЕТЫ
    section_allur = PageElement(xpath=KSEDLocators.section_allur) # Раздел "Отчеты"
    node_Logs = PageElement(xpath=KSEDLocators.node_Logs)  # "Журналы"
    node_Statis = PageElement(xpath=KSEDLocators.node_Statis) # "Статистические отчеты"
    node_ispDisp = PageElement(xpath=KSEDLocators.node_ispDisp) #

    logs_incDoc = PageElement(xpath=KSEDLocators.logs_incDoc)
    logs_outDoc = PageElement(xpath=KSEDLocators.logs_outDoc)
    logs_raspDoc = PageElement(xpath=KSEDLocators.logs_raspDoc)
    logs_sluDoc = PageElement(xpath=KSEDLocators.logs_sluDoc)

    stat_specDoc = PageElement(xpath=KSEDLocators.stat_specDoc)
    stat_temDoc = PageElement(xpath=KSEDLocators.stat_temDoc)
    stat_temDocO = PageElement(xpath=KSEDLocators.stat_temDocO)
    stat_tipDoc = PageElement(xpath=KSEDLocators.stat_tipDoc)

    allu_ispIncDoc = PageElement(xpath=KSEDLocators.allu_ispIncDoc)
    allu_raspDoc = PageElement(xpath=KSEDLocators.allu_raspDoc)
    allu_sluDoc = PageElement(xpath=KSEDLocators.allu_sluDoc)
    allu_ispDis = PageElement(xpath=KSEDLocators.allu_ispDis)
    allu_ispDispA = PageElement(xpath=KSEDLocators.allu_ispDispA)
    allu_NispDI = PageElement(xpath=KSEDLocators.allu_NispDI)
    allu_NispDIrg = PageElement(xpath=KSEDLocators.allu_NispDIrg)
    allu_istS = PageElement(xpath=KSEDLocators.allu_istS)
    allu_narS = PageElement(xpath=KSEDLocators.allu_narS)
    allu_prodIsp = PageElement(xpath=KSEDLocators.allu_prodIsp)
    allu_prodPodr = PageElement(xpath=KSEDLocators.allu_prodPodr)
    allu_ReesContr = PageElement(xpath=KSEDLocators.allu_ReesContr)
    allu_ReesContrN = PageElement(xpath=KSEDLocators.allu_ReesContrN)
    allu_ReesContrF = PageElement(xpath=KSEDLocators.allu_ReesContrF)
    allu_SostIspR = PageElement(xpath=KSEDLocators.allu_SostIspR)


    # *******РАБОТА С ДОКУМЕНТАМИ*******

    # ОБЩИЕ АТРИБУТЫ
    #(форма создания документа)
    title = PageElement(name=KSEDLocators.title)  # Заголовок

    category_doc = PageElement(xpath=KSEDLocators.category_doc) # Категория документа

    doc_type = PageElement(xpath=KSEDLocators.doc_type) # Вид документа(кнопка выбора)
    doc_typeInp = PageElement(xpath=KSEDLocators.doc_typeInp) # Вид документа(поле ввода)
    btnOKDT = PageElement(xpath=KSEDLocators.btnOKDT) # Вид документа (кнопка "ОК")

    podpisant = PageElement(xpath=KSEDLocators.podpisant) # Подписант(ы)

    sposob_dost = PageElement(xpath=KSEDLocators.sposob_dost) # Способ доставки

    btnCreateDoc = PageElement(xpath=KSEDLocators.btnCreateDoc) # Кнопка "Создать"

    adresat = PageElement(xpath=KSEDLocators.adresat) # Адресат

    korrespondent = PageElement(xpath=KSEDLocators.korrespondent)  # Корреспондент

    # (карточка документа)
    attachments = PageElement(xpath=KSEDLocators.attachments) # # Переход во вкладку "Вложения"
    vlozheniya = PageElement(xpath=KSEDLocators.vlozheniya) # Вложения (раскрытие раздела)
    osnSvedeniya = PageElement(xpath=KSEDLocators.osnSvedeniya) # Основные сведения (раскрытие раздела)
    printForm = PageElement(xpath=KSEDLocators.printForm)# Печатные формы (раскрытие раздела)
    printBarCode = PageElement(xpath=KSEDLocators.printBarCode) #Печатная форма штрих кода документа
    btnPrintInPrintForm = PageElement(id_=KSEDLocators.btnPrintInPrintForm)# Кнопка печати в окне печатной формы

    mode = PageElement(xpath=KSEDLocators.mode) # Переключение в двупанельный вид
    fileUpload = PageElement(xpath=KSEDLocators.fileUpload) # Загрузить файл
    fileUpload2 = PageElement(xpath=KSEDLocators.fileUpload2)  # Загрузить файл в поручении
    files = PageElement(xpath=KSEDLocators.files) # Выберите файлы
    show = PageElement(xpath=KSEDLocators.show) # Показать общую карточка
    show_list = PageElement(xpath=KSEDLocators.show_list)# Показать ввиде списка
    btnPrint = PageElement(xpath=KSEDLocators.btnPrint) # Кнопка печати в форме предварительного просмотра вложения

    soglasovanieWkladka = PageElement(xpath=KSEDLocators.soglasovanieWkladka) # Вкладка "Согласование"
    createRuleBtn = PageElement(xpath=KSEDLocators.createRuleBtn) # Кнопка "Создать маршрут"
    createRuleIndivid = PageElement(xpath=KSEDLocators.createRuleIndivid) # "Индивидуальный маршрут"
    addEtap = PageElement(xpath=KSEDLocators.addEtap) # Кнопка "Добавить этап"
    tipeEtap = PageElement(xpath=KSEDLocators.tipeEtap) # "Вид этапа"
    soglasuychie = PageElement(xpath=KSEDLocators.soglasuychie) # "Согласующие"
    btnOKformSogl = PageElement(xpath=KSEDLocators.btnOKformSogl) # Кнопка "ОК" на форме добавления этапа согласования

    punkti = PageElement(xpath=KSEDLocators.punkti) # Вкладка "Пункты"
    punktiBtn = PageElement(xpath=KSEDLocators.punktiBtn) # Кнопка "Пункты"
    punktPoruch = PageElement(xpath=KSEDLocators.punktPoruch) # Пункт/Поручение
    textPoruch = PageElement(xpath=KSEDLocators.textPoruch) # Текст поручения
    tipPoruch = PageElement(xpath=KSEDLocators.tipPoruch) # Тип поручения
    otvetstv_ispolnVpunktah = PageElement(xpath=KSEDLocators.otvetstv_ispolnVpunktah) # Ответственный исполнитель в пунктах карточки документа
    srokIspoln = PageElement(xpath=KSEDLocators.srokIspoln) # Срок исполнения (среднее знач)

    btnOKform = PageElement(xpath=KSEDLocators.btnOKform) # Кнопка ОК на форме

    sendFor_approval = PageElement(xpath=KSEDLocators.sendFor_approval) # Действие "Направить на согласование"
    sendFor_execution = PageElement(xpath=KSEDLocators.sendFor_execution) # Действие "Направить на исполнение"
    btnOKnaprNaIspoln = PageElement(xpath=KSEDLocators.btnOKnaprNaIspoln) # Кнопка "ОК" на форме подтверждения действия "Направить на исполнение"
    confirm = PageElement(xpath=KSEDLocators.confirm) # Подтверждение согласования

    status_Doc = PageElement(xpath=KSEDLocators.status_Doc) # Статус документа во вкладке (Основные сведения)

    #"Отправить отчет"
    actionSendAllere = PageElement(xpath=KSEDLocators.actionSendAllere) # "Отправить отчет" действие
    btnSend = PageElement(xpath=KSEDLocators.btnSend) # Кнопка "Отправить"
    textAllur = PageElement(xpath=KSEDLocators.textAllur) # Текстовое поле "Текст отчета"
    btnAddSvyz = PageElement(xpath=KSEDLocators.btnAddSvyz) # Кнопка добавления связи "..."
    searchDoc = PageElement(xpath=KSEDLocators.searchDoc) # Строка поиска в форме подбора
    oneListEl = PageElement(xpath=KSEDLocators.oneListEl) # Первый элемент в списке справочника
    btnOK = PageElement(xpath=KSEDLocators.btnOK) # Кнопка "ОК" в форме подбора

    # (панель согласования)
    APPROVED_button = PageElement(xpath=KSEDLocators.APPROVED_button) # Кнопка "Согласовать"
    APPROVED_WITH_REMARK_button = PageElement(xpath=KSEDLocators.APPROVED_WITH_REMARK_button) # Кнопка "Согласовать с комментариями"
    REJECTED_button = PageElement(xpath=KSEDLocators.REJECTED_button) # Кнопка "Отклонить"
    internal_approval = PageElement(xpath=KSEDLocators.internal_approval) # Кнопка "Внутреннее согласование"
    prop_bpm_comment = PageElement(name=KSEDLocators.prop_bpm_comment) # Поле комментария
    apply_button_button = PageElement(xpath=KSEDLocators.apply_button_button) # Кнопка "ОК" при вынесении решения согласования

    SIGNED_button = PageElement(xpath=KSEDLocators.SIGNED_button) # Кнопка "Подписать"

    # # ПРОТОКОЛ
    # #(форма создания документа)
    # addEl = PageElement(xpath=KSEDLocators.addEl) # Вид документа(Протокол совещания рабочей группы)
    # addEl2 = PageElement(xpath=KSEDLocators.addEl2) #Вид документа "Служебная записка"

    # РАСПОРЯДИТЕЛЬНЫЙ ДОКУМЕНТ
    #(форма создания документа)
    addEl = PageElement(xpath=KSEDLocators.addEl) # Вид документа(Протокол совещания рабочей группы)
    addEl2 = PageElement(xpath=KSEDLocators.addEl2) #Вид документа "Служебная записка"
    preambula = PageElement(xpath=KSEDLocators.preambula) # Преамбула
    obcontrol = PageElement(xpath=KSEDLocators.obcontrol) # Общий контроль
    wid_doc = PageElement(xpath=KSEDLocators.wid_doc) # Вид документа (в РД)
    wid_doc_rasp = PageElement(xpath=KSEDLocators.wid_doc_rasp) # Вид документа РД (Распоряжение)

    addPunkt = PageElement(xpath=KSEDLocators.addPunkt) # Кнопка "Добавить пункт"
    textPunktaRD = PageElement(name=KSEDLocators.textPunktaRD) # Текст пункта РД
    otvetstv_ispolnVpunktahRD = PageElement(xpath=KSEDLocators.otvetstv_ispolnVpunktahRD) # Ответственный исполнитель в пункте РД
    rassilka = PageElement(xpath=KSEDLocators.rassilka) # Вкладка "Рассылка"
    btnVipolnit = PageElement(xpath=KSEDLocators.btnVipolnit) # Кнопка "Выполнить..."
    punktBtnVipolnit = PageElement(xpath=KSEDLocators.punktBtnVipolnit) # Создать и заполнить


    # ПРОТОКОЛ
    #(форма создания документа)
    date = PageElement(xpath=KSEDLocators.date) # Дата совещания
    category = PageElement(xpath=KSEDLocators.category) # Категория
    Chairman = PageElement(xpath=KSEDLocators.Chairman) # Председатель
    Secretary = PageElement(xpath=KSEDLocators.Secretary) # Секретарь
    person_present = PageElement(xpath=KSEDLocators.person_present) # Присутствовали


    #РЕЕСТР
    #(форма создания документа)
    vid_reestra = PageElement(xpath=KSEDLocators.vid_reestra) # Вид реестра
    vid_reestraPR = PageElement(xpath=KSEDLocators.vid_reestraPR) # Вид реестра (Передачи на рег..)
    vid_reestraPP = PageElement(xpath=KSEDLocators.vid_reestraPP) # Вид реестра (Приема/передачи)
    btnCreateChern = PageElement(xpath=KSEDLocators.btnCreateChern)  # Кнопка "Создать черновик"
    btnCreateSend = PageElement(xpath=KSEDLocators.btnCreateSend) # Кнопка "Создать и отправить"
    inpDoc = PageElement(xpath=KSEDLocators.inpDoc) # Поле "Документы"
    poluchatel = PageElement(xpath=KSEDLocators.poluchatel) # Поле "Получатель"

    # СЛУЖЕБНАЯ ЗАПИСКА
    #(форма создания документа)
    adresati = PageElement(xpath=KSEDLocators.adresati) # Адресаты

    # ПРОИЗВОЛЬНЫЙ ДОКУМЕНТ
    #(форма создания документа)
    prorabotka = PageElement(xpath=KSEDLocators.prorabotka) # Проработка
    chBprorab = PageElement(xpath=KSEDLocators.chBprorab) # чекбокс проработка
    normokontrol = PageElement(xpath=KSEDLocators.normokontrol) # Нормоконтроль
    chBnorm = PageElement(xpath=KSEDLocators.chBnorm) # чекбокс Проработка
    soglasovanie = PageElement(xpath=KSEDLocators.soglasovanie) # Согласование
    podpisanie = PageElement(xpath=KSEDLocators.podpisanie) # Подписание
    utverzhdenie = PageElement(xpath=KSEDLocators.utverzhdenie) # Утверждение
    oznakomlenie = PageElement(xpath=KSEDLocators.oznakomlenie) # Ознакомление

    # ПОРУЧЕНИЕ
    # (форма создания документа)
    tipPoruch = PageElement(xpath=KSEDLocators.tipPoruch) # Тип поручения
    text_poruch = PageElement(name=KSEDLocators.text_poruch) #Текст поручения
    otvetstv_ispoln = PageElement(xpath=KSEDLocators.otvetstv_ispoln) # Ответственный исполнитель

    # ПАКЕТ ВХОДЯЩЕЙ КОРРЕСПОНДЕНЦИИ

    # ВХОДЯЩИЙ ДОКУМЕНТ
    #(форма создания документа)
    ishNumber = PageElement(name=KSEDLocators.ishNumber) # Исходящий номер
    dateIS = PageElement(xpath=KSEDLocators.dateIS) # Дата исходящего

    # ИСХОДЯЩИЙ ДОКУМЕНТ
    # (форма создания документа)
    osnovPodpis = PageElement(name=KSEDLocators.osnovPodpis) # Основание подписания
    korrespondentISH = PageElement(xpath=KSEDLocators.korrespondentISH) # Корреспондент


    clickNull = PageElement(xpath=KSEDLocators.clickNull) # КЛИК ВНЕ АТРИБУТОВ


    #Формы отчетов

    #Мои поисковые запросы
    listChange = PageElement(xpath=KSEDLocators.listChange)  # Выпадающий список
    listChangeSZ = PageElement(xpath=KSEDLocators.listChangeSZ)  # Выпадающий список - служебная записка
    listChangeRD = PageElement(xpath=KSEDLocators.listChangeRD)  # Выпадающий список - РД
    butSave = PageElement(xpath=KSEDLocators.butSave) #Кнопка сохранить
    nameZap = PageElement(xpath=KSEDLocators.nameZap) #Наименование запроса
    zaprosToDel = PageElement(xpath=KSEDLocators.zaprosToDel)#созданный запрос
    butDel = PageElement(xpath=KSEDLocators.butDel) #Кнопка удалить
    butRed = PageElement(xpath=KSEDLocators.butRed)  # Кнопка редактировать
    butDelAc = PageElement(xpath=KSEDLocators.butDelAc)  # Кнопка удалить подтверждение
    butAct = PageElement(xpath=KSEDLocators.butAct) # Кнопка "Действия с выбранными"
    checkBoxFirst = PageElement(xpath=KSEDLocators.checkBoxFirst)  # Первый чекбокс в списке
    butFavorite = PageElement(xpath=KSEDLocators.butFavorite)  # Кнопка добавить в избранное
    butOK = PageElement(xpath=KSEDLocators.butOK) #Кнопка OK добавить в избранное




















