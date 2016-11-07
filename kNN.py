'''
Created on 2016/11/7
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

'''
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
group,labels=createDataSet()
print(group)
print("~~~~~")
#print(labels)
#print(random.rand(4,4))

#inx未知类别的值，dotaset已知类别的数据，labels已知相对应的类别，选取与当前点距离最小的k个点
def classify0(inX,dataSet,labels,k):
    #数组的大小可以通过shape属性获得，这里是二维数组，0轴长度为4
    dataSetSize = dataSet.shape[0]
    #tile()沿inx的各个维度的重复次数，这里获取差值
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat ** 2#获取各行到点的距离
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5 #开根号
    sortedDistIndicies = distances.argsort() #argsort函数返回的是数组值从小到大的索引值
    classCount={}
    print(distances)
    print(sortedDistIndicies)
    print("~~~~~")
    for i in range(k):#range(k)代表从0到k（不包含k）
        voteIlabel = labels[sortedDistIndicies[i]]
        print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        print(classCount.get(voteIlabel,0))
        print(classCount)
    #key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。
    #这个技术是快速的因为key指定的函数将准确地对每个元素调用。
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print("~~~~~")
    print(classCount)
    print(sortedClassCount)
    print(sortedClassCount[0][0])
    return sortedClassCount[0][0]

    



