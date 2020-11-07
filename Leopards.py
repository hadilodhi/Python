from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

# Clear terminal
os.system('cls')

# Define Variables
countries = []
countries2 = []
failed = []
empty_lines = 0

# Setting parameters for selenium to work
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://leopardscourier.com/pk/services/rate-calculator/')

# Read CSV File
leopardscsv = open('Leopards.csv', "r")
reader = csv.reader(leopardscsv)
for row in reader:
    if not ''.join(row).strip():
        empty_lines += 1 
        continue
    countries.append([row [0], row[1], row[2]])
leopardscsv.close()

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
        edit = driver.find_element_by_class_name("demo-container").text
        edit = edit.replace("AMOUNT: ","")
        edit = edit.replace(" PKR","")
        edit = edit.split(".", 1)[0]
        row[2] = edit.replace(",",".")
        countries2.append([row [0], row[1], row[2]])
        driver.get('https://leopardscourier.com/pk/services/rate-calculator/')
    except:
        failed.append(countries)
        pass

#Write CSV File
leopardscsvs = open('Leopards.csv', "w", newline='')
writer = csv.writer(leopardscsvs)
for row in countries2:
    writer.writerow([row [0], row[1], row[2]])
leopardscsvs.close()

#Done
driver.quit()
if len(failed) > 0:
        print("%s cases have failed" % len(failed))
else:
    print("Procedure concluded")