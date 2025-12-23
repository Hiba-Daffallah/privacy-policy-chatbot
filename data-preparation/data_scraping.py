'''
In this file you can find the python code used for web scrapping the privacy policies across major 
social media platforms and saving them all in one dataset

author: Hiba Daffallah
'''

import requests
from bs4 import BeautifulSoup

def scrape_privacy_policy(url, filename):
    '''
    This function is used to scrape privacy policy from a given url and
    saves it to a file

    inputs:
    url: the url of the website we'll get the privacy policy from
    filename: the name of the file to save the data in

    outputs:
    the privacy policy data will be uploaded to the file 
    '''
    # add timeout to avoid program from getting stuck if website is slow
    response = requests.get(url, timeout= 30) 
    # parse the HTML content into a navigable structure
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract main content (adjust selectors per site)
    text = soup.get_text()
    
    # open a file to write in the scraped text
    # adding encoding makes sure the code behaves consistently in all systems
    with open(f'data/privacy_policies/{filename}.txt', 'w', encoding= 'utf-8') as f: 
        f.write(text)