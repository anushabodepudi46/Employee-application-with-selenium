from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_add_employee():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # IMPORTANT: Replace with your VM IP
    driver.get("http://<VM-IP>:5000")

    # Enter employee name
    input_box = driver.find_element(By.NAME, "name")
    input_box.send_keys("John")

    # Click button
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    # Verify result
    assert "John" in driver.page_source

    driver.quit()
