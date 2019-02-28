import requests

url = 'https://imgsrc.baidu.com/baike/pic/item/8b82b9014a90f60379de464a3512b31bb051ed55.jpg'
headers = {'User-Agent':'Mozilla/5.0'}

res = requests.get(url,headers=headers)

res.encoding = 'utf-8'
html = res.content

with open('龙猫.jpg','wb') as f:
    f.write(html)

