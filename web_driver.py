from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from email_handler import send_email

# -------------- DRIVER SETUP -------------- #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

attempts = 0


def check_price() -> float:
    driver.get("https://www.udemy.com/course/python-django-the-practical-guide/?couponCode=KEEPLEARNING")
    try:
        wait.until(ec.presence_of_element_located(
            (By.CLASS_NAME, "base-price-text-module--container--Sfv-5.ud-clp-price-text")))
        element = driver.find_element(By.CLASS_NAME, "base-price-text-module--container--Sfv-5.ud-clp-price-text")
        price = element.text

        if price:
            price = price[(price.find("$") + 1):]
            return float(price)
        else:
            global attempts
            if attempts <= 3:
                check_price()
                attempts += 1

    except NoSuchElementException:
        print("No such element")


cur_price = check_price()
driver.quit()

print("Driver successfully fetched the price.")

if cur_price < 100:
    send_email(cur_price)
