from urllib import request
import re
import time
import csv

#1111


class MaoyanSpyder(object):
    def __init__(self):

        self.baseurl = 'https://bj.lianjia.com/zufang/pg%srt200600000001l0rp3rp4/#contentList'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}


        self.page = 1


    def getPage(self,url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)

    def parsePage(self,html):

        p = re.compile(
            '<a target="_blank" href="/zufang.*?html">(.*?)</a>.*?<a target=.*?">(.*?)</a>.*?target=.*?">(.*?)</a>.*?<span class="content__list--item-price"><em>(.*?)</em>(.*?)</span>',re.S)


        # p = re.compile(
        #
        #     '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        rlist = p.findall(html)
        self.writecsv(rlist)

    def writecsv(self,rlist):
        with open('链家租房.csv','a',newline='') as f:
            writer = csv.writer(f)
            for rt in rlist:
                writer.writerow([rt[0].strip(),rt[1].strip()+rt[2].strip(),
                                rt[3].strip() + rt[4].strip()])



    def workOn(self):
        for pn in range(1,9):
            url = self.baseurl%pn
            print(url)
            self.getPage(url)
            print('第%d页完成'%self.page)
            self.page += 1
            time.sleep(0.5)



if __name__ == '__main__':
    spyder = MaoyanSpyder()
    spyder.workOn()
