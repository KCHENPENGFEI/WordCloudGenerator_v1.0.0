# -*- coding:utf-8 -*-
__author__ = 'Chen Binbin'
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud


def CreateWordCloud(txtpath, cutflag, picpath, bkgrd, MaxSize, clarity, outputpath):
    # Read the whole text.
    text = open(txtpath).read()  #read the file and recode in gbk
    text = unicode(text, 'gbk')
    print(cutflag)
    if cutflag :
        textnew = " ".join(jieba.cut(text, cut_all = True))   #choose cut the word by jieba or not
    else :
        textnew = text

    maskpic = np.array(Image.open(picpath))   #choose the mask picture


    wc = WordCloud(font_path = "C:\Windows\Fonts\msyh.ttc", background_color = bkgrd, max_words = 2000, mask = maskpic,
                   max_font_size = MaxSize, random_state = 60, scale = clarity, mode = "RGBA")
    # generate word cloud
    wc.generate(textnew)
    wc.to_file(outputpath + '/result.png')   #generate the wordcloud

if __name__ == "__main__":
    pass
