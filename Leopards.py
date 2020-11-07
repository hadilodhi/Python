from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import os


# Clear terminal
os.system('cls')

# Setting parameters for selenium to work
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://leopardscourier.com/pk/services/rate-calculator/')

# Read CSV File
leopardscsv = open('Leopards.csv',"r")
reader = csv.reader(leopardscsv)
countries = []
failed = []
for row in reader:
    countries.append([row [0], row[1]])
# Close Cookie Message
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[2]/span/a[2]").click()

# Commands
for row in countries:
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/select/option[3]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/div[2]/span/span[1]/span/span[1]").click()
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("INTERNATIONAL XPS")
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/div[3]/span/span[1]/span/span[1]").click()
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Karachi")
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/div[4]/div/span/span[1]/span/span[1]").click()
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(row[0])
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
        driver.find_element_by_id("Weight").clear()
        driver.find_element_by_id("Weight").send_keys(row[1])
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        #Guess = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/span").text
        #print("Price: ")
        driver.get('https://leopardscourier.com/pk/services/rate-calculator/')
    except:
        failed.append(countries)
        pass


driver.quit()
if len(failed) > 0:
        print("%s cases have failed" % len(failed))
else:
    print("Procedure concluded")