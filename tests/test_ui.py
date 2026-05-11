from selenium.webdriver.common.by import By


BASE_URL = "http://127.0.0.1:5000"


def test_page_title_is_visible(browser):
    browser.get(BASE_URL)
    title = browser.find_element(By.ID, "title")
    assert title.is_displayed()
    assert "Форма обратной связи" in title.text


def test_submit_button_text(browser):
    browser.get(BASE_URL)
    button = browser.find_element(By.ID, "submit-btn")
    assert button.text == "Отправить"


def test_valid_form_submission_shows_success(browser):
    browser.get(BASE_URL)
    browser.find_element(By.ID, "username").send_keys("Иван")
    browser.find_element(By.ID, "email").send_keys("ivan@mail.com")
    browser.find_element(By.ID, "submit-btn").click()

    success = browser.find_element(By.ID, "success-message")
    assert success.is_displayed()
    assert "успешно" in success.text.lower()


def test_invalid_form_submission_shows_error(browser):
    browser.get(BASE_URL)
    browser.find_element(By.ID, "username").send_keys("Иван")
    browser.find_element(By.ID, "email").send_keys("invalid-email")
    browser.find_element(By.ID, "submit-btn").click()

    error = browser.find_element(By.ID, "error-message")
    assert error.is_displayed()
