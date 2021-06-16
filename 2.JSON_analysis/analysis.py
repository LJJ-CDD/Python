import  json
import csv

class JXSpider(object):
    '''将本地json转换为CSV'''
    def __init__(self, root):
        self.root = root

    def parse_page(self,json_str):
        '''将json字符串转成python字符串'''
        python_dict=json.loads(json_str)
        python_list=python_dict['Data']['Posts']
        for car in python_list:
            career_dict={}
            career_dict['RecruitPostName']=car['RecruitPostName']
            career_dict['LocationName']=car['LocationName']
            career_dict['Responsibility']= car['Responsibility'].replace('\n','').replace('\r','') # 格式化
            self.write_page(career_dict)

    def write_page(self, career_dict):
        ''' 写入csv '''
        filename = self.root + '/TX.csv'
        film_list = []
        with open(filename, 'a', encoding='utf-8') as f: 
            writer = csv.writer(f)
            for K,V in career_dict.items():
                film_list.append(V)
            writer.writerow(film_list)

    def main(self):
        for i in range(1,6):
            filename = self.root + '/第{}页.json'.format(i)
            f=open(filename,'r',encoding='utf-8')
            json_str=f.read()
            self.parse_page(json_str)