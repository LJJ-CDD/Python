import os
import time
from analysis import JieXiBangDanSpider
from spider_board import MaoYanSpider  # 爬取榜单网页

def judge_os():
    root = os.getcwd()
    root = root + '/榜单'
    root = root.replace(os.sep, '/')
    if(not os.path.exists(root)):
        os.mkdir(root)    
    return root

if __name__ == '__main__':
    root = judge_os()
    start=time.time()
    #spider=MaoYanSpider(root)
    #spider.main()
    spider=JieXiBangDanSpider(root)
    spider.main()
    end=time.time()
    print('执行时间%.2f'%(end-start))
