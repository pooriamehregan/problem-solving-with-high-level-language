from python_scripts.requesting_urls import get_html
from python_scripts.filter_urls import find_articles
from python_scripts.collect_dates import find_dates
import logging


def do_5_1():
    url1 = "https://en.wikipedia.org/wiki/Studio_Ghibli"
    url2 = "https://en.wikipedia.org/wiki/Star_Wars"
    url3 = "https://en.wikipedia.org/wiki/Dungeons_%26_Dragons"
    url4 = "https://en.wikipedia.org/w/index.php"
    params4 = {'title': 'main', 'action': 'info'}
    params5 = {'title': 'Hurricane_Gonzalo', 'oldid': '983056166'}

    get_html(url1, output="requesting_urls/url1.txt")
    get_html(url2, output="requesting_urls/url2.txt")
    get_html(url3, output="requesting_urls/url3.txt")
    get_html(url4, params=params4, output="requesting_urls/url4.txt")
    get_html(url4, params=params5, output="requesting_urls/url5.txt")


def do_5_2():
    url1 = 'https://en.wikipedia.org/wiki/Nobel_Prize'
    url2 = 'https://en.wikipedia.org/wiki/Bundesliga'
    url3 = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'

    html1 = get_html(url1).text
    html2 = get_html(url2).text
    html3 = get_html(url3).text
    find_articles(html1, 'https://en.wikipedia.org', "filter_urls/url1.txt")
    find_articles(html2, 'https://en.wikipedia.org', "filter_urls/url2.txt")
    find_articles(html3, 'https://en.wikipedia.org', "filter_urls/url3.txt")


def do_5_3():
    url1 = 'https://en.wikipedia.org/wiki/Linus_Pauling'
    url2 = 'https://en.wikipedia.org/wiki/Rafael_Nadal'
    url3 = 'https://en.wikipedia.org/wiki/J._K._Rowling'
    url4 = 'https://en.wikipedia.org/wiki/Richard_Feynman'
    url5 = 'https://en.wikipedia.org/wiki/Hans_Rosling'

    html1 = get_html(url1).text
    html2 = get_html(url2).text
    html3 = get_html(url3).text
    html4 = get_html(url4).text
    html5 = get_html(url5).text
    find_dates(html1, out='filter_dates_regex/url1.txt')
    find_dates(html2, out='filter_dates_regex/url2.txt')
    find_dates(html3, out='filter_dates_regex/url3.txt')
    find_dates(html4, out='filter_dates_regex/url4.txt')
    find_dates(html5, out='filter_dates_regex/url5.txt')


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    # logging.disable(logging.INFO)  # use this call if you wish to disable logging
    logging.info('Executing task 5.1')
    do_5_1()
    logging.info('Executing task 5.2')
    do_5_2()
    logging.info('Executing task 5.3.')
    do_5_3()
    logging.info('Finished.')
