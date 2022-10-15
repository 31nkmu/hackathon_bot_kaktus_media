from bs4 import BeautifulSoup as bs
import csv
import requests

URL = 'https://kaktus.media/?lable=8&date=2022-10-15&order=time'
dict_with_news = {}


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = bs(html, 'lxml')
    return soup


def get_list_news():
    html = get_html(URL)
    soup = get_soup(html)
    catalog = soup.find('div', class_='Tag--articles')
    news = catalog.find_all('div', class_='Tag--article')
    count = 1
    list_news = []
    for new in news:
        dict_with_news[count] = new
        name = f"{count}. {new.find('a', class_='ArticleItem--name').text.strip()}"
        list_news.append(name)
        count += 1
        if count == 21:
            break
    return '\n'.join(list_news)


def get_one_new(int_):
    url_of_one_new = dict_with_news[int_].find('a', 'ArticleItem--name').get('href')
    html = get_html(url_of_one_new)
    soup = get_soup(html)
    all_about_new = soup.find('div', class_='BbCode').find('p').text
    return all_about_new


def get_photo(int_):
    photo = dict_with_news[int_].find('img', class_='ArticleItem--image-img lazyload').get('src')
    return photo
