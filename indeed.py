import requests
from bs4 import BeautifulSoup

BASE_URL = f"https://www.indeed.com"

def _extract_last_page_num(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", {"aria-label": "pagination"})

    if not div:
        return 1 # If pagination is not found, assume there's 1 page

    lis = div.find_all("li")
    page_numbers = []

    for li in lis:
        try:
            page = int(li.text.strip())
            page_numbers.append(page)
        except ValueError:
            continue

    return max(page_numbers) if page_numbers else 1

def _extract_jobs_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("a", {"class": "tapItem"})

    jobs = []
    for card in job_cards:
        title = card.find("h2", {"class": "jobTitle"}).text.strip()
        company = card.find("span", {"class": "companyName"}).text.strip()
        location = card.find("div", {"class": "companyLocation"}).text.strip()
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
        })

    return jobs
    

def get_jobs(search_term):


    url = BASE_URL + f"/jobs?q+={search_term}"