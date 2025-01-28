from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd 
import os
import sys
from datetime import datetime   

# Website to scrape
website = "https://www.thesun.co.uk/sport/football/"

path = "/Users/mymac/Desktop/Automation with python/myenv/lib/python3.13/site-packages/chromedriver_autoinstaller/132/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service , options=options)
driver.get(website)
application_path= os.path.dirname(sys.executable)
now = datetime()
dateof = now.strftime("%m%d%y")

# Lists to store extracted data
titles = []
texts = []
links = []

# Find all elements containing the necessary data
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# Loop through each container to extract the data
for container in containers:
    try:
        header = container.find_element(by="xpath", value="./a/span").text
        text = container.find_element(by="xpath", value="./a/h3").text
        link = container.find_element(by="xpath", value="./a").get_attribute("href")
        titles.append(header)
        texts.append(text)
        links.append(link)
    except Exception as e:
        print(f"Error extracting data: {e}")

# Create a dictionary to map the data to column names
my_dict = {
    "titles": titles,
    "texts": texts,
    "links": links
}

# Convert the dictionary to a pandas DataFrame
df_elements = pd.DataFrame(my_dict)
filename = f'headlines-{dateof}.csv'
finalfile = os.path.join(application_path , filename)
df_elements.to_csv(finalfile )


driver.quit()

# use the corntab -e to create an automation with time and then give it the following example : 09*** /Users/mymac/Desktop/Automation\ with\ python/2.Web\ automation\ and\ Web\ Scraping/dist/creating_driver 

