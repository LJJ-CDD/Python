from urllib import request
import requests
import re
import csv
import os

class JieXiBangDanSpider(object):
    ''' 解析榜单 '''
    def __init__(self, root):
        self.root = root

    def parse_page(self, html):
        ''' 正则匹配 '''
        pattern = re.compile('<dd>.*?<a.*?class="image-link".*?<img.*?data-src="(.*?)".*?</a>.*?'   # 图片
                             '<div class="movie-item-info">.*?class="name">.*?'     # 电影名称
                             '<a.*?title="(.*?)".*?class="star">(.*?)</p>.*?'       #主演
                             'class="releasetime">(.*?)</p>.*?'     # 上映时间
                             'class="score">.*?<i.*?>(.*?)</i>.*?<i.*?>(.*?)</i></p>'   # 评分
                             , re.S)   
        r_list = pattern.findall(html)
        self.write_page(r_list)

    def write_page(self, r_list):
        ''' 写入csv '''
        filename = self.root + '/maoyan.csv'
        film_list = []
        with open(filename, 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            for rt in r_list:
                one_film = [
                        rt[1].strip(), rt[2].strip()[5:15],rt[3].strip()[5:],rt[4].strip()+rt[5].strip(),rt[0]
                    ]
                film_list.append(one_film)
                self.download_image(rt[0], rt[1])  # 下载图片
            writer.writerows(film_list)
    
    def save_image(self, content, name):
        ''' 下载图片 '''
        file_path = '{0}/{1}.{2}'.format(self.root, name, 'jpg')#注意斜杠是/
        if not os.path.exists(file_path):#os.path.exists(file_path)判断文件是否存在，存在返回1，不存在返回0
            with open(file_path, 'wb') as f:
                f.write(content)
                f.close()

    def download_image(self, url, name):#保存图片链接
        r = requests.get(url)
        r.raise_for_status()
        self.save_image(r.content, name)

    def main(self):
        for i in range(1,6):
            filename = self.root + '/第{}页.html'.format(i)
            f=open(filename,'r',encoding='utf-8')
            html=f.read()
            self.parse_page(html)