from page_objects import PageObject

from page_objects import PageElement

from page_objects import MultiPageElement



class homePage(PageObject):

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

    myWork          = PageElement(xpath='//div[contains(text(), "Моя работа")]')           # Моя работа
    expedition      = PageElement(xpath='//div[contains(text(), "Экспедиция")]')           # Экспедиция
    navigation      = PageElement(xpath='//div[contains(text(), "Навигатор")]')            # Навигатор
    allur           = PageElement(xpath='//div[contains(text(), "Отчеты")]')               # Отчеты
    workReg         = PageElement(xpath='//div[contains(text(), "Работа регистратора")]')  # Работа регистратора
    medo            = PageElement(xpath='//div[contains(text(), "МЭДО")]')                 # МЭДО
    mySearch        = PageElement(xpath='//div[contains(text(), "Мои поисковые запросы")]')# Мои поисковые запросы

    # Область просмотра




















