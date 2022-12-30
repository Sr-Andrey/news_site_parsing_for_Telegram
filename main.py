import json
import requests
from bs4 import BeautifulSoup
testi = []


def get_first_news():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

    url = 'https://www.championat.com/football/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    article_cards = soup.find_all('div', class_='article-preview')
    article_cards_top = soup.find_all('div', class_='top-article')
    article_cards_top_small = soup.find_all('div', class_='top-article _small')

    dict_news = {}

    for article in article_cards_top:
        article_title = article.find(
            'a', class_='top-article__title').text.strip()
        article_url = article.find('a').get('href')
        # print(article_title, article_url)

        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        dict_news[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    for article in article_cards_top_small:
        article_title = article.find(
            'a', class_='top-article__title').text.strip()
        article_url = article.find('a').get('href')
        # print(article_title, article_url)

        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        dict_news[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    for article in article_cards:
        article_title = article.find(
            'a', class_='article-preview__title').text.strip()
        article_url = article.find('a').get('href')

        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        dict_news[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    with open('news_dic.json', 'w', encoding='utf-8') as file:
        json.dump(dict_news, file, indent=4, ensure_ascii=False)

    print(f'Finish')


def check_news_update():
    fresh_news = {}
    with open('news_dic.json', encoding='utf-8') as file:
        dict_news = json.load(file)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

    url = 'https://www.championat.com/football/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    article_cards = soup.find_all('div', class_='article-preview')
    article_cards_top = soup.find_all('div', class_='top-article')
    article_cards_top_small = soup.find_all('div', class_='top-article _small')

    for article in article_cards:
        article_url = article.find('a').get('href')
        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        if article_id in dict_news:
            continue
        else:
            article_title = article.find(
                'a', class_='article-preview__title').text.strip()
            article_url = article.find('a').get('href')
            dict_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
            fresh_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
    for article in article_cards_top:
        article_url = article.find('a').get('href')
        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        if article_id in dict_news:
            continue
        else:
            article_title = article.find(
                'a', class_='top-article__title').text.strip()
            article_url = article.find('a').get('href')
            dict_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
            fresh_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
    for article in article_cards_top_small:
        article_url = article.find('a').get('href')
        article_id = ''.join(article_url.split('/')[-1]).split('-')[1]

        if article_id in dict_news:
            continue
        else:
            article_title = article.find(
                'a', class_='article-preview__title').text.strip()
            article_url = article.find('a').get('href')
            dict_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
            fresh_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }

    with open('news_dic.json', 'w', encoding='utf-8') as file:
        json.dump(dict_news, file, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    # get_first_news()
    print(check_news_update())


if __name__ == '__main__':
    main()
