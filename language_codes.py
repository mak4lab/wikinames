from requests import get
from bs4 import BeautifulSoup

html = get("https://www.wikidata.org/wiki/Help:Wikimedia_language_codes/lists/all").text
soup = BeautifulSoup(html)

table_rows = soup.select("table tbody tr")
language_codes = [row.td.string.strip() for row in table_rows if row.td and row.td.string]
print("language_codes:", language_codes)
