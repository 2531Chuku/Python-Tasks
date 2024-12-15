import requests
from bs4 import BeautifulSoup


def webScraper(url):
    try:
        sendRequest(url)
    except requests.exceptions.RequestException as e:
        print(f"Sorry there was an error fetching data from the website: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def sendRequest(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')
    results(articles)

    

def results(articles):
    print("________________Extracted Articles:_____________________________")
    for index, article in enumerate(articles, start=1):
        title = article.get_text(strip=True)
        link = article.find('a')['href'] if article.find('a') else 'No link available'
        print(f"{index}. Title: {title}\n   Link: {link}")
        print("-------------------------------------------------------")

url = input("Enter the website URL: ")
webScraper(url)


# Test Case : please use this url : https://webscraper.io/test-sites