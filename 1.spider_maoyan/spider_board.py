from urllib import request,parse
import random
import time

class MaoYanSpider(object):
    ''' 爬取网页 '''
    def __init__(self, root):
        self.url="https://maoyan.com/board/4?offset={}"
        self.ua_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
        ]
        #用于记录页数
        self.page = 1
        self.root = root

    '''发送请求函数'''
    def get_page(self,url):
        #定义一个headers
        headers={
            'User-Agent':random.choice(self.ua_list),
        }
        #构造请求头
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        # 将获取的html写到本地
        self.parse_page(html)

    '''定义一个函数写到本地'''
    def parse_page(self,html):
        filename = self.root + '/第{}页.html'.format(self.page)
        print(filename)
        with open(filename,'w+',encoding='utf-8') as f:
            f.write(html)

    '''主函数'''
    def main(self):
        '''拼接url地址'''
        for offset in range(0,60,10):
            url=self.url.format(offset)
            print(url)
            #发送请求  获取响应
            self.get_page(url)
            time.sleep(random.randint(5,8))
            print("第%d页爬取完成"%self.page)
            self.page+=1
