from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but1=browser.find_element(By.CSS_SELECTOR,"button.btn.btn-primary")
    but1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    answer=y

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)
    
      
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

 
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
