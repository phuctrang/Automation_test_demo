from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_My_Site():
    chrome_driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    chrome_driver.get('https://phuctrang.github.io/myProfile/')
    chrome_driver.maximize_window()

    """
    # case dupicate class (button)
    <a href="https://beacons.ai/phuctrang" class="button">
        <i class="fas fa-user-check"></i> MY SITE
    </a>
    <a href="https://www.facebook.com/trang.hophuc.77/" class="button">
        <i class="fab fa-facebook-square"></i> FACEBOOK
    </a>
    """
    chrome_driver.find_element(By.XPATH, '//*[@class="button"]//*[@class="fab fa-facebook-square"]').click()

    # Facebook: login button fail
    # chrome_driver.find_element(By.XPATH, '//form[@class="x1i10hfl x9f619 xggy1nq x1s07b3s"]//*[@id="login_form"]').click()
    sleep(10)
    chrome_driver.close()

