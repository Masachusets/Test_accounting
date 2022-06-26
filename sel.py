from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def enter_to_yandex(login, password):
    driver = webdriver.Chrome()
    url = 'https://passport.yandex.ru/auth/'
    driver.get(url)

    login_id = driver.find_element(By.ID, 'passp-field-login')
    login_id.clear()
    login_id.send_keys(login)

    button = driver.find_element(By.ID, 'passp:sign-in')
    button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "passp-field-passwd")))

        password_id = driver.find_element(By.ID, 'passp-field-passwd')
        password_id.clear()
        password_id.send_keys(password)

        button = driver.find_element(By.ID, 'passp:sign-in')
        button.click()
        return 'Done'
    except:
        driver.close()
        return 'Error'
