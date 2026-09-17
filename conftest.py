import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\n[Архитектура] Глобальный запуск Chrome через conftest...")
    driver = webdriver.Chrome()
    yield driver
    print("\n[Архитектура] Глобальное закрытие Chrome...")
    driver.quit()

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"