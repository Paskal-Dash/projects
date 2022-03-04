import time
import os
import pickle
from target.login import *
import win32gui, win32con
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# os.chdir(os.path.dirname(os.path.abspath(__file__)))

def info_log(log):
    with open('log.txt', 'a+') as log_file:
        log_file.write(log)

def driver_connection():
    options = Options()
    # options.add_argument("--no-sandbox-and-elevated")
    # options.add_argument("--no-startup-window")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver

def check_login(day):
    driver = driver_connection()
    driver.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ru-ru")
    driver.implicitly_wait(15)

    login_step(driver)
    looting_step(driver, day)
    driver.close()

def looting_step(driver, day):
    driver.find_element(By.XPATH, f"//body/div/div/div/div/div/span[contains(text(), 'День {day}')]").click()
    t = datetime.today()
    log = f"{t.strftime('[%Y-%m-%d %H:%M:%S:%f]')} Я забрал награзу за день под номером {day}"
    info_log(log)
    time.sleep(10)

def login_step(driver):

    # # Вход в аккаунт
    # driver.find_element(By.CLASS_NAME, 'components-home-assets-__sign-header_---avatar---2Zo35h').click()
    # driver.find_element(By.XPATH, "//input[@placeholder='Имя пользователя/Адрес электронной почты']").send_keys(login)
    # driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys(password)
    # driver.find_element(By.CLASS_NAME, 'login-btn').click()
    
    # time.sleep(60)
    
    # # Cookies
    # pickle.dump(driver.get_cookies(), open("GenshinAuthorizationCookies", "wb"))

    time.sleep(5)

    for cookie in pickle.load(open("GenshinAuthorizationCookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(1)

if __name__ == '__main__':
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
    
    while True:
        t = datetime.today()
        future = datetime(t.year, t.month, t.day, 7, 0, 0)
        if t.hour >= 7:
            future += timedelta(days=1)
        time.sleep((future-t).total_seconds())
        check_login(future.day)
