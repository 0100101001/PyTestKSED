# Извлечение номера документа из файла
def rFile():

    my_file = open("D:\PyTestKSED\KSED\TestData\linkDoc.txt", "r")
    my_string = my_file.read()
    my_string.strip()
    return my_string
    my_file.close()

def rFileRD():

    my_file = open("D:\PyTestKSED\KSED\TestData\linkDocRD.txt", "r")
    my_string = my_file.read()
    my_string.strip()
    return my_string
    my_file.close()
#
#     my_file = open("tempDoc.txt")
#     my_string = my_file.read()
#     my_string.strip()
#
#     locator = str("'//a[text() = ") + '"' + str(my_string) + '"]' + "'"
#     return (locator)
#
#     my_file.close()


class KSEDLocators:

    # Ссылка на документ
    LinkDoc = rFile()
    LinkDocRD = rFileRD()


    # Форма авторизации
    username_text = 'username' # name
    password_text = 'password' # name
    LogIn_button = '//span/button' # xpath

    # *******СТРОКА МЕНЮ*******
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
    notificationProtokol = '(//a[contains(text(), "Протокол:")])[1]' #xpath # Первое в списке уведомление о протоколе
    notificationFirst = '(//span[@class = "detail"]/a)[1]' #id  # Уведомление первое в списке
    # *******МЕНЮ ПОЛЬЗОВАТЕЛЯ*******
    user_menu = 'HEADER_USER_MENU_POPUP_text' #id  # Меню пользователя
    USER_LOGOUT = 'HEADER_USER_MENU_LOGOUT_text' #id # Выход из системы

    my_profile = '//a[text() = "Мой профиль"]'  # xpath # Пункт меню "Мой профиль"
    fieldlabel = '//div[@class = "fieldlabel"]' #xpath # Должность в области краткой информации
    btnEdit_profile = '//button[contains(@id, "button-edit-button")]' #xpath # Кнопка "Изменить профиль"
    inputPosition = '//input[contains(@id, "-input-jobtitle")]' #xpath # Поле ввода должности

    logic_ESM = '//a[text() = "Логика ECM. Мой профиль"]'  # xpath # Пункт меню "Логика ECM. Мой профиль"
    autoAnswerText = 'prop_lecm-absence_auto-answer-text' #name # Текст автоответа (Меня нет в офисе)
    btnCancelAbsence = '//button[contains(@id, "cancelButton-button")]' #xpath # Кнопка "Отменить отсутствие"
    btnYes = '//button[text() = "Да"]' #xpath # Кнопка "Да" (отменить отсутствие)


    edit_password = '//a[text() = "Изменить пароль"]' #xpath # Пункт меню "Изменить пароль"
    inputOldPassword = '//input[contains(@id, "oldpassword")]' #xpath # Введите старый пароль
    inputNewPassword1 = '//input[contains(@id, "newpassword1")]'  # xpath # Введите старый пароль
    inputNewPassword2 = '//input[contains(@id, "newpassword2")]'  # xpath # Введите старый пароль
    btnOKchange = '//button[contains(@id, "_default-bu")][text() = "ОК"]' #xpath # Кнопка "Изменить пароль"

    # *******ЛЕВАЯ ЧАСТЬ СТРАНИЦЫ (Кнопка "Создать" и разделы)*******
    newDoc_button = '//button[contains(@id, "newDocumentButton-button")]' #xpath  # "Создать"

    protocol = '//a[contains(@class, "hassubmenu")][contains(text(), "Протокол")]' #xpath  # Протокол
    rd = '//a[contains(@class, "hassubmenu")][contains(text(), "Распорядительный документ")]' #xpath  # РД
    reestr = '//a[contains(text(), "Реестр")]' #xpath  # Реестр
    poruchenie = '//a[contains(@class, "hassubmenu")][contains(text(), "Поручение")]' #xpath  # Поручение
    resolution = '//a[contains(@class, "hassubmenu")][contains(text(), "Резолюция")]' #xpath  # Резолюция
    SZ = '//a[contains(@class, "hassubmenu")][contains(text(), "Служебная записка")]' #xpath  # Служебная записка
    proizvDoc = '//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Произвольный документ")]' # xpath Произвольный документ
    paket_vh = '//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Пакет входящей корреспонденции")]' #xpath #Пакет Вх. кор.
    vhDoc = '//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Входящий документ")]'
    ishDoc = '//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Исходящий документ")]'

    # РАЗДЕЛЫ
    myWork = '//div[contains(text(), "Моя работа")]' #xpath  # Моя работа

    expedition = '//div[contains(text(), "Экспедиция")]' #xpath  # Экспедиция

    navigation = '//div[contains(text(), "Навигатор")]' #xpath  # Навигатор

    allur = '//div[contains(text(), "Отчеты")]' #xpath  # Отчеты

    workReg = '//div[contains(text(), "Работа регистратора")]' #xpath  # Работа регистратора

    medo = '//div[contains(text(), "МЭДО")]' #xpath  # МЭДО

    mySearch = '//div[contains(text(), "Мои поисковые запросы")]' #xpath  # Мои поисковые запросы
    poiskzapr = '//span[text() = "Поисковые запросы"]' #xpath # Поисковые запросы
    myPoiskZapr = '//td[contains(@id, "ygtvcontente")]/span[text() = "2"]' #xpath # Поисковые запросы
    ControlZapr = '//span[text() = "Управление поисковыми запросами"]' #xpath # Управление поисковыми запросами


    # ОБЛАСТЬ ПРОСМОТРА (КСЭД)
    oblProsm = '(//div[contains(@id, "_default-body")][contains(@class, "datagrid")])[2]' #xpath # Область просмотра
    full_text_search = '(//input[contains(@id, "_default-full-text-search")])[1]' #xpath # Поисковая строка
    oneDocInList = '(//a[contains(@href, "document?nodeRef=workspace")])[1]' #xpath # Первый документ в списке
    subordinate = '//span[@class = "expand-table-icon"]' #xpath # "+" раскрытие подчиненные документы
    oneSubordInList = '(//a[contains(@href, "document?nodeRef=workspace")]' \
                      '[not(contains(@href, "/d"))])[1]' #xpath # Первая ссылка на подчиненный документ
    ActionTab = '//span[contains(@class, "group-actions-counter")]' #xpath # Кнопка "Действия с выбранными"
    chBinOnl = '//input[contains(@id, "_default-select-all-records")]'#'//input[@name = "fileChecked"][3]'


    # ОТЧЕТЫ
    section_allur = '//div[contains(@id, "ac-head")][contains(text(), "Отчеты")]' #xpath  # Раздел "Отчеты"
    node_Logs = '//span[contains(text(), "Журналы")]'#xpath                               # "Журналы"

    node_Statis = '//span[contains(@class, "ygtvlabel")][contains(text(), "Статистические")]'#xpath  # "Статистические отчеты"
    edsBykindStat = '//a[contains(@onclick, "eds-by-kind-stat")]' #xpath # Отчет "Сводка по видам документов"

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


    # *******РАБОТА С ДОКУМЕНТОМ*******

    # ОБЩИЕ АТРИБУТЫ
    #(форма создания документа)
    title = 'prop_lecm-document_title'  # name  # Заголовок

    category_doc = '//input[cункontains(@id, "-category-assoc-cntrl-autocomplete-input")]'  # xpath  # Категория документа

    doc_type = '//button[contains(@id, "type-assoc-cntrl-tree-picker-button-button")]' #xpath # Вид документа(кнопка выбора)
    doc_typeInp = '//input[contains(@id, "type-assoc-cntrl-autocomplete-input")]'      #xpath # Вид документа(поле ввода)
    btnOKDT = '//button[contains(@id, "type-assoc-cntrl-ok-button")]'                  # xpath # Вид документа (кнопка "ОК")

    podpisant = '//input[contains(@id, "signerEmployeeAssoc-cntrl-autocomplete-input")]'  # xpath  # Подписант(ы)

    sposob_dost = '//input[contains(@id, "_delivery-method-assoc-cntrl-autocomplete-input")]'  # xpath # Способ доставки

    btnCreateDoc = '//button[contains(@id, "_default-form-submit-button")]'  # xpath  # Кнопка "Создать"

    adresat = '//input[contains(@id, "_recipient-assoc-autocomplete")]'  # xpath # Адресат

    korrespondent = '//input[contains(@id, "sender-assoc-autocomplete")]'  # xpath # Корреспондент

    # (карточка документа)
    attachments = '//span[contains(@id, "action-expand")][contains(@class, "attachments-expand")]' #xpath # Переход во вкладку "Вложения"
    vlozheniya = '//h2[contains(@id, "heading")][contains(text(), "Вложения")]'  # xpath # Вложения (раскрытие раздела)
    osnSvedeniya = '//h2[contains(@id, "heading")][contains(text(), "Основные сведения")]' #xpath # Основные сведения (раскрытие раздела)
    printForm = '//h2[contains(@id, "heading")][contains(text(), "Печатные формы")]' #xpath # Печатные формы (раскрытие раздела)
    printBarCode = '//a[contains(text(), "Штрих-код документа")]' #xpath #Печатная форма штрих кода документа
    btnPrintInPrintForm = 'print' #id # Кнопка печати в окне печатной формы
    mode = '//button[contains(@id, "default-cntrl-split-panel-button-button")]' #xpath
    fileUpload = '(//button[contains(@id, "fileUpload-button-button")])[2]' #xpath # Загрузить файл
    fileUpload2 = '//button[contains(@id, "fileUpload-button-button")]'  # xpath # Загрузить файл в поручении
    files = '//input[@type="file"][@name="files[]"]' #xpath # Выберите файлы
    show = '//a[contains(@id, "action-show-main")]' #xpath # Показать общую карточка
    show_list = '//a[@class = "preview-show-list"]' #xpath # Показать ввиде списка
    btnPrint = '//button[contains(@id, "print_from_preview")]' #xpath # Кнопка печати в форме предварительного просмотра вложения

    soglasovanieWkladka = '//em[contains(text(), "Согласование")]'  # xpath # Вкладка "Согласование"
    createRuleBtn = '//button[contains(@id, "create-approval-list-button-button")]'  # xpath # Кнопка "Создать маршрут"
    createRuleIndivid = '//a[text() = "Индивидуальный маршрут"]' #xpath # "Индивидуальный маршрут"
    addEtap = '//button[contains(@id, "cntrl-add-stage-button")]' #xpath # Кнопка "Добавить этап"
    tipeEtap = '//input[contains(@id, "type-cntrl-autocomplete-input")]' #xpath # "Вид этапа"
    soglasuychie = '//input[contains(@id, "approvers-autocomplete")]' #xpath # "Согласующие"
    btnOKformSogl = '//button[contains(@id, "form-submit-button")]' #xpath # Кнопка "ОК" на форме добавления этапа согласования


    punkti = '//em[contains(text(), "Пункты")]' #xpath # Вкладка "Пункты"
    punktiBtn = '//button[contains(@id, "create-point-button")]' #xpath # Кнопка "Пункты"
    punktPoruch = '(//a[contains(@class, "yuimenuitemlabel")][contains(text(), "Поручение")])[1]' #xpath # Пункт/Поручение
    textPoruch = '//textarea[contains(@id, "ts_point-desc")]' #xpath # Текст поручения
    tipPoruch = '//input[contains(@id, "type-assoc-cntrl-autocomplete-input")]'  # xpath # Тип поручения
    otvetstv_ispolnVpunktah = '//input[contains(@id, "_executor-assoc-cntrl-autocomplete-input")]'  # xpath # Ответственный исполнитель в пунктах карточки документа
    srokIspoln = '//input[contains(@id, "ts_limitation-date-cntrl-date")]' #xpath # Срок исполнения (среднее знач)

    btnOKform = '//button[contains(@id, "form-submit-button")]' #xpath # Кнопка ОК на форме

    addPunkt = '(//button[@title = "Добавить пункт"])[1]' #xpath # Кнопка "Добавить пункт"
    textPunktaRD = 'prop_lecm-ord-table-structure_item-content' #name # Текст пункта РД
    rassilka = '//em[text() = "Рассылка"]' #xpath # Вкладка "Рассылка"
    btnVipolnit = '(//button[contains(@id, "create-mailing-list-button-button")])[1]'  # xpath # Кнопка "Создать маршрут"
    punktBtnVipolnit = '//a[text() = "Создать и заполнить указатель"]' #xpath # Создать и заполнить
    otvetstv_ispolnVpunktahRD = '//input[contains(@id, "executor-assoc-cntrl-autocomplete-input")]' #xpath # Ответственный исполнитель в пункте РД
    #(Функциональное меню "Действия")
    #Согласовать
    sendFor_approval = '//div[contains(text(), "Направить на согласование")]' #xpath # Действие "Направить на согласование"
    sendFor_execution = '//div[contains(text(), "Направить на исполнение")]'  # xpath # Действие "Направить на исполнение"
    btnOKnaprNaIspoln = '//button[text() = "ОК"]' #xpath # Кнопка "ОК" на форме подтверждения действия "Направить на исполнение"
    confirm = '(//button[contains(@id, "-button")][text() = "ОК"])[2]' #xpath # Подтверждение согласования

    #"Отправить отчет"
    actionSendAllere = '//div[text() = "Отправить отчет"]' #xpath # "Отправить отчет" действие
    btnSend = '//button[text() = "Отправить"]' #xpath # Кнопка "Отправить"
    textAllur = '//textarea[contains(@name, "_execute_1ReportText")]' #xpath # Текстовое поле "Текст отчета"
    btnAddSvyz = '//button[contains(@id, "tree-picker-button-button")]' #xpath # Кнопка добавления связи "..."
    searchDoc = '//input[contains(@id, "picker-searchText")]' #xpath # Строка поиска в форме подбора
    oneListEl = '(//span[@class = "addIcon"])[1]'  # xpath # Первый элемент в списке справочника
    btnOK = '//button[contains(@id, "-ok-button")]' #xpath # Кнопка "ОК" в форме подбора


    status_Doc = '//span[contains(@id, "_status")]' #xpath # Статус документа во вкладке (Основные сведения)

    # (панель согласования)
    APPROVED_button = '//button[contains(@id, "APPROVED-button")]' #xpath # Кнопка "Согласовать"
    APPROVED_WITH_REMARK_button = '//button[contains(@id, "APPROVED_WITH_REMARK-button")]' #xpath # Кнопка "Согласовать с комментариями"
    REJECTED_button = '//button[contains(@id, "REJECTED-button")]' #xpath # Кнопка "Отклонить"
    internal_approval = '//button[contains(@id, "internal_approval-button")]' #xpath # Кнопка "Внутреннее согласование"
    prop_bpm_comment = 'prop_bpm_comment' #name # Поле комментария
    apply_button_button = '//button[contains(@id, "apply-button")]' #xpath # Кнопка "ОК" при вынесении решения согласования

    SIGNED_button = '//button[contains(@id, "SIGNED-button")]' #xpath # Кнопка "Подписать"




    # # ПРОТОКОЛ
    # #(форма создания документа)
    # addEl = '(//span[@class="addIcon"])[7]' #xpath  # Вид документа(Протокол совещания рабочей группы)
    # addEl2 = '(//span[@class="addIcon"])[6]' #xpath Вид документа "Служебная записка"

    # РАСПОРЯДИТЕЛЬНЫЙ ДОКУМЕНТ
    #(форма создания документа)
    preambula = '//textarea[contains(@id, "-eds-document_summaryContent")]' #xpath  # Преамбула
    obcontrol = '//input[contains(@id, "-ord_controller-assoc-cntrl-autocomplete-input")]' #xpath  # Общий контроль
    wid_doc = '(//select[contains(@id, "_assoc_lecm-eds-document_document-type-assoc")])[1]' #xpath  # Вид документа (в РД)
    wid_doc_rasp = '//option[contains(text(), "Распоряжение")]' #xpath  # Вид документа РД (Распоряжение)

    # ПРОТОКОЛ
    #(форма создания документа)
    addEl = '(//span[@class="addIcon"])[7]' #xpath  # Вид документа(Протокол совещания рабочей группы)
    addEl2 = '(//span[@class="addIcon"])[6]' #xpath Вид документа "Служебная записка"
    date = '//input[contains(@id, "_meeting-date-cntrl-date")]' #xpath  # Дата совещания
    category = '//input[contains(@id, "_category-assoc-cntrl-autocomplete-input")]'#xpath  # Категория
    Chairman = '//input[contains(@id, "chairman-assoc-cntrl-autocomplete-input")]'#xpath  # Председатель
    Secretary = '//input[contains(@id, "_secretary-assoc-cntrl-autocomplete-input")]'#xpath  # Секретарь
    person_present = '//input[contains(@id, "_attended-assoc-cntrl-autocomplete-input")]'#xpath  # Присутствовали
    #(карточка документа)



    #РЕЕСТР
    #(форма создания документа)
    vid_reestra = '//select[contains(@id, "_document-registry_type")]' #xpath  # Вид реестра
    vid_reestraPR = '//option[contains(text(), "Передачи на регистрацию")]' #xpath  # Вид реестра (Передачи на рег..)
    vid_reestraPP = '//option[contains(text(), "Приема/передачи")]' #xpath  # Вид реестра (Приема/передачи)
    btnCreateChern = '//button[contains(text(), "Создать черновик")]' #xpath  # Кнопка "Создать черновик"
    btnCreateSend = '//button[contains(text(), "Создать и отправить")]'  # Кнопка "Создать и отправить"
    inpDoc = '//input[contains(@id, "registry_doc-assoc-cntrl-autocomplete-input")]' #xpath  # Поле "Документы"
    poluchatel = '//input[contains(@id, "document-registry_receiver-assoc-autocomplete")]' #xpath  # Поле "Получатель"

    # СЛУЖЕБНАЯ ЗАПИСКА
    #(форма создания документа)
    adresati = '//input[contains(@id, "internal_recipients-assoc-autocomplete")]'#xpath # Адресаты

    # ПРОИЗВОЛЬНЫЙ ДОКУМЕНТ
    #(форма создания документа)
    prorabotka = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[1]'#xpath # Проработка
    chBprorab = '(//input[contains(@class, "formsCheckBox")])[1]' #xpath # чекбокс проработка
    normokontrol = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[2]'#xpath # Нормоконтроль
    chBnorm = '(//input[contains(@class, "formsCheckBox")])[2]' #xpath # чекбокс Проработка
    soglasovanie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[3]'#xpath # Согласование
    podpisanie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[4]'#xpath # Подписание
    utverzhdenie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[5]'#xpath # Утверждение
    oznakomlenie = '(//input[contains(@id, "_status-employee-assoc-cntrl-autocomplete-input")])[7]'#xpath # Ознакомление

    # ПОРУЧЕНИЕ
    # (форма создания документа)
    text_poruch = 'prop_lecm-errands_content' # name #Текст поручения
    otvetstv_ispoln = '//input[contains(@id, "executor-assoc-autocomplete")]'#xpath # Ответственный исполнитель

    # ПАКЕТ ВХОДЯЩЕЙ КОРРЕСПОНДЕНЦИИ

    # ВХОДЯЩИЙ ДОКУМЕНТ
    #(форма создания документа)
    ishNumber = 'prop_lecm-incoming_outgoing-number' #name # Исходящий номер
    dateIS = '//input[contains(@id, "-incoming_outgoing-date-cntrl-date")]'  # xpath  # Дата исходящего

    # ИСХОДЯЩИЙ ДОКУМЕНТ
    #(форма создания документа)
    osnovPodpis = 'prop_lecm-outgoing_signing-basis' #name # Основание подписания
    korrespondentISH = '//input[contains(@id, "contractor-assoc-autocomplete")]' #xpath # Корреспондент
    clickNull = '//div[contains(@id, "_default-form-container")]'  # КЛИК ВНЕ АТРИБУТОВ

    # Мои поисковые Запросы
    listChange = '//select[contains(@id, "default_searchQuery-selectType-entry")]' #Выпадающий список
    listChangeSZ = '//option[text() = "Служебная записка"]' #Выпадающий список - служебная записка
    listChangeRD = '//option[text() = "Распорядительный документ"]'  # Выпадающий список - РД
    butSave = '//div[contains(@class, "query-button-grey")][3]' #Кнопка сохранить
    nameZap = '//input[contains(@id, "createDetails_prop_lecm-search-queries_name")]' #Наименование запроса
    zaprosToDel = '//span[text() = "ToDel"]'#созданный запрос
    butDel = '//span[contains(@class, "yui-button yui-push-button")]//button[text() = "Удалить поисковый запрос"]' #Кнопка удалить
    butRed = '//span[contains(@class, "yui-button yui-push-button")]//button[text() = "Редактировать поисковый запрос"]' #Кнопка редактировать
    butDelAc = '//span[contains(@class, "first-child")]//button[text() = "Удалить"]' #Кнопка удалить подтверждение
    checkBoxFirst = '(//input[@name = "fileChecked"])[1]' #Первый чекбокс в списке
    butAct = '(//button[text() = "Действия с выбранными"])[2]' #Кнопка действия с выбором
    butExp ='(//button[text() = "Экспорт"])[2]' #Кнопка экспорта
    butFavorite = '//a [text() = "Добавить в избранное"]' #Кнопка добавить в избранное
    butOK = '//button[text() = "Ок"]' #Кнопка OK добавить в избранное
    butSelExp = '(//a[text() = "Выгрузить выбранные"])' #Кнопка экспорта выбранного