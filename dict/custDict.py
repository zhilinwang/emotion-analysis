#! /usr/bin/env python2.7
#coding=utf-8
import jieba
#jieba.load_userdict('words_pos.dict')
l=jieba.cut(u'[����]����[��ô��]')
for w in l:
   print w.decode('utf-8')
