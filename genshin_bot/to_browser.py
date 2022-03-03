import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(15)
# driver.close()


# curr_datetime = datetime.today()
# date = curr_datetime.day
# time = curr_datetime.time().strftime("%H %M").split() #[0] - час, [1] - минуты

driver = webdriver.Chrome()
driver.get("https://vk.com/login?u=2&to=/index.php")
driver.implicitly_wait(10)

login = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
checkbox = driver.find_element(By.ID, "expire")

login.send_keys("89024862116")
password.send_keys("PASSWORD")
checkbox.click()

login.send_keys(Keys.RETURN)
time.sleep(15)

driver.close()