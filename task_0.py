import requests, bs4

url = 'http://lib.ru/HITPARAD/hitlast1000.txt'
r = requests.get(url)
r.encoding = 'koi8-r'

b = bs4.BeautifulSoup(r.text, 'html.parser')
table_number = b.select('table:nth-of-type(2) tr td:nth-of-type(1)')
table_name = b.select('table:nth-of-type(2) tr td:nth-of-type(2) a')
table_text = b.select('table:nth-of-type(2) tr td:nth-of-type(3) a')

i = 0
while i < len(table_number):
    print(table_number[i].getText(), 'Автор:', table_name[i].getText(), 'Произведение:', table_text[i].getText())
    i += 1