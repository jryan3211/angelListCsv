from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time


print("This script will scrape information about startups from 'https://angel.co/companies' and place it into an aptly named csv file!")
url = input("Go to that site, select any filters you want to search by, and then input the new url here: \n")

print("\nPlease wait a max of 30 seconds...")

# open the webpage on chrome 
browser = webdriver.Chrome()
browser.get(url)

# wait for page to load
#browser.implicitly_wait(10) # doesnt work
time.sleep(3) # make sure page loads


# hit more until you cannot anymore 
count = 0 
while True: # max number of pages they'll let you search
	
	try:
		browser.find_element_by_css_selector('.more').click()
		time.sleep(3) # wait for additional startups to load
		#count = count + 1
	except:
		break

# getting results code
html = browser.page_source
soup = soup(html, 'html.parser')
containers = soup.find_all("div", {"class":"base startup"})
#print("Length after all pages loaded:", len(containers))

# creating a csv file and writing the headers

# make filename based on search filters
filters = soup.find("div", {"class":"currently-showing"})
filename = "angelList"

for f in filters: # append each filter
	filename = filename + "-" + f.text

filename = filename + ".csv"

fp = open(filename, "w")

headers = "Company, Location, Market, Website, Company Size, Stage\n" # column headers
fp.write(headers)

# loop through startups and add to csv
for container in containers:

	name_container = container.find_all("div", {"class":"name"})
	company_name = name_container[0].text.replace("\n", "").replace(",", " ")
	
	location_container = container.find_all("div", {"class":"column location"})
	location = location_container[0].text.replace("Location", "").replace("\n", "").replace(",", " ")

	market_container = container.find_all("div", {"class":"column market"})
	market = market_container[0].text.replace("Market", "").replace("\n", "").replace(",", " ")

	website_container = container.find_all("div", {"class":"column website"})
	website = website_container[0].text.replace("\n", "").replace("Website", "").replace(",", " ")

	companySize_container = container.find_all("div", {"class":"column company_size"})
	companySize = companySize_container[0].text.replace("\n", "").replace("Employees", "").replace(",", " ")
	companySize = companySize + " people"
	
	stage_container = container.find_all("div", {"class":"column stage"})
	stage = stage_container[0].text.replace("Stage", "").replace("\n", "").replace(",", " ")

	fp.write(company_name + "," + location + "," + market + "," + website + "," + companySize + "," + stage + "\n")

fp.close()
