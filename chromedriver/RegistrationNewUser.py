import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import bible

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")


driver = webdriver.Chrome(
    executable_path=r"D:\Ice Dating\automation\chromedriver\chromedriver.exe",
    options=options
)

try:
    driver.get("https://front-stage.ice.dating/profile")
    element = driver.find_element(By.CSS_SELECTOR,
        '#root > div > div > div > div.mainPage__main > div > div > div.registrationStepFirst__genderSelection > div > div.registrationStepFirst__genderMale > p')
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.CSS_SELECTOR,
        "#root > div > div > div > div.mainPage__main > div > div > div > div.registrationStepSecond__formInput > input.registrationStepSecond__form__inputName").send_keys(
        "Anus")
    driver.get_screenshot_as_file("1.png")

    element = driver.find_element(By.CSS_SELECTOR,
        '#root > div > div > div > div.mainPage__main > div > div > div > div.registrationStepSecond__formInput > div.registrationStepSecond__formBirthday > div > div > div > input[type=text]')
    driver.execute_script("arguments[0].click();", element)

    select = Select(driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select'))
    select.select_by_value('1990')

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[5]')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[2]/input')
    driver.execute_script("arguments[0].click();", element)
    element.send_keys("Odessa")
    time.sleep(3)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[2]/div/div[2]')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/input[2]')
    driver.execute_script("arguments[0].click();", element)
    element.send_keys(regLogin)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/input[3]')
    driver.execute_script("arguments[0].click();", element)
    element.send_keys("121339121qq")

    # element = driver.find_elements(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/button')
    # driver.execute_script("arguments[0].click();", element)






    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()