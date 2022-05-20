import requests

res = requests.get('https://n.news.naver.com/mnews/article/025/0003191616',
                   headers={
                       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36'
                   })
print(res.text)
