import bs4
import requests
from django.http import HttpResponse


# Create your views here.
def listing(request):
    return HttpResponse("Listing")


def news(request):
    remote = requests.get("https://www.imdb.com/movies-in-theaters/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    content = soup.findAll("div", {"class": "list_item"})
    return HttpResponse(all)


def coming(request):
    remote = requests.get("https://www.imdb.com/movies-coming-soon/")
    soup = bs4.BeautifulSoup(remote.text, "lxml")
    soup.prettify()
    content = soup.findAll("div", {"class": "list_item"})
    return HttpResponse(all)
