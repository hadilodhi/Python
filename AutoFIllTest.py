from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
os.system('cls')

# using Pandas to read the csv file
source_information = pd.read_csv('my_file.csv')
print(source_information)

# setting the URL for BeautifulSoup to operate in
url = "http://www.stealmylogin.com/demo.html"
my_web_form = get(url).content
soup = BeautifulSoup(my_web_form, 'html.parser')

# Setting parameters for selenium to work
path = r'C:/Users/Hadi Lodhi/Desktop/Python/chromedriver.exe' #make sure you insert the path to your driver here!
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(path, options=options)
driver.get(url)

# creating a procedure to fill the form
def fulfill_form(username, user_email):
    # use Chrome Dev Tools to find the names or IDs for the fields in the form
    input_customer_name = driver.find_element_by_name('username')
    input_customer_email = driver.find_element_by_name('password')
    #submit = driver.find_element_by_name('login')
    submit = driver.find_element_by_xpath("//input[@type='submit' and @value='login']")

    #input the values and hold a bit for the next action
    input_customer_name.send_keys(username)
    time.sleep(1)
    input_customer_email.send_keys(user_email)
    time.sleep(1)
    submit.click()
    time.sleep(7)


# creating a list to hold any entries should them result in error
failed_attempts = []


# creating a loop to do the procedure and append failed cases to the list
for customer in source_information:
    try:
        fulfill_form(source_information['username'], source_information['user_email'])
    except:
        failed_attempts.append(source_information['username'])
        pass

if len(failed_attempts) > 0:
    print("%s cases have failed" % len(failed_attempts))

print("Procedure concluded")