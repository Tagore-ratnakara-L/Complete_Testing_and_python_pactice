import pytest
from selenium import webdriver

#Appliying below fixture to get pulled chrome driver
# @pytest.fixture()
# def driver():
#     print("creating chrome driver")
#     my_driver = webdriver.Chrome()
#     yield my_driver
#     print("Closing chrome driver")
#     my_driver.quit()

#Adding fixture to get multiple browsers open
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"creating {browser} driver")
    if browser=="chrome":
        my_driver = webdriver.Chrome()
    elif browser=="edge":
        my_driver = webdriver.edge()
    else:
        print(f"Expected 'chrome' or 'edge' , but got {browser}")
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()

def pytest_adoption(parser):
    parser.adoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or edge)"
    )