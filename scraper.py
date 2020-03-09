import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.arukereso.hu/videokartya-c3142/"

# Read the whole page
uClient = uReq(url)
page_response = uClient.read()
uClient.close()

# Parse html
page = soup(page_response, "html.parser")

# Find the divs I'm looking for
elements = page.findAll("div", {"class": "product-box-container"})

print(len(elements))