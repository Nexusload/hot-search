#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import random
import time


def get_top_searches():
    # Define a list of Google domains to use for the search
    google_domains = [
        'https://www.google.com',
        'https://www.google.co.uk',
        'https://www.google.ca',
        'https://www.google.com.au',
        'https://www.google.co.nz',
        'https://www.google.co.jp',
        'https://www.google.co.kr',
        'https://www.google.co.in',
        'https://www.google.com.br',
        'https://www.google.fr'
    ]

    # Choose a random Google domain
    google_domain = random.choice(google_domains)

    # Make a GET request to the Google search page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(google_domain + '/trends/hottrends/atom/feed', headers=headers)

    # Parse the response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'xml')

    # Extract the titles of the top 10 trending searches
    titles = soup.find_all('title')[1:]
    top_searches = [title.text for title in titles][:20]

    # Return the top searches as a string separated by commas
    return ','.join(top_searches)
