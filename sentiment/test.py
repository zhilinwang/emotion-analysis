#!/usr/bin/env python2.7
#coding=utf-8
import NLP
def testSa():
    result=NLP.sentiment(u'今天不大高兴')
    for rst in result:
        print rst,
def testRemove():
    l=NLP.clause(u'')
    words=NLP.cut(l)
    NLP.loadDict()
    wds=NLP.rmStopWords(words)
    for w in wds:
        for i in w:
            print i.encode('utf-8')
def test():
    l=NLP.clause(u'')
    print len(l)
    for x in l:
        print x, len(x)

    words=NLP.cut(l)
    for w in words:
        for i in w:
            print i.encode('utf-8')
    words=NLP.tokenize(l)
    for w in words:
        for i in w:
            print i[0],i[1],i[2]
    NLP.loadDict()
testSa()
