from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import sys


# Clear terminal
os.system('cls')
print("Procedure starting")
time.sleep(1)

# Define Variables
countries = []
countries2 = []
failed = []
empty_lines = 0

# Setting parameters for selenium to work
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://mydhl.express.dhl/pk/en/home.html#/createNewShipmentTab')

# Read CSV File
DHLcsv = open('DHL.csv',"r")
reader = csv.reader(DHLcsv)
for row in reader:
    if not ''.join(row).strip():
        empty_lines += 1 
        continue
    countries.append([row[0], row[1], row[2], row[3], row[4]])
DHLcsv.close()

# Close Cookie Message
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/footer/div/div/div/button").click()

# Commands
for row in countries:
    try:
        Country = "/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div[1]/div/div[2]/form/div/div/div/ul/li[" +  row[1] + "]/a"
        City = row[2]
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/ul/li[2]/span[1]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div[1]/div/div[1]/form/div/div/div/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div[1]/div/div[1]/form/div/div/div/ul/li[159]/a").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div[1]/div/div[2]/form/div/div/div/input").click()
        driver.find_element_by_xpath(Country).click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div[1]/div/fieldset/div[2]/form[1]/div/label/span/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div[1]/div/fieldset/div[2]/form[1]/div/label/span/input").send_keys("Karachi")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div[1]/div/fieldset/div[2]/form[1]/div/label/span/ul/li[35]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[4]/div/div/fieldset/div[2]/form[1]/div/label/span/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[4]/div/div/fieldset/div[2]/form[1]/div/label/span/input").send_keys(City)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[4]/div/div/fieldset/div[2]/form[1]/div/label/span/ul/li[1]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/form/footer/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/fieldset/div[3]/div/div[1]/input").send_keys("30")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/fieldset/div[3]/div/div[2]/input").send_keys("30")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/fieldset/div[3]/div/div[3]/input").send_keys("18")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/fieldset/div[2]/div/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/fieldset/div[2]/div/div/input").send_keys(row[3])
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        troublesome = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/form/footer/button")#.click()
        driver.execute_script("arguments[0].click();",troublesome)
        time.sleep(5)
        # Formatting
        try:
            edit = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[3]/form/div/div/div[1]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div/div[3]/div/span").text
        except:
            try:
                edit = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[3]/form/div/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/span").text
            except:
                sys.exit(1)
        edit = edit.split(".", 1)[0]
        row[4] = edit.replace(",",".")
        # Append
        countries2.append([row[0], row[1], row[2], row[3], row[4]])
        # Reload
        driver.get('https://mydhl.express.dhl/pk/en/home.html#/createNewShipmentTab')
    except:
        failed.append(countries)
        pass


# Write CSV File
DHLcsvs = open('DHL.csv', "w", newline='')
writer = csv.writer(DHLcsvs)
for row in countries2:
    writer.writerow([row[0], row[1], row[2], row[3], row[4]])
DHLcsvs.close()

# Done
driver.quit()
if len(failed) > 0:
        print("%s cases have failed" % len(failed))
else:
    print("Procedure concluded")
    print("Opening file in excel")
time.sleep(5)
currentDirectory = os.getcwd()
currentDirectory = currentDirectory + r"\DHL.csv"
os.startfile(currentDirectory)