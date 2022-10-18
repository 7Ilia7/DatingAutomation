import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")


driver = webdriver.Chrome(
    executable_path=r"D:\Ice Dating\automation\chromedriver\chromedriver.exe",
    options=options
)

try:
    driver.get("https://front-stage.ice.dating")
    # element = driver.find_element(By.CSS_SELECTOR,
    #     '#root > div > div > div > div.mainPage__main > div > div > div.registrationStepFirst__genderSelection > div > div.registrationStepFirst__genderMale > p')
    # driver.execute_script("arguments[0].click();", element)
    # driver.maximize_window()
    # driver.find_element(By.CSS_SELECTOR,
    #     "#root > div > div > div > div.mainPage__main > div > div > div > div.registrationStepSecond__formInput > input.registrationStepSecond__form__inputName").send_keys(
    #     "Anus")
    # time.sleep(10)
    #
    # element = driver.find_element(By.CSS_SELECTOR,
    #     '#root > div > div > div > div.mainPage__main > div > div > div > div.registrationStepSecond__formInput > div.registrationStepSecond__formBirthday > div > div > div > input[type=text]')
    # driver.execute_script("arguments[0].click();", element)
    #
    # select = Select(driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select'))
    # select.select_by_value('1990')
    #
    # element = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[5]')
    # driver.execute_script("arguments[0].click();", element)
    #
    # element = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[2]/input')
    # driver.execute_script("arguments[0].click();", element)
    # element.send_keys("Odessa")
    # time.sleep(3)
    #
    # element = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/div[2]/div/div[2]')
    # driver.execute_script("arguments[0].click();", element)
    #
    # element = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/input[2]')
    # driver.execute_script("arguments[0].click();", element)
    # element.send_keys("greeench707@gmail.com")
    #
    # element = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div/div/div/div[3]/div/div/div/div[1]/input[3]')
    # driver.execute_script("arguments[0].click();", element)
    # element.send_keys("121339121qq")
    #
    # element = driver.find_element(By.CSS_SELECTOR,
    #      '#root > div > div > div > div.mainPage__main > div > div > div > button')
    # driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[1]/div[3]')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div[1]/input')
    driver.execute_script("arguments[0].click();", element)
    element.send_keys("greench707@gmail.com")

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/div[2]/span/input')
    driver.execute_script("arguments[0].click();", element)
    element.send_keys("121339121qq")

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div/div/div/div[3]/div/div/button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[1]/div/div[3]/div[1]/span/div/img')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[1]/div/div[5]/ul/li[3]/div/div')
    driver.execute_script("arguments[0].click();", element)


    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[4]/div/div[1]/div/div')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="locationSelector"]')
    driver.execute_script("arguments[0].click();", element)
    element.clear()
    element.send_keys("Odessa")
    time.sleep(2)

    element = driver.find_element(By.XPATH,
        '//*[@id="simple-popover"]/div[3]/div/form/div[3]/div/div[3]')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element(By.XPATH,
        '//*[@id="simple-popover"]/div[3]/div/form/div[8]/button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[4]/div/div[1]/div/div')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    element = driver.find_element(By.XPATH,
        '//*[@id="simple-popover"]/div[3]/div/form/div[1]/div[1]/label/p')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    element = driver.find_element(By.XPATH,
        '//*[@id="simple-popover"]/div[3]/div/form/div[4]/p[2]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)


    element = driver.find_element(By.XPATH,
        '//*[@id="simple-popover"]/div[3]/div/form/div[8]/button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[4]/div/div[1]/div/div')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    # element = driver.find_element(By.CSS_SELECTOR,
    #     '#simple-popover > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-j04zx8 > div > form > div.radius.filters__item > div > span > span.MuiSlider-thumbColorPrimary.MuiSlider-thumbSizeMedium.MuiSlider-thumb.css-r69ln3 > input')
    # driver.execute_script("arguments[0].click();", element)
    # element.send_keys("44")
    # time.sleep(3)

    slidersDistance = driver.find_elements(By.CSS_SELECTOR,
    '#simple-popover > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-j04zx8 > div > form > div.radius.filters__item > div > span > span.MuiSlider-thumbColorPrimary.MuiSlider-thumbSizeMedium.MuiSlider-thumb.css-r69ln3')  # Selecting all sliders
    left_slider = slidersDistance[0]
    # right_slider = sliders[1]
    move = ActionChains(driver)
    # Moving the left slider
    move.click_and_hold(left_slider).move_by_offset(-220, 0).release().perform()
    # Moving the right slider
    # move.click_and_hold(right_slider).move_by_offset(-28, 0).release().perform()

    slidersAge = driver.find_elements(By.CSS_SELECTOR,
    '#simple-popover > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-j04zx8 > div > form > div.age.filters__item > div > span > span:nth-child(4)')  # Selecting all sliders
    left_slider = slidersAge[0]
    # right_slider = sliders[1]
    move = ActionChains(driver)
    # Moving the left slider
    move.click_and_hold(left_slider).move_by_offset(-50, 0).release().perform()
    # Moving the right slider
    # move.click_and_hold(right_slider).move_by_offset(-28, 0).release().perform()

    slidersHeight = driver.find_elements(By.CSS_SELECTOR,
    '#simple-popover > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-j04zx8 > div > form > div.height.filters__item > div > span > span:nth-child(4)')  # Selecting all sliders
    left_slider = slidersHeight[0]
    # right_slider = sliders[1]
    move = ActionChains(driver)
    # Moving the left slider
    move.click_and_hold(left_slider).move_by_offset(-50, 0).release().perform()
    # Moving the right slider
    # move.click_and_hold(right_slider).move_by_offset(-28, 0).release().perform()

    slidersWeight = driver.find_elements(By.CSS_SELECTOR,
    '#simple-popover > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-j04zx8 > div > form > div.weight.filters__item > div > span > span.MuiSlider-track.css-43iyhz')  # Selecting all sliders
    left_slider = slidersWeight[0]
    # right_slider = sliders[1]
    move = ActionChains(driver)
    # Moving the left slider
    move.click_and_hold(left_slider).move_by_offset(200, 0).release().perform()
    # Moving the right slider
    # move.click_and_hold(right_slider).move_by_offset(-28, 0).release().perform()

    element = driver.find_element(By.XPATH,
        '//*[@id="root"]/div[2]/div[1]/div[4]/div/div[2]/div[2]/div')
    driver.execute_script("arguments[0].click();", element)





    # element = driver.find_element(By.XPATH,
    #     '//*[@id="simple-popover"]/div[3]/div/form/div[8]/button')
    # driver.execute_script("arguments[0].click();", element)































    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()