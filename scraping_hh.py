import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from time import sleep


URL = "https://spb.hh.ru/search/vacancy?area=1&area=2&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&only_with_salary=true&text=python"

def get_headers()-> dict:
    """
    Ф-ция возвращает словарь - фейковый заголовок браузера.
    """
    return Headers(browser="firefox", os="win").generate()

def get_response_text() -> str:
    """
    Ф-ция возвращает строковый ответ на запрос к сайту
    """
    return requests.get(URL, headers=get_headers()).text

def get_bs_object()-> object:
    """
    Ф-ция возвращает объект BeautifulSoup.
    """
    return BeautifulSoup(get_response_text(), "lxml")

def get_title_jobs() -> list:
    """
    Функция возвращает список наименований первых ("свежих") 20-ти вакансий сайта hh.ru.
    """
    titles_list = []
    hh_main = get_bs_object()
    job_names = hh_main.find_all("a", class_="serp-item__title")
    for job in job_names:
        titles_list.append(job.text)
    return titles_list

def get_jobs_links() -> list:
    """
    Ф-ция возвращает список ссылок на вакансии.
    """
    links_list = []
    hh_main = get_bs_object()
    links = hh_main.find_all("a", class_="serp-item__title")
    for link in links:
        links_list.append(link.get('href'))
        sleep(1)
    return links_list

def get_salaries() -> list:
    """
    Ф-ция возвращает список "вилок" зарплат.
    """
    salaris_list = []
    hh_main = get_bs_object()
    salaris = hh_main.find_all("span", class_="bloko-header-section-2")
    for salary in salaris:
        salaris_list.append(salary.text)
    return salaris_list

def get_towns() -> list:
    """
    Ф-ция возвращает список городов (Москва и/или С.-Петербург) расположения вакансий.
    """
    towns_list = []
    hh_main = get_bs_object()
    town_names = hh_main.find_all("div", class_="bloko-text")
    for town in town_names:
        if 'Москва' in town.text:
            towns_list.append(town.text[:6])
        elif 'Санкт-Петербург' in town.text:
            towns_list.append(town.text[:15])
    return towns_list

def get_companies() -> list:
    """
    Ф-ция возвращает список компаний.
    """
    companis_list = []
    hh_main = get_bs_object()
    companis_names = hh_main.find_all("a", class_="bloko-link bloko-link_kind-tertiary")
    for company in companis_names:
        companis_list.append(company.text)
    return companis_list