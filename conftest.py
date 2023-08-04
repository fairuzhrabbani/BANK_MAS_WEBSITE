import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

BaseUrl = "https://todomvc.com/examples/knockoutjs/"

@pytest.fixture(scope="function", autouse=True)
def browser_setup(request):
    chrome_service = Service(executable_path='./Drivers/chromedriver_win32/chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)