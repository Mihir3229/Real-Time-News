from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    records = {}
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json
    records['allnews'] = inshorts_data
    return render(request,'index.html',records)

def top(request):
    records1 = {}
    url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    inshorts_data = url.json
    records1['topnews'] = inshorts_data
    return render(request,'top.html' ,records1)


def trending(request):
    records2 = {}
    url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    inshorts_data = url.json
    records2['trending'] = inshorts_data
    return render(request,'trending.html' ,records2)

def science(request):
    records3 = {}
    url = requests.get("https://inshorts.me/news/topics/science")
    inshorts_data = url.json
    records3['science'] = inshorts_data
    return render(request,'science.html' ,records3)

def entertainment(request):
    records4 = {}
    url = requests.get("https://inshorts.me/news/topics/entertainment")
    inshorts_data = url.json
    records4['entertainment'] = inshorts_data
    return render(request,'enter.html' ,records4)

def sports(request):
    records5 = {}
    url = requests.get("https://inshorts.me/news/topics/sports")
    inshorts_data = url.json
    records5['sports'] = inshorts_data
    return render(request,'sports.html' ,records5)