import bs4
import requests
import string
import re
from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint


def listing(request):
    return render(request, 'scraping/main.html')


def news(request):
    remote = requests.get("https://www.imdb.com/movies-in-theaters/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    all = soup.findAll("div", {"class": "list_item"})
    for div in all:
        chars = '()[]-/\ '
        titre = div.find("h4").findChildren("a", recursive=False)[0]
        date = div.find("h4").findChildren("span", recursive=False)[0].text
        #for char in chars:
        #   date = date.replace(char, "")
        duration = div.find("p", {"class": "cert-runtime-genre"}).findChildren("time")[0].text
        metascore = div.find("div", {"class": "rating_txt"}).findChildren("span")[0].text
        description = div.find("div", {"class": "outline"}).text
        return HttpResponse([titre, date, duration, metascore, description])


def coming(request):
    remote = requests.get("https://www.imdb.com/movies-coming-soon/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    all = soup.findAll("div", {"class": "list_item"})
    return HttpResponse(all)
