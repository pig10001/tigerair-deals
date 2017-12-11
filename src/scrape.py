from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://www.tigerair.com.au/deals"
driver.get(url)
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
divs = soup.find_all('div', class_="special-deal-item")

for div in divs:
	attributes = div.find("a").attrs
	print attributes['data-origin'] + " to " + attributes['data-destination']
