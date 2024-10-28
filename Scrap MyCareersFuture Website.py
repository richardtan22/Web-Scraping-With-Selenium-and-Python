#!/usr/bin/env python
# coding: utf-8

# In[28]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files\\Google\\chromedriver.exe"
service = Service(PATH)

# Initialize the Chrome WebDriver with the service
web = webdriver.Chrome(service=service)

# MyCareersFuture websit
url = 'https://www.mycareersfuture.gov.sg/'

# open Chrome and navigate to the Web Page
web.get(url)

# Enter "Data Engineer" in the search box on the web page and press Enter
search_box = web.find_element('xpath', '//*[@id="search-text"]')
search_box.send_keys('Data Engineer')
search_box.send_keys(Keys.RETURN)

# wait for 5 seconds, until page gets fully loaded
WebDriverWait(web, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-list")))
#time.sleep(5)

element_list = []
next_pg = True
while next_pg:
    results = web.find_elements(By.CLASS_NAME, "pl2-l")
    for i in results:
        title = i.find_elements(By.CLASS_NAME, "JobCard__jobtitle___3HqOw")
        link = i.find_elements(By.CSS_SELECTOR, "a[href*='/job/']")
        for i in range(len(title)):
            element_list.append([title[i].text, link[i].get_attribute("href")])
     
    # Click next button if it is still available
    try:
        next_button = web.find_element(By.XPATH, "//*[contains(@aria-label, 'Next')]")
        next_button.click()
        time.sleep(2)
    except:
        #print("This is the last page.")
        next_pg = False
        web.quit()
        
# Print the results
for element in element_list:
    print(f'Title: {element[0]}, Link: {element[1]}')

