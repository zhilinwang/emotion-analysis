#! /usr/bin/env python2.7
#coding=utf-8
import sys
import re
import jieba
import dictLoad
import logging
import math
logger=logging.getLogger(__name__)
tokens=u'[?.!;？。！； ]'
def clause(text):
    logger.info("Text to parse is:%s" % text)
    return re.split(tokens,text)

def cut(l):
    words=[]
    for s in l:
        words.append(jieba.cut(s))
    return words

def tokenize(l):
    words=[]
    for s in l:
        words.append(jieba.tokenize(s))
    return words

def loadDict():
    dictLoad.loadAll()

def rmStopWords(l):
    words=[]
    for s in l:
        sent=[]
        for w in s:
            if w not in dictLoad.stop:
                sent.append(w)
        words.append(sent)
    return words

def sentiment(text):
    jieba.load_userdict("/root/moodevaluator/main/server/senti-analysis/dict/weibo_face.dict")
    loadDict()
    words=rmStopWords(cut(clause(text)))
    for s in words:
        yield(sa(s))

def sa(s):
    sIdx=0
    eIdx=0
    score_sum=0
    for w in s:
        score=0
        logger.info("word:%s" %w)
        if w in dictLoad.emotion:
            eIdx=s.index(w)
            score=int(dictLoad.emotion[w])
            for i in s[sIdx:eIdx]:
                if i in dictLoad.degree:
                    score*=int(dictLoad.degree[i])   
            for i in s[sIdx:eIdx]:
                if i in dictLoad.reverse:
                    score*=int(dictLoad.reverse[i])
            logger.info('sent.:%s,word:%s,sIdx:%d,eIcx:%d,score:%d'%(''.join(s).encode('utf-8'),w,sIdx,eIdx,score))
        sIdx=eIdx
        score_sum+=score
    return score_sum

def tags(statuses):
    stats=[]
    for s in statuses:
        stats.append(s)
    tot_doc=len(stats)
    tf_idf={}
    matrix={}
    doc_wc={}
    idf={}
    result={}
    logger.info('total document:%d' % tot_doc)
    for i in range(tot_doc):
        docs=rmStopWords(cut(clause(stats[i])))
        for words in docs:
            for word in words:
                if (i,word) in matrix:
                    matrix[(i,word)]=matrix[(i,word)]+1
                else:
                    matrix[(i,word)]=1
                if word not in idf:
                    idf[word]=0
            for word in words:
                idf[word]=idf[word]+1
            if doc_wc.get(i) is None:
                doc_wc[i]=len(words)
            else:
                doc_wc[i]=doc_wc[i]+len(words)
    for i in range(tot_doc):
        for word in idf:
            if(i,word) in matrix:   
                logger.info('word:%s, tf: %d, idf:%d .' % (word,matrix.get((i,word))/doc_wc[i],tot_doc/idf[word]))
                tf_idf[(i,word)]=matrix[(i,word)]/doc_wc[i]*math.log(tot_doc/idf[word]) 
    for i in range(tot_doc):
        for word in idf:
            if(i,word) in tf_idf:
                if word not in result:
                    result[word]=tf_idf[(i,word)]
                else:
                    result[word]+=tf_idf[(i,word)]
    return result       

def tf_idfs(statuses):
    tf_idf={}
    matrix={}
    row=0
    col=0
    word_array_set=[]
    idf={}
    for s in statuses:
        words=rmStopWords(cut(clause(s)))
        for word in words:
            if word in word_array_set:
                idx=word_array_set.index(word)
                logger.info(idx)
                matrix[(row,idx)]=matrix.get((row,idx))+1
            else:
                word_array_set.append(word)
                idx=word_array_set.index(word)
                matrix[(row,idx)]=1
                col=col+1
                logger.info(word)
                logger.info(col)
        row=row+1
    for row in range(row):
        for col in range(col):
            logger.info(matrix[(row,col)])   
        
        
def main():
    pass



if __name__ == '__main__':
    main()

