import pytest
from selenium import webdriver

from Config.config import TestData


# @pytest.fixture(params=["chrome", "edge"], scope='class')
@pytest.fixture(params=["edge"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path=TestData.EDGE_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    web_driver.set_page_load_timeout(30)
    yield
    web_driver.close()
