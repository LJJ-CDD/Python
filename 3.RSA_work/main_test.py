from logging import root
import tkinter  # 窗体相关
import tkinter.messagebox   # 实现提示框的组件
import tkinter.simpledialog # 对话框
import os   # 路径
import sys  # 操作系统交互
import re # 正则

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
        self.root.title("Liu_RsaText") # 设置标题
        self.root.iconbitmap() # 设置logo的资源
        self.root.geometry("500x300") # 设置初始化尺寸
        self.root.maxsize(1000, 400) # 设置窗体的最大尺寸
        self.root["background"] = "LightSlateGray" # 背景色

        self.photo = tkinter.PhotoImage(file=IMAGES_PATH) # 定义图片组件
        self.content = tkinter.StringVar()  # 修改标签文字
        self.root.protocol("WM_DELETE_WINDOW", self.close_handle) # 窗体关闭事件

        ''' 组件 '''
        #self.label_photo()
        #self.TK_text()
        #self.label_text()
        self.TK_button()

        self.root.mainloop() # 显示窗体

    def label_text(self):
        # 进行文本标签定义
        Lambda_text = tkinter.Label(self.root, textvariable=self.content, width=200, height=200, 
            bg="#223011", fg="#ffffff",font=("微软雅黑", 10), justify="right")
        Lambda_text.pack() # 组件显示

    def label_photo(self):
        # 进行文本图片标签定义
        Label_photo = tkinter.Label(self.root, image=self.photo)  # 图片标签
        Label_photo.pack() # 标签显示 

    def TK_text(self):
        # 定义文本组件窗口
        text = tkinter.Text(self.root, width=50, height=10, font=("微软雅黑", 10))
        #text.image_create("end", image=self.photo)
        text.insert("current", "请输入正确的Email信息....") # 默认提示信息
        text.bind("<Button-1>", lambda event :
            self.event_handle_text(event, text, " "))
        text.bind("<KeyPress>",lambda even: 
            self.event_handle_keyboard(even, text))
        text.bind("<KeyRelease>",lambda even: 
            self.event_handle_keyboard(even, text))
        text.pack() # 显示文本组件

    def TK_button(self):
        # 定义按钮组件
        button = tkinter.Button(self.root, text="Liu" , image=self.photo,
            compound="bottom", fg="black", font=("微软雅黑", 10))   # 图片文本混合按钮
        button.bind("<Button-1>", lambda event :
            self.event_handle(event, "Hello World"))    # 事件
        button.pack()

    def event_handle(self, event, info):
        # 消息框事件
        input_message = tkinter.simpledialog.askstring("提示信息", "请输入要显示的信息: ")
        self.label_text()
        tkinter.messagebox.showinfo(title="Liu消息提示", message=input_message)
    
    def event_handle_text(self, event, text, info):
        # 文本删除事件
        text.delete("0.0", "end")

    def event_handle_keyboard(self, event, text):
         # 获得文本框信息输入事件
        email = text.get("0.0", "end")
        if re.match(EMAIL_PATTERN, email, re.I | re.X):
            self.content.set("Email邮箱输入正确，内容为: %s" % email)
        else:
            self.content.set("Email数据输入错误!")

    def close_handle(self):
        if tkinter.messagebox.askyesnocancel("程序关闭确认！", "是否确认关闭程序？"):
            self.root.destroy() # 关闭程序
            
def main(): # 主函数 
    MainForm() # 实例化窗体类

if __name__ == "__main__":
    main()
