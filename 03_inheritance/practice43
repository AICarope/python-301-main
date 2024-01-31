import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
print(soup.prettify())