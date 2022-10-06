from selenium import webdriver
import sys
from time import sleep
from selenium.webdriver.common.by import By
# Next use this API:
"""
Chrome_driver (Old API)               Chrome_driver (New API)
find_element_by_id(‘id’)	        find_element(By.ID, ‘id’)
find_element_by_name(‘name’)	    find_element(By.NAME, ‘name’)
find_element_by_xpath(‘xpath’)	    find_element(By.XPATH, ‘xpath’)
"""
def test_lambdatest_todo_app():
    # chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    # connection chrome_driver
    chrome_driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')

    # get web url
    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    # max_view
    chrome_driver.maximize_window()

    # set click
    chrome_driver.find_element(By.NAME,"li1").click()
    chrome_driver.find_element(By.NAME,"li2").click()

    # set click
    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    # input in textbox
    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element(By.ID,"sampletodotext")
    email_text_field.send_keys(sample_text)

    # wait 5 second
    sleep(5)

    # set click
    chrome_driver.find_element(By.ID,"addbutton").click()
    sleep(5)

    # find textbox & input data
    output_str = chrome_driver.find_element(By.NAME,"li6").text
    sys.stderr.write(output_str)

    # sleep(2)
    # finish ./
    chrome_driver.close()

# run: pytest sample_test.py --verbose --capture=no