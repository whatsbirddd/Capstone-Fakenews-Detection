import requests
from bs4 import BeautifulSoup


def get_title_body_from_link(link):
    res = requests.get(link,
                       headers={
                           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36'
                       })
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select_one('.media_end_head_headline').text.strip()
    body = soup.select_one('#newsct_article').text.strip()
    return title, body

