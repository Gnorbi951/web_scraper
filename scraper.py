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
    main_news_html = page.find("article", {"class": "article-top-story"})

    main_title_tag = main_news_html.find("h1")
    main_title_text = str(main_title_tag)[4:-5]

    return main_title_text


if __name__ == "__main__":

    while True:
        try:
            write_to_file(getInformation())
        except Exception as e:
            print(e)
        time.sleep(300)
