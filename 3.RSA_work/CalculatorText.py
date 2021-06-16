from logging import root
import tkinter  # 窗体相关
import tkinter.messagebox   # 实现提示框的组件
import tkinter.simpledialog # 对话框
import os   # 路径
import sys  # 操作系统交互
import re
from typing import Pattern # 正则

import rsa_test

def get_resource_path(relative_path): # 利用此函数实现资源路径的定位
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS # 获取临时资源
    else:
        base_path = os.path.abspath(".")    # 获取当前路径
    return os.path.join(base_path, relative_path) # 绝对路径

LOGO_PATH = get_resource_path(os.path.join("Python_work\\3.RSA_work\\resources", "RSA.ico")) # 图标文件路径
IMAGES_PATH = get_resource_path(os.path.join("Python_work\\3.RSA_work\\resources", "Rsa_Icon.png")) # 图片路径
EMAIL_PATTERN = r"[a-zA-Z0-9]\w+@\w+\.(cn|com|com.cn|gov|net)"  # 正则表达式
#LOGO_PATH = get_resource_path(os.path.join("resources", "RSA.ico")) # 图标文件路径
#IMAGES_PATH = get_resource_path(os.path.join("resources", "Rsa_Icon.png")) # 图片路径

import tkinter # 导入相关的窗体模块
class MainForm: # 定义窗体类
    def __init__(self):
        self.root = tkinter.Tk() # 创建一个窗体
        self.root.title("CalculatorText") # 设置标题
        self.root.iconbitmap() # 设置logo的资源
        self.root.geometry("231x280") # 设置初始化尺寸
        self.root["background"] = "LightSlateGray" # 背景色
        #self.photo = tkinter.PhotoImage(file=IMAGES_PATH) # 定义图片组件
        #self.root.protocol("WM_DELETE_WINDOW", self.close_handle) # 窗体关闭事件

        ''' 组件 '''
        self.button_frame()
        self.input_frame()
        self.root.mainloop() # 显示窗体

    def input_frame(self): # 定义输入组
        self.input_frame = tkinter.Frame(self.root, width=20) # 创建一个内部容器
        self.content = tkinter.StringVar()  # 修改标签文字
        self.entry = tkinter.Entry(self.input_frame, 
            width=14, font=("微软雅黑", 20), textvariable=self.content) # 用entry 控制单行输入
        self.entry.pack(fill="x", expand=1) # x轴全填充
        self.clean = False # 清除标记，每一次计算完成之后清除
        self.input_frame.pack(side="top")

    def button_frame(self): # 定义按钮组
        self.button_frame = tkinter.Frame(self.root, width=50) # 创建容器
        self.button_list = [[], [], [], []] # 一共定义了4组组件
        self.button_list[0].append(tkinter.Button(self.button_frame, text="1", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[0].append(tkinter.Button(self.button_frame, text="2", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[0].append(tkinter.Button(self.button_frame, text="3", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[0].append(tkinter.Button(self.button_frame, text="+", fg="black", width=3, font=("微软雅黑", 20)))
        
        self.button_list[1].append(tkinter.Button(self.button_frame, text="4", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="5", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="6", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="-", fg="black", width=3, font=("微软雅黑", 20)))
        
        self.button_list[2].append(tkinter.Button(self.button_frame, text="7", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="8", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="9", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="*", fg="black", width=3, font=("微软雅黑", 20)))

        self.button_list[3].append(tkinter.Button(self.button_frame, text=".", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="0", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="=", fg="black", width=3, font=("微软雅黑", 20)))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="/", fg="black", width=3, font=("微软雅黑", 20)))
        
        self.row = 0 # 进行行数的控制
        for group in self.button_list:
            self.column = 0 # 进行列的控制
            for button in group:
                button.bind("<Button-1>", lambda event: self.button_handle(event)) # 绑定事件
                button.grid(row=self.row, column=self.column)
                self.column += 1 # 每次列+1
            self.row += 1
        
        self.button_frame.pack(side="bottom")

    def button_handle(self, event):
        oper = event.widget["text"] # 获取组件中的文本
        if self.clean: # 第二次计算
            self.content.set("") # 清除标记中的数据
            self.clean = False # 留给下一次计算输入
        if oper != "=": # 意味着计算
            self.entry.insert("end", oper)
        elif oper == "=": # 执行运算
            result = 0 # 保存程序的计算结果
            exp = self.entry.get()
            result = eval(exp)
            self.entry.insert("end", "=%s" % result)        
            self.clean = True

def main(): # 主函数 
    MainForm() # 实例化窗体类

if __name__ == "__main__":
    main()
