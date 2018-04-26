#-*- coding:utf-8 -*-
__author__ = 'Chen Binbin'


from Tkinter import *
from ttk import Combobox
from tkFileDialog import askdirectory, askopenfilename
from wordcloudgenerator import CreateWordCloud

def selectPath_pic():
    path_pic.set(askopenfilename())

def selectPath_text():
    path_text.set(askopenfilename())

def selectPath_result():
    path_result.set(askdirectory())

def generate():
    txtpath = path_text.get().encode("utf-8")
    # print(type(txtpath))
    # print(txtpath)
    picpath = path_pic.get().encode("utf-8")
    # print(type(picpath))
    # print(picpath)
    outputpath = path_result.get().encode("utf-8")
    # print(type(outputpath))
    dict1 = {"是": 1, "否": 0}
    CutFlag = dict1[Cutflag.get().encode(encoding='UTF-8')]
    # print(type(CutFlag))
    dict2 = {"白色": 'white', "蓝色": 'blue', "黄色": 'yellow', "红色": 'red', "黑色": 'black', "绿色": 'green', "透明": None}
    bkgrd = dict2[Background.get().encode(encoding='UTF-8')]
    # print(type(bkgrd))
    dict3 = {"普清": 8, "高清": 16}
    clarity = dict3[Clarity.get().encode(encoding='UTF-8')]
    # print(type(clarity))
    # print(type(MaxSize.get()))
    CreateWordCloud(txtpath, CutFlag, picpath, bkgrd, MaxSize.get(), clarity, outputpath)

wcg = Tk()
wcg.title('Word Cloud Generator v.1.0')
wcg.geometry('360x260')

path_pic = StringVar()
path_text = StringVar()
path_result = StringVar()
Cutflag =  StringVar()
Background = StringVar()
MaxSize = IntVar()
Clarity = StringVar()

Label(wcg, text = "文本路径:").grid(row = 0, column = 0, stick = W)
Entry(wcg, textvariable = path_text, width = 30).grid(row = 0, column = 1, stick = W)
Button(wcg, text = "路径选择", command = selectPath_text).grid(row = 0, column = 2, stick = W)

Label(wcg, text = "图像路径:").grid(row = 1, column = 0, stick = W)
Entry(wcg, textvariable = path_pic, width = 30).grid(row = 1, column = 1, stick = W)
Button(wcg, text = "路径选择", command = selectPath_pic).grid(row = 1, column = 2, stick = W)

Label(wcg, text = "词云保存路径:").grid(row = 2, column = 0, stick = W)
Entry(wcg, textvariable = path_result, width = 30).grid(row = 2, column = 1, stick = W)
Button(wcg, text = "路径选择", command = selectPath_result).grid(row = 2, column = 2, stick = W)

Label(wcg, text = "是否分词:").grid(row = 3, column = 0, stick = W)
input_CutFlag = Combobox(wcg, width = 6, textvariable = Cutflag, values = ("是", "否"))
input_CutFlag.current(0)
input_CutFlag.grid(row = 3, column = 1, stick = W)

Label(wcg, text = "背景颜色:").grid(row = 4, column = 0, stick = W)
input_bkgrd = Combobox(wcg, width = 6, textvariable = Background, values = ("白色", "蓝色", "黄色", "红色", "黑色", "绿色", "透明"))
input_bkgrd.current(0)
input_bkgrd.grid(row = 4, column = 1, stick = W)

Label(wcg, text = "最大字号:").grid(row = 5, column = 0, stick = W)
input_size = Combobox(wcg, width = 6, textvariable = MaxSize, values = (8, 18, 28, 38, 48, 58))
input_size.current(1)
input_size.grid(row = 5, column = 1, stick = W)

Label(wcg, text = "清晰度:").grid(row = 6, column = 0, stick = W)
input_clarify = Combobox(wcg, width = 6, textvariable = Clarity, values = ("普清", "高清"))
input_clarify.current(0)
input_clarify.grid(row = 6, column = 1, stick = W)

Button(wcg, text = 'generate', command = generate).grid(row = 7, column = 1)
Label(wcg, text = ' ').grid(row = 8, column =1)
Label(wcg, text = 'author@Chen Binbin, ZJU').grid(row = 9, column = 1)
wcg.mainloop()


