import requests, bs4

url = 'https://pokupki.market.yandex.ru/catalog/mobilnye-telefony/54726/list?hid=91491'
r = requests.get(url)
r.encoding = 'UTF8'

b = bs4.BeautifulSoup(r.text, 'html.parser')
span_titles = b.select('div._brandTheme-default span.b_3l-uEDOaBN')
span_price = b.select('span.b_3LMhEMfZeH span:nth-of-type(1)')

i = 0
list = {}
while i < len(span_titles):
    list[span_titles[i].getText()] = span_price[i].getText()
    i += 1
print(list)