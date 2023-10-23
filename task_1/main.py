import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import re
import pytest
@dataclass
class Wiki_Data:
    Websites: str
    Popularity: int
    Front_end: str
    Back_end: str
    Database: str

result = []
@pytest.fixture
def data_extraction():

    URL = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
    wiki_link = requests.get(URL).text
    soup = BeautifulSoup(wiki_link, 'html.parser')

    data = soup.find('table', class_="wikitable")
    res = data.find_all('tr')[1:]

    for i in res:
        rows = i.find_all('td')

        Websites = re.search(r'^\w+',rows[0].text).group()
        Popularity = int(re.search(r'^\w+',rows[1].text.replace(',', '').replace('.', '')).group())
        Front_end = rows[2].text.rstrip('\n')
        Back_end = re.sub(r'\[\d+]', '', rows[3].text.rstrip('\n'))
        Database = re.sub(r'\[\d+]', '', rows[4].text.rstrip('\n'))

        result.append(Wiki_Data(Websites, Popularity, Front_end, Back_end, Database))
    return result