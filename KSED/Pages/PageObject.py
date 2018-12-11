from page_objects import PageObject, PageElement
#from Locators import HomePageLocators



class Locator(PageObject):

    # ПРЕДУСЛОВИЕ
    baseURL = 'http://213.128.208.34/share/page/arm?code=SED'

    BARCODE = '171267'
    # ---------------------------------------------

    # Форма авторизации
    username_text = PageElement(name='username')
    password_text = PageElement(name='password')
    LogIn_button = PageElement(xpath='//span/button')


    # Строка меню
    ksed            = PageElement(xpath='(//a[contains(@title, "КСЭД")])[1]')              # КСЭД

    barcode_search  = PageElement(id_='SEARCH_BARCODE_text')                               # Поиск по ШК
    search_bc       = PageElement(xpath='//input[contains(@id, "search_bc")]')             # Строка поиска по ШК

    more_menu       = PageElement(id_='LOGIC_ECM_MORE_MENU_BAR')                           # Меню "Ещё"
    ksed_in_more_m  = PageElement(id_='SED_MENU_ITEM_ADDITIONAL_text')                     # КСЭД в меню "Ещё"
    Company_dir     = PageElement(xpath='//a[contains(@title, "Справочник организации")]') # Справочник организации
    admin           = PageElement(xpath='//a[contains(@title, "Администрирование")]')      # Администрирование
    transfer        = PageElement(xpath='//a[contains(@title, "Передача дел")]')           # Передача дел
    arm_arh         = PageElement(xpath='//a[contains(@title, "Передача дел")]')           # АРМ Архивное дело
    verify          = PageElement(xpath='//a[contains(@title, "Верификация")]')            # Верификация
    scanner         = PageElement(xpath='//a[contains(@title, "Верификация")]')            # Работа со сканером ШК

    notification    = PageElement(id_='NOTIFICATIONS_text')                                # Уведомления

    # Меню пользователя
    user_menu       = PageElement(id_='HEADER_USER_MENU_POPUP_text')                       # Меню пользователя

    # Левая часть страницы (Кнопка "Создать" и разделы)
    newDoc_button   = PageElement(xpath='//button[contains(@id, "newDocumentButton-button")]')  # "Создать"

    protocol        = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Протокол")]') # Протокол
    rd              = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Распорядительный документ")]') # РД
    reestr          = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Реестр")]') # Реестр
    poruchenie      = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Поручение")]') # Поручение
    resolution      = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Резолюция")]')  # Резолюция
    SZ              = PageElement(xpath='//a[contains(@class, "hassubmenu")][contains(text(), "Служебная записка")]')  # Служебная записка




    # Форма создания документа
    doc_type        = PageElement(xpath='//button[contains(@id, "type-assoc-cntrl-tree-picker-button-button")]') #Вид документа(кнопка выбора)
    addEl           = PageElement(xpath='(//span[@class="addIcon"])[7]') # Вид документа(Протокол совещания рабочей группы)
    btnOKDT         = PageElement(xpath='//button[contains(@id, "type-assoc-cntrl-ok-button")]') # Вид документа (ОК)
    title           = PageElement(name='prop_lecm-document_title') # Заголовок *****
    preambula       = PageElement(xpath='//textarea[contains(@id, "-eds-document_summaryContent")]') # Преамбула
    podpisant       = PageElement(xpath='//input[contains(@id, "signerEmployeeAssoc-cntrl-autocomplete-input")]') # Подписант
    obcontrol       = PageElement(xpath='//input[contains(@id, "-ord_controller-assoc-cntrl-autocomplete-input")]')  # Общий контроль
    wid_doc         = PageElement(xpath='(//select[contains(@id, "_assoc_lecm-eds-document_document-type-assoc")])[1]')# Вид документа в РД
    wid_doc_rasp    = PageElement(xpath='//option[contains(text(), "Распоряжение")]') # Вид документа РД (Распоряжение)
    date            = PageElement(xpath='//input[contains(@id, "_meeting-date-cntrl-date")]') # Дата совещания
    category        = PageElement(xpath='//input[contains(@id, "_category-assoc-cntrl-autocomplete-input")]') # Категория
    Chairman        = PageElement(xpath='//input[contains(@id, "chairman-assoc-cntrl-autocomplete-input")]') # Председатель
    Secretary       = PageElement(xpath='//input[contains(@id, "_secretary-assoc-cntrl-autocomplete-input")]') # Секретарь
    person_present  = PageElement(xpath='//input[contains(@id, "_attended-assoc-cntrl-autocomplete-input")]') #Присутствовали
    category_doc    = PageElement(xpath='//input[contains(@id, "-category-assoc-cntrl-autocomplete-input")]') # Категория документа *****
    btnCreateDoc    = PageElement(xpath='//button[contains(@id, "_default-form-submit-button")]') # Кнопка "Создать"
    vid_reestra     = PageElement(xpath='//select[contains(@id, "_document-registry_type")]') # Вид реестра
    vid_reestraPR   = PageElement(xpath='//option[contains(text(), "Передачи на регистрацию")]') # Вид реестра (Передачи на рег..)
    vid_reestraPP   = PageElement(xpath='//option[contains(text(), "Приема/передачи")]') # Вид реестра (Приема/передачи)
    btnCreateChern  = PageElement(xpath='//button[contains(text(), "Создать черновик")]') # Кнопка "Создать черновик"
    btnCreateSend   = PageElement(xpath='//button[contains(text(), "Создать и отправить")]')  # Кнопка "Создать черновик"
    inpDoc          = PageElement(xpath='//input[contains(@id, "registry_doc-assoc-cntrl-autocomplete-input")]') # Поле "Документы"
    poluchatel      = PageElement(xpath='//input[contains(@id, "document-registry_receiver-assoc-autocomplete")]') # Поле "Получатель"


    myWork          = PageElement(xpath='//div[contains(text(), "Моя работа")]')           # Моя работа
    expedition      = PageElement(xpath='//div[contains(text(), "Экспедиция")]')           # Экспедиция
    navigation      = PageElement(xpath='//div[contains(text(), "Навигатор")]')            # Навигатор
    allur           = PageElement(xpath='//div[contains(text(), "Отчеты")]')               # Отчеты
    workReg         = PageElement(xpath='//div[contains(text(), "Работа регистратора")]')  # Работа регистратора
    medo            = PageElement(xpath='//div[contains(text(), "МЭДО")]')                 # МЭДО
    mySearch        = PageElement(xpath='//div[contains(text(), "Мои поисковые запросы")]')# Мои поисковые запросы

    # Область просмотра


    #Отчеты
    section_allur   = PageElement(xpath='//div[contains(@id, "ac-head")][contains(text(), "Отчеты")]') # Раздел "Отчеты"
    node_Logs       = PageElement(xpath='//span[contains(text(), "Журналы")]')              # "Журналы"
    node_Statis     = PageElement(xpath='//span[contains(@class, "ygtvlabel")][contains(text(), "Статистические")]') # "Статистические отчеты"
    node_ispDisp    = PageElement(xpath='//span[contains(text(), "Отчеты по исполнительской дисциплине")]')

    logs_incDoc     = PageElement(xpath='//a[contains(text(), "Журнал регистрации входящих документов")]')
    logs_outDoc     = PageElement(xpath='//a[contains(text(), "Журнал регистрации исходящих документов")]')
    logs_raspDoc    = PageElement(xpath='//a[contains(text(), "Журнал регистрации Распорядительных документов")]')
    logs_sluDoc     = PageElement(xpath='//a[contains(text(), "Журнал Регистрации служебных записок")]')

    stat_specDoc    = PageElement(xpath='//a[contains(text(), "Сводка по видам документов")]')
    stat_temDoc     = PageElement(xpath='//a[contains(text(), "Сводка по тематикам документов")]')
    stat_temDocO    = PageElement(xpath='//a[contains(text(), "Сводка по тематикам документов (объедин.)")]')
    stat_tipDoc     = PageElement(xpath='//a[contains(text(), "Сводка по типам документов")]')

    allu_ispIncDoc  = PageElement(xpath='//a[contains(text(), "Исполнение входящих документов")]')
    allu_raspDoc    = PageElement(xpath='//a[contains(text(), "Исполнение распорядительного документа")]')
    allu_sluDoc     = PageElement(xpath='//a[contains(text(), "Исполнение служебных записок")]')
    allu_ispDis     = PageElement(xpath='//a[contains(text(), "Исполнительская дисциплина по авторам")]')
    allu_ispDispA   = PageElement(xpath='//a[contains(text(), "Исполнительская дисциплина по исполнителям")]')
    allu_NispDI     = PageElement(xpath='//a[contains(text(), "Неисполнительные поручения с истекшим сроком")]')
    allu_NispDIrg   = PageElement(xpath='//a[contains(text(), "Неисполнительные поручения с истекшим сроком РГ")]')
    allu_istS       = PageElement(xpath='//a[contains(text(), "Поручения с истекающим сроком")]')
    allu_narS       = PageElement(xpath='//a[contains(text(), "Поручения, исполненные с нарушением срока")]')
    allu_prodIsp    = PageElement(xpath='//a[contains(text(), "Продуктивность по Исполнителям")]')
    allu_prodPodr   = PageElement(xpath='//a[contains(text(), "Продуктивность по Подразделениям")]')
    allu_ReesContr  = PageElement(xpath='//a[contains(text(), "Реестр для закрытия неактуальных контрольных поручений")]')
    allu_ReesContrN = PageElement(xpath='//a[contains(text(), "Реестр неисполнительных контрольных поручений")]')
    allu_ReesContrF = PageElement(xpath='//a[contains(text(), "Реестр фактических исполнительных контрольных поручений")]')
    allu_SostIspR   = PageElement(xpath='//a[contains(text(), "Состояние исполнения резолюций")]')


    #Формы отчетов

    def PE(self):
        r = self.username_text.locator
        print('123')


























