
class KSEDLocators:
    # Форма авторизации
    username_text = 'username' # name
    password_text = 'password' # name
    LogIn_button = '//span/button' # xpath

    # Строка меню
    ksed = '(//a[contains(@title, "КСЭД")])[1]' #xpath  # КСЭД

    barcode_search = 'SEARCH_BARCODE_text' #id  # Поиск по ШК
    search_bc = '//input[contains(@id, "search_bc")]' #xpath  # Строка поиска по ШК

    more_menu = 'LOGIC_ECM_MORE_MENU_BAR' #id # Меню "Ещё"
    ksed_in_more_m = 'SED_MENU_ITEM_ADDITIONAL_text' #id  # КСЭД в меню "Ещё"
    Company_dir = '//a[contains(@title, "Справочник организации")]' #xpath  # Справочник организации
    admin = '//a[contains(@title, "Администрирование")]' #xpath  # Администрирование
    transfer = '//a[contains(@title, "Передача дел")]' #xpath  # Передача дел
    arm_arh = '//a[contains(@title, "Передача дел")]' #xpath  # АРМ Архивное дело
    verify = '//a[contains(@title, "Верификация")]' #xpath  # Верификация
    scanner = '//a[contains(@title, "Верификация")]' #xpath  # Работа со сканером ШК

    notification = 'NOTIFICATIONS_text' #id  # Уведомления

    # Меню пользователя
    user_menu = 'HEADER_USER_MENU_POPUP_text' #id  # Меню пользователя

    # Левая часть страницы (Кнопка "Создать" и разделы)
    newDoc_button = '//button[contains(@id, "newDocumentButton-button")]' #xpath  # "Создать"

    protocol = '//a[contains(@class, "hassubmenu")][contains(text(), "Протокол")]' #xpath  # Протокол
    rd = '//a[contains(@class, "hassubmenu")][contains(text(), "Распорядительный документ")]' #xpath  # РД
    reestr = '//a[contains(text(), "Реестр")]' #xpath  # Реестр
    poruchenie = '//a[contains(@class, "hassubmenu")][contains(text(), "Поручение")]' #xpath  # Поручение
    resolution = '//a[contains(@class, "hassubmenu")][contains(text(), "Резолюция")]' #xpath  # Резолюция
    SZ = '//a[contains(@class, "hassubmenu")][contains(text(), "Служебная записка")]' #xpath  # Служебная записка
    proizvDoc = '//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Произвольный документ")]' # xpath Произвольный документ

    # Форма создания документа
    doc_type = '//button[contains(@id, "type-assoc-cntrl-tree-picker-button-button")]' #xpath  # Вид документа(кнопка выбора)
    addEl = '(//span[@class="addIcon"])[7]' #xpath  # Вид документа(Протокол совещания рабочей группы)
    addEl2 = '(//span[@class="addIcon"])[6]' #xpath Вид документа "Служебная записка"
    btnOKDT = '//button[contains(@id, "type-assoc-cntrl-ok-button")]' #xpath # Вид документа (ОК)
    title = 'prop_lecm-document_title' #name  # Заголовок *****
    preambula = '//textarea[contains(@id, "-eds-document_summaryContent")]' #xpath  # Преамбула
    podpisant = '//input[contains(@id, "signerEmployeeAssoc-cntrl-autocomplete-input")]' #xpath  # Подписант
    obcontrol = '//input[contains(@id, "-ord_controller-assoc-cntrl-autocomplete-input")]' #xpath  # Общий контроль
    wid_doc = '(//select[contains(@id, "_assoc_lecm-eds-document_document-type-assoc")])[1]' #xpath  # Вид документа в РД
    wid_doc_rasp = '//option[contains(text(), "Распоряжение")]' #xpath  # Вид документа РД (Распоряжение)
    date = '//input[contains(@id, "_meeting-date-cntrl-date")]' #xpath  # Дата совещания
    category = '//input[contains(@id, "_category-assoc-cntrl-autocomplete-input")]'#xpath  # Категория
    Chairman = '//input[contains(@id, "chairman-assoc-cntrl-autocomplete-input")]'#xpath  # Председатель
    Secretary = '//input[contains(@id, "_secretary-assoc-cntrl-autocomplete-input")]'#xpath  # Секретарь
    person_present = '//input[contains(@id, "_attended-assoc-cntrl-autocomplete-input")]'#xpath  # Присутствовали
    category_doc = '//input[contains(@id, "-category-assoc-cntrl-autocomplete-input")]'#xpath  # Категория документа *****
    btnCreateDoc = '//button[contains(@id, "_default-form-submit-button")]'#xpath  # Кнопка "Создать"
    vid_reestra = '//select[contains(@id, "_document-registry_type")]' #xpath  # Вид реестра
    vid_reestraPR = '//option[contains(text(), "Передачи на регистрацию")]' #xpath  # Вид реестра (Передачи на рег..)
    vid_reestraPP = '//option[contains(text(), "Приема/передачи")]' #xpath  # Вид реестра (Приема/передачи)
    btnCreateChern = '//button[contains(text(), "Создать черновик")]' #xpath  # Кнопка "Создать черновик"
    btnCreateSend = '//button[contains(text(), "Создать и отправить")]'  # Кнопка "Создать и отправить"
    inpDoc = '//input[contains(@id, "registry_doc-assoc-cntrl-autocomplete-input")]' #xpath  # Поле "Документы"
    poluchatel = '//input[contains(@id, "document-registry_receiver-assoc-autocomplete")]' #xpath  # Поле "Получатель"
    adresat = '//input[contains(@id, "internal_recipients-assoc-autocomplete")]' # Адресаты
    prorabotka = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[1]' # Проработка
    normokontrol = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[2]' # Нормоконтроль
    soglasovanie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[3]' # Согласование
    podpisanie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[4]' # Подписание
    utverzhdenie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[5]' # Утверждение
    oznakomlenie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[7]' # Ознакомление
    vid_docInput = '//input[contains(@id, "_document-type-assoc-cntrl-autocomplete-input")]' # Вид документа (Поле)

    clickNull = '//div[contains(@id, "_default-form-container")]' # КЛИК ВНЕ АТРИБУТОВ


    myWork = '//div[contains(text(), "Моя работа")]' #xpath  # Моя работа
    expedition = '//div[contains(text(), "Экспедиция")]' #xpath  # Экспедиция
    navigation = '//div[contains(text(), "Навигатор")]' #xpath  # Навигатор
    allur = '//div[contains(text(), "Отчеты")]' #xpath  # Отчеты
    workReg = '//div[contains(text(), "Работа регистратора")]' #xpath  # Работа регистратора
    medo = '//div[contains(text(), "МЭДО")]' #xpath  # МЭДО
    mySearch = '//div[contains(text(), "Мои поисковые запросы")]' #xpath  # Мои поисковые запросы

    # Область просмотра

    # Отчеты
    section_allur = '//div[contains(@id, "ac-head")][contains(text(), "Отчеты")]' #xpath  # Раздел "Отчеты"
    node_Logs = '//span[contains(text(), "Журналы")]'#xpath  # "Журналы"
    node_Statis = '//span[contains(@class, "ygtvlabel")][contains(text(), "Статистические")]'#xpath  # "Статистические отчеты"
    node_ispDisp = '//span[contains(text(), "Отчеты по исполнительской дисциплине")]' #xpath

    logs_incDoc = '//a[contains(text(), "Журнал регистрации входящих документов")]' #xpath
    logs_outDoc = '//a[contains(text(), "Журнал регистрации исходящих документов")]' #xpath
    logs_raspDoc = '//a[contains(text(), "Журнал регистрации Распорядительных документов")]' #xpath
    logs_sluDoc = '//a[contains(text(), "Журнал Регистрации служебных записок")]' #xpath

    stat_specDoc = '//a[contains(text(), "Сводка по видам документов")]' #xpath
    stat_temDoc = '//a[contains(text(), "Сводка по тематикам документов")]' #xpath
    stat_temDocO = '//a[contains(text(), "Сводка по тематикам документов (объедин.)")]' #xpath
    stat_tipDoc = '//a[contains(text(), "Сводка по типам документов")]' #xpath

    allu_ispIncDoc = '//a[contains(text(), "Исполнение входящих документов")]' #xpath
    allu_raspDoc = '//a[contains(text(), "Исполнение распорядительного документа")]' #xpath
    allu_sluDoc = '//a[contains(text(), "Исполнение служебных записок")]' #xpath
    allu_ispDis = '//a[contains(text(), "Исполнительская дисциплина по авторам")]' #xpath
    allu_ispDispA = '//a[contains(text(), "Исполнительская дисциплина по исполнителям")]' #xpath
    allu_NispDI = '//a[contains(text(), "Неисполнительные поручения с истекшим сроком")]' #xpath
    allu_NispDIrg = '//a[contains(text(), "Неисполнительные поручения с истекшим сроком РГ")]' #xpath
    allu_istS = '//a[contains(text(), "Поручения с истекающим сроком")]' #xpath
    allu_narS = '//a[contains(text(), "Поручения, исполненные с нарушением срока")]' #xpath
    allu_prodIsp = '//a[contains(text(), "Продуктивность по Исполнителям")]' #xpath
    allu_prodPodr = '//a[contains(text(), "Продуктивность по Подразделениям")]' #xpath
    allu_ReesContr = '//a[contains(text(), "Реестр для закрытия неактуальных контрольных поручений")]' #xpath
    allu_ReesContrN = '//a[contains(text(), "Реестр неисполнительных контрольных поручений")]' #xpath
    allu_ReesContrF = '//a[contains(text(), "Реестр фактических исполнительных контрольных поручений")]' #xpath
    allu_SostIspR = '//a[contains(text(), "Состояние исполнения резолюций")]' #xpath
