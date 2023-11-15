import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


os.environ['PATH'] += r"C:/Users/bhara/Documents/drivers"
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(8)
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()

# progress_ele = driver.find_element(By.CLASS_NAME, 'progress-label')
# print(f"{progress_ele.text == 'completed!'}")

WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element filtration
        'Complete!'  # The expected text
    )
)
