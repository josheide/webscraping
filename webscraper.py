from bs4 import BeautifulSoup
from welcome_message import print_welcome_message
import requests
from urllib.parse import urlparse


class Webscraper:
    def __init__(self):
        self.scraped_data = []

    def get_user_input(self):
        while True:
            url = input("Please enter the website URL you want to scrape (or press Enter for default - index.hu): ")
            
            if not url: 
                return "https://index.hu/"
    
            parsed_url = urlparse(url)
            if parsed_url.scheme and parsed_url.netloc:
                return url
            else:
                print("Invalid URL. Please enter a valid URL.")
    
    def scrape_website(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        titles = doc.find_all('a')

        print("Scraped Titles and URLs:")
        for item in titles:
            title_text = item.get('title')
            url_text = item.get('href')

            if title_text and url_text:
                data_tuple = (title_text, url_text)
                self.scraped_data.append(data_tuple)  # Append the tuple to the list

                print("Title: " + title_text)
                print("URL: " + url_text)
                print(" ")
                
    def save_to_file(self):
        with open('scraped_data.txt', 'a', encoding='utf-8') as file:
            for data_tuple in self.scraped_data:
                file.write("Title: " + data_tuple[0] + '\n')
                file.write("URL: " + data_tuple[1] + '\n')
                file.write('\n')
                

class Articlescraper:
    def __init__(self):
        self.scraped_data = []

    def get_user_input(self):
        while True:
            url = input("Please enter the URL of the article you want to scrape: ")
            
            if not url: 
                print("Please try again!")
    
            parsed_url = urlparse(url)
            if parsed_url.scheme and parsed_url.netloc:
                return url
            else:
                print("Invalid URL. Please enter a valid URL.")
    
    def scrape_website(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        title = doc.find("h1").text.strip()  
        paragraphs = doc.find_all("p")
        
        content = "\n\n".join([p.text.strip() for p in paragraphs if p.text.strip()])  # Join non-empty paragraphs with two empty lines in between
                
        data_tuple = (title, content)
        self.scraped_data.append(data_tuple)

        print("Title:", title)
        print("Content:", content)
        print()

    def save_to_file(self):
        with open('scraped_articles.txt', 'a', encoding='utf-8') as file:
            for data_tuple in self.scraped_data:
                file.write("Title: " + data_tuple[0] + '\n')
                file.write("Content:\n" + data_tuple[1] + '\n')
                file.write('\n')


def main():
    print_welcome_message()
        
    while True:
        print("Please choose an option:")
        print("1. Scrape a website")
        print("2. Scrape an article")
        print("3. Quit")
        
        option = input("Enter your choice (1, 2, or 3): ")
        
        if option == "1":
            scraper = Webscraper()
            url = scraper.get_user_input()
            scraper.scrape_website(url)
            scraper.save_to_file()
        elif option == "2":
            scraper = Articlescraper()
            url = scraper.get_user_input()
            scraper.scrape_website(url)
            scraper.save_to_file()
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")
    
if __name__ == '__main__':
    main()
