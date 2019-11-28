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
    total = 0
    for div in all:
        image = div.find("img", {"class": "poster"})['src']

        try:
            title = div.find("h4").findChildren("a", recursive=False)[0].text
        except:
            pass

        try:
            release_year = div.find("h4").findChildren("span", recursive=False)[0].text
        except:
            pass

        try:
            duration = div.find("p", {"class": "cert-runtime-genre"}).findChildren("time")[0].text
        except:
            pass

        try:
            metascore = div.find("div", {"class": "rating_txt"}).findChildren("span")[0].text
        except:
            pass

        try:
            description = div.find("div", {"class": "outline"}).text
        except:
            pass

        try:
            director = div.find("div", {"class": "txt-block"}).findChildren("span")[0].text
        except:
            pass

        total += 1
        film = Film(title=title, release_year=release_year, duration=duration, description=description, director=director)
        film.save()

    films = Film.objects.all()
    return render(request, "crud/show.html", {'films': films})


def coming(request):
    remote = requests.get("https://www.imdb.com/movies-coming-soon/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    all = soup.findAll("div", {"class": "list_item"})
    return HttpResponse(all)
