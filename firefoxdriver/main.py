from selenium import webdriver
import time

url = "https://test2.ice.dating/"
driver = webdriver.Firefox(executable_path=r"D:\Репозитории\Selenium\firefoxdriver\geckodriver.exe")


try:
    driver.get(url=url)
    driver.save_screenshot("2.png")
    time.sleep(5)
    # driver.get(url="https://test2.ice.dating/")
    # time.sleep(5)

    # driver.refresh()     #обновления страницы
    # driver.get_screenshot_as_file("1.png")   #сделать скрншот
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # driver.get(url="https://test2.ice.dating/")
    # time.sleep(2)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()