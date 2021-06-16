from fake_useragent import  UserAgent
import  requests
import  time
import  random
class  TXSpider(object):
    '''爬取和写入到本地json'''
    def __init__(self,root):
        self.url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1619657326691&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=' \
                 '&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.headers={
            'user-agent':UserAgent().random
        }
        self.page=1
        self.root = root

    def get_page(self,url):
        res=requests.get(url=url,headers=self.headers)
        html=res.content.decode('utf-8')
        return html

    def write_page(self,html):
        '''将json写到本地'''
        filename = self.root + '/第{}页.json'.format(self.page)
        print(filename)
        with open(filename,'w+',encoding='utf-8') as f:
            f.write(html)

    def main(self):
        for page in range(1,6):
            url=self.url.format(page)
            html=self.get_page(url)
            self.write_page(html)
            time.sleep(random.randint(3,5))
            print("第{}页爬取成功".format(self.page))
            self.page+=1