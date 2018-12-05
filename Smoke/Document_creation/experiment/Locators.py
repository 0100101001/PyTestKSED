import logging, os


class Locator:

    username_text = 'username' # name

    password_text = 'password' #name

    LogIn_button = '//span/button' # xpath

    # def getByType(self, object, locatorType):
    #
    #     locatorType = locatorType.lower()
    #
    #     if locatorType == "id":
    #         return By.ID
    #     elif locatorType == "name":
    #         return By.NAME
    #     elif locatorType == "xpath":
    #         return By.XPATH
    #     elif locatorType == "css":
    #         return By.CSS_SELECTOR
    #     elif locatorType == "class":
    #         return By.CLASS_NAME
    #     elif locatorType == "link":
    #         return By.LINK_TEXT
    #     else:
    #         self.log.info("Locator type " + locatorType +
    #                       " not correct/supported")
    #     return False

    def __init__(self, web_driver, uri=''):

        super().__init__(web_driver, uri)
