from page_objects import PageObject, PageElement
from TestData.locators import KSEDLocators



class Locator(PageObject, KSEDLocators):

    # ПРЕДУСЛОВИЕ
    baseURL = 'http://213.128.208.34/share/page/arm?code=SED'

    BARCODE = '171267'
    # ---------------------------------------------

    # Форма авторизации
    username_text = PageElement(name=KSEDLocators.username_text)
    password_text = PageElement(name=KSEDLocators.password_text)
    LogIn_button = PageElement(xpath=KSEDLocators.LogIn_button)


    # Строка меню
    ksed            = PageElement(xpath=KSEDLocators.ksed) # КСЭД

    barcode_search  = PageElement(id_=KSEDLocators.barcode_search) # Поиск по ШК
    search_bc       = PageElement(xpath=KSEDLocators.search_bc) # Строка поиска по ШК

    more_menu       = PageElement(id_=KSEDLocators.more_menu) # Меню "Ещё"
    ksed_in_more_m  = PageElement(id_=KSEDLocators.ksed_in_more_m) # КСЭД в меню "Ещё"
    Company_dir     = PageElement(xpath=KSEDLocators.Company_dir) # Справочник организации
    admin           = PageElement(xpath=KSEDLocators.admin) # Администрирование
    transfer        = PageElement(xpath=KSEDLocators.transfer) # Передача дел
    arm_arh         = PageElement(xpath=KSEDLocators.arm_arh) # АРМ Архивное дело
    verify          = PageElement(xpath=KSEDLocators.verify) # Верификация
    scanner         = PageElement(xpath=KSEDLocators.scanner) # Работа со сканером ШК

    notification    = PageElement(id_=KSEDLocators.notification) # Уведомления

    # Меню пользователя
    user_menu       = PageElement(id_=KSEDLocators.user_menu) # Меню пользователя

    # Левая часть страницы (Кнопка "Создать" и разделы)
    newDoc_button   = PageElement(xpath=KSEDLocators.newDoc_button) # "Создать"

    protocol        = PageElement(xpath=KSEDLocators.protocol) # Протокол
    rd              = PageElement(xpath=KSEDLocators.rd) # РД
    reestr          = PageElement(xpath=KSEDLocators.reestr) # Реестр
    poruchenie      = PageElement(xpath=KSEDLocators.poruchenie) # Поручение
    resolution      = PageElement(xpath=KSEDLocators.resolution)  # Резолюция
    SZ              = PageElement(xpath=KSEDLocators.SZ)  # Служебная записка




    # Форма создания документа
    doc_type        = PageElement(xpath=KSEDLocators.doc_type) #Вид документа(кнопка выбора)
    addEl           = PageElement(xpath=KSEDLocators.addEl) # Вид документа(Протокол совещания рабочей группы)
    btnOKDT         = PageElement(xpath=KSEDLocators.btnOKDT) # Вид документа (ОК)
    title           = PageElement(name=KSEDLocators.title) # Заголовок *****
    preambula       = PageElement(xpath=KSEDLocators.preambula) # Преамбула
    podpisant       = PageElement(xpath=KSEDLocators.podpisant) # Подписант
    obcontrol       = PageElement(xpath=KSEDLocators.obcontrol)  # Общий контроль
    wid_doc         = PageElement(xpath=KSEDLocators.wid_doc)# Вид документа в РД
    wid_doc_rasp    = PageElement(xpath=KSEDLocators.wid_doc_rasp) # Вид документа РД (Распоряжение)
    date            = PageElement(xpath=KSEDLocators.date) # Дата совещания
    category        = PageElement(xpath=KSEDLocators.category) # Категория
    Chairman        = PageElement(xpath=KSEDLocators.Chairman) # Председатель
    Secretary       = PageElement(xpath=KSEDLocators.Secretary) # Секретарь
    person_present  = PageElement(xpath=KSEDLocators.person_present) #Присутствовали
    category_doc    = PageElement(xpath=KSEDLocators.category_doc) # Категория документа *****
    btnCreateDoc    = PageElement(xpath=KSEDLocators.btnCreateDoc) # Кнопка "Создать"
    vid_reestra     = PageElement(xpath=KSEDLocators.vid_reestra) # Вид реестра
    vid_reestraPR   = PageElement(xpath=KSEDLocators.vid_reestraPR) # Вид реестра (Передачи на рег..)
    vid_reestraPP   = PageElement(xpath=KSEDLocators.vid_reestraPP) # Вид реестра (Приема/передачи)
    btnCreateChern  = PageElement(xpath=KSEDLocators.btnCreateChern) # Кнопка "Создать черновик"
    btnCreateSend   = PageElement(xpath=KSEDLocators.btnCreateSend)  # Кнопка "Создать и отправить"
    inpDoc          = PageElement(xpath=KSEDLocators.inpDoc) # Поле "Документы"
    poluchatel      = PageElement(xpath=KSEDLocators.poluchatel) # Поле "Получатель"


    myWork          = PageElement(xpath=KSEDLocators.myWork)           # Моя работа
    expedition      = PageElement(xpath=KSEDLocators.expedition)           # Экспедиция
    navigation      = PageElement(xpath=KSEDLocators.navigation)            # Навигатор
    allur           = PageElement(xpath=KSEDLocators.allur)               # Отчеты
    workReg         = PageElement(xpath=KSEDLocators.workReg)  # Работа регистратора
    medo            = PageElement(xpath=KSEDLocators.medo)                 # МЭДО
    mySearch        = PageElement(xpath=KSEDLocators.mySearch)# Мои поисковые запросы

    # Область просмотра


    #Отчеты
    section_allur   = PageElement(xpath=KSEDLocators.section_allur) # Раздел "Отчеты"
    node_Logs       = PageElement(xpath=KSEDLocators.node_Logs)              # "Журналы"
    node_Statis     = PageElement(xpath=KSEDLocators.node_Statis) # "Статистические отчеты"
    node_ispDisp    = PageElement(xpath=KSEDLocators.node_ispDisp) # Отчеты по исполнительской дисциплине

    logs_incDoc     = PageElement(xpath=KSEDLocators.logs_incDoc) # Журнал регистрации входящих документов
    logs_outDoc     = PageElement(xpath=KSEDLocators.logs_outDoc) # Журнал регистрации исходящих документов
    logs_raspDoc    = PageElement(xpath=KSEDLocators.logs_raspDoc) # Журнал регистрации Распорядительных документов
    logs_sluDoc     = PageElement(xpath=KSEDLocators.logs_sluDoc) # Журнал Регистрации служебных записок

    stat_specDoc    = PageElement(xpath=KSEDLocators.stat_specDoc) # Сводка по видам документов
    stat_temDoc     = PageElement(xpath=KSEDLocators.stat_temDoc) # Сводка по тематикам документов
    stat_temDocO    = PageElement(xpath=KSEDLocators.stat_temDocO) # Сводка по тематикам документов (объедин.)
    stat_tipDoc     = PageElement(xpath=KSEDLocators.stat_tipDoc) # Сводка по типам документов

    allu_ispIncDoc  = PageElement(xpath=KSEDLocators.allu_ispIncDoc) #Исполнение входящих документов
    allu_raspDoc    = PageElement(xpath=KSEDLocators.allu_raspDoc) #Исполнение распорядительного документа
    allu_sluDoc     = PageElement(xpath=KSEDLocators.allu_sluDoc) # Исполнение служебных записок
    allu_ispDis     = PageElement(xpath=KSEDLocators.allu_ispDis) # Исполнительская дисциплина по авторам
    allu_ispDispA   = PageElement(xpath=KSEDLocators.allu_ispDispA) # Исполнительская дисциплина по исполнителям
    allu_NispDI     = PageElement(xpath=KSEDLocators.allu_NispDI) # Неисполнительные поручения с истекшим сроком
    allu_NispDIrg   = PageElement(xpath=KSEDLocators.allu_NispDIrg) # Неисполнительные поручения с истекшим сроком РГ
    allu_istS       = PageElement(xpath=KSEDLocators.allu_istS) # Поручения с истекающим сроком
    allu_narS       = PageElement(xpath=KSEDLocators.allu_narS) # Поручения, исполненные с нарушением срока
    allu_prodIsp    = PageElement(xpath=KSEDLocators.allu_prodIsp) # Продуктивность по Исполнителям
    allu_prodPodr   = PageElement(xpath=KSEDLocators.allu_prodPodr) # Продуктивность по Подразделениям
    allu_ReesContr  = PageElement(xpath=KSEDLocators.allu_ReesContr) # Реестр для закрытия неактуальных контрольных поручений
    allu_ReesContrN = PageElement(xpath=KSEDLocators.allu_ReesContrN) # Реестр неисполнительных контрольных поручений
    allu_ReesContrF = PageElement(xpath=KSEDLocators.allu_ReesContrF) # Реестр фактических исполнительных контрольных поручений
    allu_SostIspR   = PageElement(xpath=KSEDLocators.allu_SostIspR) # Состояние исполнения резолюций


    #Формы отчетов



























