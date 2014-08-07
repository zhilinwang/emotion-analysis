#! /usr/bin/env python2.7
#coding=utf-8
import cPickle as pickle
degree={}
emotion={}
domain={}
stop=[]
reverse={}

def createDict(path,w):
    f=open(path,'r')
    d={}
    lines=f.readlines()
    for line in lines:
        d[line.strip().decode('utf-8')]=w
    f.close()
    return d

def createSet(path):
    f=open(path,'r')
    s=set()
    lines=f.readlines()
    for line in lines:
        s.add(line.strip().decode('utf-8'))    
    f.close()
    return s

def loadDegree(l):
    path,w=l.split()
    degree.update(createDict(path,w))

def loadEmotion(l):
    path,w=l.split()
    emotion.update(createDict(path,w))
    
def loadDomain(l):
    path=l.strip()
    d={}
    f=open(path,'r')
    lines=f.readlines()
    for l in lines:
        d[l.split()[0]]=l.split()[1]
    domain.update(d)   

def loadStopword(l):
    #print l
    path=l.strip()
    stop.extend(createSet(path))

def loadReverse(l):
    path,x=l.split()
    reverse.update(createDict(path,-1))


#Configuration to be loaded
cfg=['degree','emotion','domain','stopword','reverse']
#Dictionary to map which function will be loaded
load={0:loadDegree,1:loadEmotion,2:loadDomain,3:loadStopword,4:loadReverse}

def loadCfg(path):
    f=open(path,'r')
    lines=f.readlines()
    idx=-1
    for line in lines:
        if line.startswith('#'):
            s=line[1:].strip()
            idx=cfg.index(s)
        else:
            load[idx](line)
def loadAll():
    return loadCfg('/root/moodevaluator/main/server/senti-analysis/cfg/config')
def main():
    loadAll()
    print len(degree)
    print len(emotion)
    print len(domain)
    print len(stop)
    print len(reverse)
if __name__ == '__main__':
    main()
