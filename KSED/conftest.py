#!/usr/bin/python3

# -*- encoding=utf8 -*-



# This is example shows how we can manage failed tests

# and make screenshots after any failed test case.



import pytest

import allure

import uuid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options



@pytest.hookimpl(hookwrapper=True, tryfirst=True)

def pytest_runtest_makereport(item, call):

    # This function helps to detect that some test failed

    # and pass this information to teardown:



    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    return rep





@pytest.fixture

def web_browser(request, selenium):
    options = Options()                                                         # запуск firefox в скрытом режиме
    options.add_argument('-headless')                                           # запуск firefox в скрытом режиме
    browser = webdriver.Firefox(executable_path='geckodriver', options=options) # запуск firefox в скрытом режиме

    # options = Options()                                                           # запуск chrome в скрытом режиме
    # options.add_argument('--headless')                                            # запуск chrome в скрытом режиме
    # browser = webdriver.Chrome(chrome_options=options)                            # запуск chrome в скрытом режиме

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # browser = webdriver.Chrome(options=options)


    # browser = selenium                                                      # закомментировать для скрытого режима

    browser.set_window_size(1920, 1080)
    # browser.maximize_window()




    # browser.set_window_size(1920, 1080)
    #browser.maximize_window()



    # Return browser instance to test case:

    browser.implicitly_wait(10)
    yield browser



    # Do teardown (this code will be executed after each test):



    if request.node.rep_call.failed:

        # Make the screen-shot if test failed:

        try:

            browser.execute_script("document.body.bgColor = 'white';")



            # Make screen-shot for local debug:

            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')



            # Attach screenshot to Allure report:

            allure.attach(browser.get_screenshot_as_png(),

                          name=request.function.__name__,

                          attachment_type=allure.attachment_type.PNG)



            # For happy debugging:

            print('URL: ', browser.current_url)

            print('Browser logs:')

            for log in browser.get_log('browser'):

                print(log)



        except:

            pass # just ignore any errors here

    browser.quit()