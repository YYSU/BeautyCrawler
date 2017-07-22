import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 \
     (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36Name'
}
res = requests.get('https://www.ptt.cc/bbs/Beauty/M.1499664133.A.40C.html',
                   headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
images = soup.select('a[href^=http://i.imgur]')

for image in images:
    print(image['href'])
    filename = image['href'].split('/')[3]
    img = urlopen(image['href'])
    with open('./images/' + str(filename), 'wb') as f:
        f.write(img.read())
