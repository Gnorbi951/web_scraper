from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from filewriter import write_to_file
import time


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

    return [headline_text, headline_link]


if __name__ == "__main__":

    while True:
        try:
            write_to_file(getInformation())
        except:
            print("whupsie")
        time.sleep(300)
