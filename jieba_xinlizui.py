#!/usr/bin/env python
# -*- coding: utf-8 -*-    
import sys
import jieba
import jieba.analyse
import jieba.posseg as pseg

from os import path

d=path.dirname(__file__)

jieba.add_word('高于')
text_path='《心理罪0：第七个读者》作者：雷米.txt'
text=open(path.join(d,text_path),'rb').read()

def Cutwords(text):
    mywordlist=[]
    seg_list=jieba.cut(text,cut_all=False)
    liststr="/".join(seg_list)
    for myword in liststr.split('/'):
        if len(myword.strip())>1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)

txt5=Cutwords(text)
text_write='5.txt'
with open(text_write,'w') as f:
    f.write(txt5)
    print("Success")
    
tags=jieba.analyse.extract_tags(text,50,withWeight=False)
text=" ".join(tags)
print(tags)


