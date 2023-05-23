from bs4 import BeautifulSoup
import requests

print("Welcome to my Web Scraper!")

while True:
    url = input("Please enter the website URL you want to scrape (or press Enter for default - index.hu): ")

    if not url:
        url = "https://index.hu/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    titles = doc.find_all('h1') + doc.find_all('h2')

    print("Scraped Titles:")
    for item in titles:
        title_text = item.text.strip()
        print(" - " + item.text.strip())
        
        with open('scraped_titles.txt', 'a', encoding='utf-8') as file:
            file.write(" - " + title_text + '\n')

    user_input = input("Do you want to scrape another website? (yes/no): ")
    if user_input.lower() != "yes":
        break
    