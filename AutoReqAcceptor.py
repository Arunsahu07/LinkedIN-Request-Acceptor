import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager





options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
# sleep(5)
try:
    userid = '' # enter your id
    password = '' # enter your password
    checklink = driver.find_element_by_class_name("sign-in-form__form-input-container")
    driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(userid)
    driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
    sleep(2)
    
except:
    print("CAN'T SIGNIN")


# for accepting the connection requests
try:
    driver.get("https://www.linkedin.com/mynetwork/")
    sleep(2)
    invite = driver.find_element_by_class_name("mn-invitation-list")
    while invite:
        invite.find_element_by_class_name("artdeco-button--secondary").click()
        sleep(2)
        invite = driver.find_element_by_class_name("mn-invitation-list")
        
except Exception as e:
    print("Error-",e)


driver.close()


