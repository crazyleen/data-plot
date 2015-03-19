#!/usr/bin/env python
# coding=UTF-8
from pylab import *

#获取不同颜色
class RandomColor():
    i=-1
    cnames= ['blue','gray','brown','green','cyan','red','lightgreen',\
'black','lightyellow','purple','pink','greenyellow','white']

    @staticmethod
    def getColor():
        if RandomColor.i < len(RandomColor.cnames) - 1:
            RandomColor.i=RandomColor.i+1
        return RandomColor.cnames[RandomColor.i]


#读取文件的点
class Points(object):
    Xs = []
    Ys = []
    i_iter = 0

    def __init__(self, filename):
        self.loadFile(filename)

    #load points into arrays from csv
    def loadFile(self, filename):
        X=[]
        Y=[]
        for line in file(filename):
            if "Cluster" in line:
                #print line
                if len(X) > 0:
                    self.Xs.append(X)
                    self.Ys.append(Y)
	            X=[]
                Y=[]
                continue

            xstr,ystr = line.split(",")
            X.append(float(xstr))
            Y.append(float(ystr))

        if len(X) > 0:
            self.Xs.append(X)
            self.Ys.append(Y)

        #自定义list排序对比函数
        def comp(x,y):
           if len(x) > len(y):
                return -1
           elif len(x) == len(y):
                return 0
           else:
                return 1

        #list排序
        self.Xs.sort(comp)
        self.Ys.sort(comp)

    def getX(self):
        return self.Xs

    def getY(self):
        return self.Ys

    #迭代器
    def __iter__(self):
        self.i_iter = 0
        return self;

    #支持for in操作
    def next(self):
        if self.i_iter < len(self.Xs):
            x,y = self.Xs[self.i_iter],self.Ys[self.i_iter]
            self.i_iter = self.i_iter + 1
            return (x,y)
        raise StopIteration()

def PlotPoints(filename):
    for x,y in Points(filename):
        scatter(x,y, s=25, c=RandomColor.getColor())
    show()

if __name__ == "__main__":
    PlotPoints("output")


