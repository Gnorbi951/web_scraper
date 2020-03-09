from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getInformation():
    url = "https://www.origo.hu/index.html"

    # Read the whole page
    uClient = uReq(url)
    page_response = uClient.read()
    uClient.close()

    # Parse html
    page = soup(page_response, "html.parser")

    # Find the divs I'm looking for
    main_news_html = page.find("div", {"class": "news-text-block"})

    headline = main_news_html.find("a", {"class": "news-title"})
    headline_text = headline['title']
    headline_link = headline['href']

    print(headline_link)
    print(headline_text)

getInformation()