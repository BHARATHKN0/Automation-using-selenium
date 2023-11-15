import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

os.environ['PATH'] += r"C:/Users/bhara/Documents/drivers"
driver = webdriver.Chrome()

driver.get('https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm')
driver.implicitly_wait(10)

feet = driver.find_element(By.ID, 'height_feet')
inches = driver.find_element(By.ID, 'height_inches')
weight = driver.find_element(By.ID, 'your_weight')

feet.send_keys(6)
inches.send_keys(1)
weight.send_keys(130)

btn = driver.find_element(By.XPATH, '//input[@value="Compute BMI"]')
btn.click()

# WebDriverWait(driver, 30).until(
#     ec.text_to_be_present_in_element(
#         (By.ID, 'yourbmi'),  # Element filtration
#         'Your BMI'  # The expected text
#     )
# )
bmi_input = driver.find_element(By.ID, 'yourbmi')
bmi_value = bmi_input.get_attribute('value')

print('BMI:', bmi_value)
