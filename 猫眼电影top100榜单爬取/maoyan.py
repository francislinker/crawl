from urllib import request
import re
import csv
import time

#１．找url规律,拼接url

# baseurl = 'https://maoyan.com/board/4?offset='

#第n页：offset = (n-1)*10

#2.找源代码，拼接正则

#３.代码实现


class MaoyanSpyder(object):
    def __init__(self):

        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    def getPage(self,url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)

    def parsePage(self,html):
        p = re.compile(
            '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        rlist = p.findall(html)
        self.savePage(rlist)

    def savePage(self,rlist):
        with open ('Film','a') as f:
            writer = csv.writer(f)


            for rt in rlist:
                f.write(
                    rt[0].strip() + '' +
                    rt[1].strip() + '' +
                    rt[2] + '\n'
                )
                # l = [
                #     rt[0].strip(),
                #     rt[1].strip(),
                #     rt[2].strip()
                # ]
                #
                # writer.writerow(l)

    def workOn(self):
        for pn in range(0,91,10):
            url = self.baseurl+str(pn)
            print(url)
            self.getPage(url)

if __name__ == '__main__':
    spyder = MaoyanSpyder()
    spyder.workOn()
