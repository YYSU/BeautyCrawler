import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 \
     (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36Name'
}
res = requests.get('https://www.ptt.cc/bbs/Beauty/M.1499664133.A.40C.html', headers=headers)
print(res.text)
