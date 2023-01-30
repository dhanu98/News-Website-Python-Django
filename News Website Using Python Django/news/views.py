from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

article_list = []

r = requests.get('https://news.google.com/news/rss')
soup = BeautifulSoup(r.content, features='xml')
articles = soup.findAll('item')
for a in articles:

    titles = a.title.text
    date = a.pubDate.text
    link = a.link.text
    '''summary = news_data.summary'''
    source = a.source.text
    article = {
        'title': titles,
        'source' : source,
        'link': link,
        'date': date
    }
    article_list.append(article)

def index(req):
    return render(req, 'news/index.html', {'article_news': article_list} )