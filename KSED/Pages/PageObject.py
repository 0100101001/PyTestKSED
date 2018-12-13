from page_objects import PageObject, PageElement
from TestData.locators import KSEDLocators



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

    # *******МЕНЮ ПОЛЬЗОВАТЕЛЯ*******
    user_menu = PageElement(id_=KSEDLocators.user_menu) # Меню пользователя
    USER_LOGOUT = PageElement(id_=KSEDLocators.USER_LOGOUT) # Выход из системы

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

    # ОБЛАСТЬ ПРОСМОТРА (КСЭД)

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
    attachments = PageElement(xpath=KSEDLocators.attachments) # Вложения (раскрытие раздела)
    osnSvedeniya = PageElement(xpath=KSEDLocators.osnSvedeniya) # Основные сведения (раскрытие раздела)
    mode = PageElement(xpath=KSEDLocators.mode) # Переключение в двупанельный вид
    fileUpload = PageElement(xpath=KSEDLocators.fileUpload) # Загрузить файл
    files = PageElement(xpath=KSEDLocators.files) # Выберите файлы
    show = PageElement(xpath=KSEDLocators.show) # Показать общую карточка
    punkti = PageElement(xpath=KSEDLocators.punkti) # Вкладка "Пункты"
    punktiBtn = PageElement(xpath=KSEDLocators.punktiBtn) # Кнопка "Пункты"
    punktPoruch = PageElement(xpath=KSEDLocators.punktPoruch) # Пункт/Поручение
    textPoruch = PageElement(xpath=KSEDLocators.textPoruch) # Текст поручения
    tipPoruch = PageElement(xpath=KSEDLocators.tipPoruch) # Тип поручения
    otvetstv_ispolnVpunktah = PageElement(xpath=KSEDLocators.otvetstv_ispolnVpunktah) # Ответственный исполнитель в пунктах карточки документа
    srokIspoln = PageElement(xpath=KSEDLocators.srokIspoln) # Срок исполнения (среднее знач)

    btnOKform = PageElement(xpath=KSEDLocators.btnOKform) # Кнопка ОК на форме

    sendFor_approval = PageElement(xpath=KSEDLocators.sendFor_approval) # Действие "Направить на согласование"

    status_Doc = PageElement(xpath=KSEDLocators.status_Doc) # Статус документа во вкладке (Основные сведения)

    # (панель согласования)
    APPROVED_button = PageElement(xpath=KSEDLocators.APPROVED_button) # Кнопка "Согласовать"
    APPROVED_WITH_REMARK_button = PageElement(xpath=KSEDLocators.APPROVED_WITH_REMARK_button) # Кнопка "Согласовать с комментариями"
    REJECTED_button = PageElement(xpath=KSEDLocators.REJECTED_button) # Кнопка "Отклонить"
    internal_approval = PageElement(xpath=KSEDLocators.internal_approval) # Кнопка "Внутреннее согласование"
    prop_bpm_comment = PageElement(name=KSEDLocators.prop_bpm_comment) # Поле комментария
    apply_button_button = PageElement(xpath=KSEDLocators.apply_button_button) # Кнопка "ОК" при вынесении решения согласования

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
    normokontrol = PageElement(xpath=KSEDLocators.normokontrol) # Нормоконтроль
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



























