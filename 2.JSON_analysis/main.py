import os
import time
from analysis import JXSpider   #解析
from spider_board import TXSpider  # 爬取网页

def judge_os():
    root = os.getcwd()
    root = root + '/招聘信息'
    root = root.replace(os.sep, '/')
    if(not os.path.exists(root)):
        os.mkdir(root)    
    return root

if __name__ == '__main__':
    root = judge_os()
    start=time.time()
    spider=TXSpider(root)
    spider.main()
    spider=JXSpider(root)
    spider.main()
    end=time.time()
    print('执行时间%.2f'%(end-start))