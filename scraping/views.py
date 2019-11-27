import bs4
import requests
import string
import re
from django.http import HttpResponse
from django.shortcuts import render
from crud.forms import FilmForm
from crud.models import Film


def listing(request):
    return render(request, 'scraping/main.html')


def news(request):
    remote = requests.get("https://www.imdb.com/movies-in-theaters/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    all = soup.findAll("div", {"class": "list_item"})
    for div in all:
        chars = '()[]-/\ '
        title = div.find("h4").findChildren("a", recursive=False)[0]
        release_year = div.find("h4").findChildren("span", recursive=False)[0].text
        #for char in chars:
        #   date = date.replace(char, "")
        duration = div.find("p", {"class": "cert-runtime-genre"}).findChildren("time")[0].text
        metascore = div.find("div", {"class": "rating_txt"}).findChildren("span")[0].text
        description = div.find("div", {"class": "outline"}).text
        director = div.find("div", {"class": "txt-block"}).findChildren("span")[0].text
        return HttpResponse([title, release_year, duration, metascore, description, director])


""" def coming(request):
    remote = requests.get("https://www.imdb.com/movies-coming-soon/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    all = soup.findAll("div", {"class": "list_item"})
    return HttpResponse(all) """
