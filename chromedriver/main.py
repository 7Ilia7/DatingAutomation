# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent

# url = "https://test2.ice.dating/"

user_agent_list = [
    "hello_world",
    "Best_of_the_best",
    "Dating_rehab"
]

useragent = UserAgent()


# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld^)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
options.add_argument(f"user-agent={random.choice(user_agent_list)}")
# options.add_argument(f"user-agent={useragent.opera}")

# set proxy
# options.add_argument("--proxy--server=138.128.91.65:8000")




driver = webdriver.Chrome(
    executable_path=r"D:\Репозитории\Selenium\chromedriver\chromedriver.exe",
    options=options
)
# r"D:\Репозитории\Selenium\firefoxdriver\geckodriver.exe" что бы не экранировать слешы
try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # time.sleep(5)
    # # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # # driver.get(url="https://test2.ice.dating/")
    # time.sleep(5)

    # driver.refresh()     #обновления страницы
    # driver.get_screenshot_as_file("1.png")   #сделать скрншот
    # time.sleep(10)
    # driver.save_screenshot("2.png")
    # driver.get(url="https://test2.ice.dating/")
    # time.sleep(2)

    driver.get("https://2ip.ua")
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
