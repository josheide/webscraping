from bs4 import BeautifulSoup
import requests

url = "https://index.hu/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

titles = doc.find_all('h1') + doc.find_all('h2')

for title in titles:
    print("- " + title.text.strip())
    print()