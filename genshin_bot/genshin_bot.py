import time
import os
import pickle
from target.login import *
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def driver_connection():
    return webdriver.Chrome()

def check_login(driver):
    login_step(driver)
    looting_step(driver)

def looting_step(driver):

    while True:
        t = datetime.today()
        future = datetime(t.year, t.month, t.day, 7, 0, 0) + timedelta(days=1)
        time.sleep((future-t).total_seconds())
        driver.find_element(By.XPATH, f"//body/div/div/div/div/div/span[contains(text(), 'День {future.day}')]").click()

def login_step(driver):

    # # Вход в аккаунт
    # driver.find_element(By.CLASS_NAME, 'components-home-assets-__sign-header_---avatar---2Zo35h').click()
    # driver.find_element(By.XPATH, "//input[@placeholder='Имя пользователя/Адрес электронной почты']").send_keys(login)
    # driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys(password)
    # driver.find_element(By.CLASS_NAME, 'login-btn').click()
    #
    # time.sleep(30)
    #
    # # Cookies
    # pickle.dump(driver.get_cookies(), open("GenshinAuthorizationCookies", "wb"))

    time.sleep(5)

    for cookie in pickle.load(open("GenshinAuthorizationCookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(1)

if __name__ == '__main__':
    driver = driver_connection()
    driver.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ru-ru")
    driver.implicitly_wait(15)

    check_login(driver)

    driver.close()