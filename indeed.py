import requests
from bs4 import BeautifulSoup

BASE_URL = f"https://www.indeed.com"

def _extract_last_page_num(url):
    """Get the last page number
    :param url: str
    :return: int
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", {"class": "pagination"})

    lis = div.find_all("li")
    for li in lis:
        child = li.findChild()
        print(child)

def get_jobs(search_term):
    """Extract jobs until the last page
    :param search_term: str
    :return: list[dict[str, str]]
    """

    url = BASE_URL + f"/jobs?q+={search_term}"
