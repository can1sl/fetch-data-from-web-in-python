import requests
from bs4 import BeautifulSoup

url = "https://www.rizetakip.com/tahminoyunu"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'html.parser')

# Find all unordered lists (ul) on the page
lists = soup.find_all("ul")

# Print only the content of <ul> and <li> elements
for index, lst in enumerate(lists):
    list_items = lst.find_all("li")
    print(f"List {index + 1} Items:")
    for item in list_items:
        print(item.text.strip())
    print()
