from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def find_element(driver, by, value, timeout=10):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((by, value))
    )

def test_language_toggle():
    driver.get("https://flip.id/")
    toggle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "toggle-language"))
    )
    toggle_button.click()
    time.sleep(2)

    # Assert that the page displays "Free financial transactions, to anyone"
    expected_text = "Free financial transactions, to anyone."
    actual_text = driver.find_element(By.CLASS_NAME, "chakra-heading").text
    assert expected_text == actual_text, f"Expected: {expected_text}, but got: {actual_text}"
    print("Test passed: The correct text is displayed.")

def test_cellular_providers():
    driver.get("https://flip.id/")

    # Scroll to the FAQ section
    faq_section = driver.find_element(By.CSS_SELECTOR, '.css-3pdxiz')
    driver.execute_script("arguments[0].scrollIntoView();", faq_section)

    # Click the specified question using its data-index
    question_data_index = "4"  # Update this with the correct data-index of the desired question
    question_xpath = f"//button[@data-index='{question_data_index}']/h3"

    # Re-find the question element before clicking
    question = find_element(driver, By.XPATH, question_xpath)
    question.click()

    # Check if Telkomsel, Indosat Ooredoo, and XL are mentioned in the answer
    answer = find_element(driver, By.ID, 'accordion-panel-Adakah layanan pembelian pulsa, paket data serta PPOB di Flip?').text
    required_providers = ["Telkomsel", "Indosat Ooredoo", "XL"]

    for provider in required_providers:
        assert provider in answer, f"{provider} not found in the answer."
        print("Test passed: The correct providers is displayed.")

def test_money_transfer_simulation():
    driver.get("https://flip.id/")

    # Find all elements with the specified CSS selector
    buttons = driver.find_elements(By.CSS_SELECTOR, '.chakra-button.css-os5e35')

    buttons[3].click()
    time.sleep(5)

    button = driver.find_element(By.CSS_SELECTOR, '.css-1l1pwnu')
    button.click()
    print("Clicked currency button.")
    time.sleep(5)

    input_box = driver.find_element(By.CSS_SELECTOR, '.chakra-input.css-4gru8k')
    input_box.send_keys('gbp')

    time.sleep(5)

    gbp_element = driver.find_element(By.CSS_SELECTOR, ".css-1i33ipy")
    gbp_element.click()
    print("Clicked the United Kingdom (GBP) element.")

    time.sleep(5)

    idr_box = driver.find_element(By.CSS_SELECTOR, '.css-19t8ja4')
    idr_box.send_keys('100000')
    
    time.sleep(5)

if __name__ == "__main__":
    driver = webdriver.Chrome() 

    try:
        # Run the tests
        test_language_toggle()
        test_cellular_providers()
        test_money_transfer_simulation()
    finally:
        # Close the browser
        driver.quit()
