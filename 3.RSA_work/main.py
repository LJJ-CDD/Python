from logging import root
import tkinter  # 窗体相关
import tkinter.messagebox   # 实现提示框的组件
import tkinter.simpledialog # 对话框
import os   # 路径
import sys  # 操作系统交互
from primes import Primes   # 生成素数
import random
import rsa_test

def get_resource_path(relative_path): # 利用此函数实现资源路径的定位
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS # 获取临时资源
    else:
        base_path = os.path.abspath(".")    # 获取当前路径
    return os.path.join(base_path, relative_path) # 绝对路径

#LOGO_PATH = get_resource_path(os.path.join("Python_work\\3.RSA_work\\resources", "RSA.ico")) # 图标文件路径
#IMAGES_PATH = get_resource_path(os.path.join("Python_work\\3.RSA_work\\resources", "Rsa_Icon.png")) # 图片路径
LOGO_PATH = get_resource_path(os.path.join("resources", "RSA.ico")) # 图标文件路径
IMAGES_PATH = get_resource_path(os.path.join("resources", "Rsa_Icon.png")) # 图片路径

import tkinter # 导入相关的窗体模块
class MainForm: # 定义窗体类
    def __init__(self):
        self.root = tkinter.Tk() # 创建一个窗体
        self.root.title("CalculatorText") # 设置标题
        self.root.iconbitmap(LOGO_PATH) # 设置logo的资源
        self.root.geometry("505x195") # 设置初始化尺寸
        self.root["background"] = "LightSlateGray" # 背景色
        #self.photo = tkinter.PhotoImage(file=IMAGES_PATH) # 定义图片组件
        self.root.protocol("WM_DELETE_WINDOW", self.close_handle) # 窗体关闭事件

        self.content_P = tkinter.StringVar()  # 素数P
        self.content_Q = tkinter.StringVar()  # 素数Q
        self.content_expressly = tkinter.StringVar()  # 明文
        self.content_ciphertext = tkinter.StringVar()  # 密文
        self.content_PK = tkinter.StringVar()  # 公钥
        self.content_SK = tkinter.StringVar()  # 私钥
        self.content_N1 = tkinter.StringVar()  # N1
        self.content_N2 = tkinter.StringVar()  # N2
        self.content_E = tkinter.StringVar()  # 公钥 E
        self.content_D = tkinter.StringVar()  # 私钥 D

        self.font_button = ("微软雅黑", 10)
        self.font_entry = ("微软雅黑", 15)
        self.label_width = 6

        ''' 组件 '''
        self.input_frame_1()
        self.input_frame_2()
        self.input_frame_3()
        self.root.mainloop() # 显示窗体

    def input_frame_1(self): # 生成公私钥框
        input_frame = tkinter.Frame(self.root, width=50) # 创建容器
        label_P = tkinter.Label(input_frame, text="素数P: ", width=self.label_width)
        entry_P = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_P)
        label_Q = tkinter.Label(input_frame, text="素数Q: ", width=self.label_width)
        entry_Q = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_Q)
        button_random = tkinter.Button(input_frame, text="随机", fg="black", width=4, font=self.font_button)
        button_random.bind("<Button-1>", lambda event: self.button_handle_random(event)) # 绑定按钮(随机素数)事件

        label_PK = tkinter.Label(input_frame, text="公钥:", width=self.label_width)
        entry_pk = tkinter.Entry(input_frame, 
            width=22, font=("微软雅黑", 10), textvariable=self.content_PK)
        label_SK = tkinter.Label(input_frame, text="私钥:", width=self.label_width)
        entry_SK = tkinter.Entry(input_frame, 
            width=22, font=("微软雅黑", 10), textvariable=self.content_SK)
        button_create = tkinter.Button(input_frame, text="生成", fg="black", width=4, font=self.font_button)
        button_create.bind("<Button-1>", lambda event: self.button_handle_create(event)) # 绑定按钮(生成公私钥)事件

        label_P.grid(row=0, column=0)
        entry_P.grid(row=0, column=1)
        label_Q.grid(row=0, column=2)
        entry_Q.grid(row=0, column=3)
        button_random.grid(row=0, column=4)

        label_PK.grid(row=1, column=0)
        entry_pk.grid(row=1, column=1)
        label_SK.grid(row=1, column=2)
        entry_SK.grid(row=1, column=3)
        button_create.grid(row=1, column=4)

        input_frame.pack()

    def input_frame_2(self):    # 加密解密框
        input_frame = tkinter.Frame(self.root, width=50) # 创建容器
        label_N1 = tkinter.Label(input_frame, text="N1: ", width=self.label_width)
        entry_N1 = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_N1)
        label_E = tkinter.Label(input_frame, text="E: ", width=self.label_width)
        entry_E = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_E)
        label_N2 = tkinter.Label(input_frame, text="N2: ", width=self.label_width)
        entry_N2 = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_N2)
        label_D = tkinter.Label(input_frame, text="D: ", width=self.label_width)
        entry_D = tkinter.Entry(input_frame, 
            width=15, font=self.font_entry, textvariable=self.content_D)

        button_encryption = tkinter.Button(input_frame, text="加密", fg="black", width=4, font=self.font_button)    # 加密
        button_decrypt = tkinter.Button(input_frame, text="解密", fg="black", width=4, font=self.font_button)   # 解密
        button_encryption.bind("<Button-1>", lambda event: self.button_handle_encryption(event)) # 绑定按钮(加密)事件
        button_decrypt.bind("<Button-1>", lambda event: self.button_handle_decrypt(event)) # 绑定按钮(解密)事件

        label_N1.grid(row=0, column=0)
        entry_N1.grid(row=0, column=1)
        label_E.grid(row=0, column=2)
        entry_E.grid(row=0, column=3)
        button_encryption.grid(row=0, column=4)

        label_N2.grid(row=1, column=0)
        entry_N2.grid(row=1, column=1)
        label_D.grid(row=1, column=2)
        entry_D.grid(row=1, column=3)
        button_decrypt.grid(row=1, column=4)

        input_frame.pack()

    def input_frame_3(self): # 明文和密文框
        input_frame = tkinter.Frame(self.root, width=50) # 创建一个内部容器
        label_expressly = tkinter.Label(input_frame, text="明文: ", width=self.label_width)
        label_ciphertext = tkinter.Label(input_frame, text="密文: ", width=self.label_width)
        entry_expressly = tkinter.Entry(input_frame, 
            width=38, font=self.font_entry, textvariable=self.content_expressly) # 明文
        entry_ciphertext = tkinter.Entry(input_frame, 
            width=38, font=self.font_entry, textvariable=self.content_ciphertext) # 密文
        
        label_expressly.grid(row=0, column=0)
        entry_expressly.grid(row=0, column=1)
        label_ciphertext.grid(row=1, column=0)
        entry_ciphertext.grid(row=1, column=1)
        input_frame.pack()

    def button_handle_random(self, event):    # 按钮(随机素数)事件
        a= Primes(2, 5000, 1000)
        p = random.choice(a)
        q = random.choice(a)
        self.content_P.set("%s" % p)
        self.content_Q.set("%s" % q)
        #print("素数p=%s, 素数q=%s" % (p,q))

    def button_handle_create(self, event):  # 按钮(生成公私钥)事件
        try:
            content_P = int(self.content_P.get())
            content_Q = int(self.content_Q.get())
        except ValueError:
            tkinter.messagebox.showinfo(title="消息提示(只能素数)", message="请输入正确的素数 P 和 Q ")
        else:
            n = content_P * content_Q
            s = (content_P-1) * (content_Q-1)
            e = rsa_test.co_prime(s)
            #print("根据e和(p-1)*(q-1))互质得到: e=%s s=%s" % (e,s))
            d = rsa_test.find_d(e,s)
            #print("根据(e*d) 模 ((p-1)*(q-1)) 等于 1 得到 d=", d)

            self.content_PK.set("(N1=%s E=%s)" % (n,e))
            self.content_SK.set("(N2=%s D=%s)" % (n,d))
            self.content_N1.set("%s" % n)
            self.content_N2.set("%s" % n)
            self.content_E.set("%s" % e)
            self.content_D.set("%s" % d)

    def button_handle_encryption(self, event):  # 按钮(加密)事件
        try:
            content_expressly = int(self.content_expressly.get())
            content_N1= int(self.content_N1.get())
            content_E = int(self.content_E.get())
        except ValueError:
            tkinter.messagebox.showinfo(title="消息提示(只能整数)", message="请输入正确的 N1、E、明文")
        else:
            B = pow(content_expressly,content_E) % content_N1   # 加密
            self.content_ciphertext.set("%s" % B)    
        
    def button_handle_decrypt(self, event):     # 按钮(解密)事件
        try:
            content_ciphertext = int(self.content_ciphertext.get())
            content_N2= int(self.content_N2.get())
            content_D = int(self.content_D.get())
        except ValueError:
            tkinter.messagebox.showinfo(title="消息提示(只能整数)", message="请输入正确的 N2、D、密文")
        else:
            C = pow(content_ciphertext,content_D) % content_N2   # 解密
            self.content_expressly.set("%s" % C)

    def close_handle(self):
        if tkinter.messagebox.askyesnocancel("程序关闭确认！", "是否确认关闭程序？"):
            self.root.destroy() # 关闭程序

def main(): # 主函数 
    MainForm() # 实例化窗体类

if __name__ == "__main__":
    main()
