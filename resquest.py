from bs4 import BeautifulSoup
import requests
import http
import re


def how_many_ep():
    url = 'https://filmeserietorrent.net/series/house-of-the-dragon/'

    #Doing a request to the url to access the html element with BeautifulSoup;
    response = requests.get(url)
    #Transform the big string into a html element like a html file in a text editor;
    soup = BeautifulSoup(response.text, 'html.parser')


    # Here I'm looking for the all span elements when they has the atribute "msn" and
    # put  all elements into my list;
    # after this the variable elements will be a list of html elements; 
    element = soup.find_all("span", attrs={"class":"msn"})

    filtered = BeautifulSoup(str(element), 'html.parser')
    # Here I will return a list of strongs with the episodes number;
    return filtered.find_all('strong')    


