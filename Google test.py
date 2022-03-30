from logging import exception
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from os.path import dirname, abspath

url = 'https://www.google.com/'

try: 

    default_sleep = 3
    
    #chromeDriver path
    d = (dirname(abspath(__file__)))
    chrome_driver = d + "\\chromedriver.exe"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    
    driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=options)
    driver.implicitly_wait(3.0)
    driver.maximize_window()

    #open chrome to the specified URL
    driver.get(url)
    sleep(default_sleep)

    #click on search field and enter search text
    searchText = "RTS Labs";
    driver.find_element_by_css_selector(".gLFyf").send_keys(searchText)
    sleep(default_sleep)
    
    #press enter
    driver.find_element_by_css_selector(".gLFyf").send_keys(Keys.ENTER)
    sleep(default_sleep)

    #select first item
    driver.find_element_by_css_selector("div:nth-child(2) > .tF2Cxc > .yuRUbf .LC20lb").click()
    sleep(default_sleep)

    #close browser
    driver.quit()
    

except exception as e:
    print(e)
    driver.quit()

