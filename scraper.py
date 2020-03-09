import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.arukereso.hu/videokartya-c3142/"

uClient = uReq(url)
page_response = uClient.read()
print(page_response)
uClient.close()