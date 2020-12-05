# Import Dependencies
import pymongo
import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from splinter import Browser
from urllib.parse import urljoin

# Set path to browser & start splinter
browser = Browser('chrome')
url = 'http://quotes.toscrape.com/'

html = browser.html
soup_obj = soup(html, 'html.parser')


def get_quote(soup_obj):
    data = {}
    data['text'] = soup_obj.find("span", class_ = "text").text
    data['author'] = soup_obj.find("small", class_ = "author").text
    link = soup_obj.a['href']
    author_url = urljoin(url, link)
    data['author'] = get_author_info(author_url)
    data['tags'] = get_tags(soup_obj)
    return data


def get_author_info(url):
    author_info = {}
    response = requests.get(url)
    soup1 =  soup(response.text, 'lxml') 
    author_info['name'] = soup1.find('h3', class_="author-title").text.strip()   
    author_info['born'] = soup1.find('span', class_="author-born-date").text.strip()
    author_info['location'] = soup1.find('span', class_="author-born-location").text.strip()
    author_info['description'] = soup1.find('div', class_="author-description").text.strip()
    return author_info


def get_tags(soup_obj):
    tags_list = []
    for tag in soup_obj.findAll("a", class_ = "tag"):
        tags_list.append(tag.text) 
    return tags_list

def all_quotes(page_number):
    quote_list = []
    html = browser.html
    soup_obj = soup(html, 'html.parser')
    quote_block = soup_obj.findAll("div", class_="quote")
    num_quote = 10
    quote_id = (page_number -1)  * num_quote 
    for block in quote_block:
        quote_id = quote_id +1
        quote = get_quote(block)
        quote['id'] = quote_id
        quote_list.append(quote) 
    return quote_list

def scrape_all(url):

    page_number = 0
    final_quotes = []

    for x in range(1,11):
        page_number = page_number +1
        browser.visit(f'http://quotes.toscrape.com/page/{x}/')
        html = browser.html
        soup_obj = soup(html, 'html.parser')

        current_quotes = all_quotes(page_number)
        final_quotes = final_quotes + current_quotes
    return final_quotes


if __name__ == "__main__":
    print(scrape_all(url))








