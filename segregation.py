import requests
from bs4 import BeautifulSoup
from scraping_hh import get_headers, get_jobs_links, get_title_jobs, get_companies, get_salaries, get_towns


KEYWORDS = ("Django", "Flask")

# Выбираем вакансии с ключевыми словами в описании
def get_segregation() -> list:
    """
    Ф-ция возвращает список словарей подходящих вакансий.
    """
    jobs_links = get_jobs_links()
    lst = []
    for link in jobs_links:
        response = requests.get(link, headers=get_headers())
        html_data = response.text
        hh_main = BeautifulSoup(html_data, "lxml")
        
        job_description = hh_main.find("div", class_="g-user-content")
        if KEYWORDS[0] in job_description.text and KEYWORDS[1] in job_description.text:
            id = jobs_links.index(link)
            
            dct = {
                'title': get_title_jobs()[id],
                'link': get_jobs_links()[id],
                'money': get_salaries()[id].replace('\u202f', ''),
                'company': get_companies()[id],
                'city': get_towns()[id]
            }
            lst.append(dct)
                        
    return lst