from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "http://localhost:5000"


def test_register():
  driver = webdriver.Chrome()
  driver.get(f'{base_url}/register')
  name_field = driver.find_element(By.NAME, 'name')
  email_field = driver.find_element(By.NAME, 'email')
  password_field = driver.find_element(By.NAME, 'password')
  name_field.send_keys('John Doen')
  email_field.send_keys('JohnDoen@gmail.com')
  password_field.send_keys('12345')
  
  submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
  submit_button.click()
  
  WebDriverWait(driver, 10)
  driver.quit() 
  
  