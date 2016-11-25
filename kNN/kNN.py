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
import matplotlib
import matplotlib.pyplot as plt
from os import listdir


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
group,labels=createDataSet()
#print(group)
#print("~~~~~")
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
    #print(distances)
    #print(sortedDistIndicies)
    #print("~~~~~")
    for i in range(k):#range(k)代表从0到k（不包含k）
        voteIlabel = labels[sortedDistIndicies[i]]
        #print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #print(classCount.get(voteIlabel,0))
        #print(classCount)
    #key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。
    #这个技术是快速的因为key指定的函数将准确地对每个元素调用。
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #print("~~~~~")
    #print(classCount)
    #print(sortedClassCount)
    #print(sortedClassCount[0][0])
    return sortedClassCount[0][0]
    
#print(classify0([0,0],group,labels,3))

def file2matrix(filename):
    fr = open(filename)
    #print(fr)
    #arrayOLines = fr.readline()
    #print(arrayOLines)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    #numberOfLines = len(fr.readlines())         #get the number of lines in the file
    #print(fr.readlines())    
    #print(numberOfLines)    
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    #print(returnMat)
    classLabelVector = []                       #prepare labels return   
    index = 0
    for line in arrayOLines:
        line = line.strip()
        #用于一处字符串头尾指定的字符
        listFromLine = line.split('\t')
        #通过制定分隔符对字符串进行切片
        returnMat[index,:] = listFromLine[0:3]
        #将前三项数据存入矩阵
        classLabelVector.append(int(listFromLine[-1]))
        # 将第四项数据存入向量
        index += 1
    #print(classLabelVector)
    #print(returnMat)
    return returnMat,classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals

datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
normMat,ranges,minVals = autoNorm(datingDataMat)
print(normMat)
#print(ranges)
#print(minVals)

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):errorCount += 1.0
    print("the total error rate is: %f" %(errorCount/float(numTestVecs)))
    
datingClassTest()

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    precentTats = float(raw_input('percentage of time spent playing video games?'))
    ffMiles = float(raw_input('frequent filer miles earned per year'))
    iceCream = float(raw_input('leters of ice cream consumed per year?'))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percenTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print('you will probably like this person:',resultList[classifierResult -1])
    
    
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

testVector = img2vector('testDigits/0_13.txt')
print(testVector[0,0:31])

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print('the classifier came back with: %d,the real answer is: %d' %(classifierResult, classNumStr))
        if(classifierResult != classNumStr): errorCount += 1.0
    print('\nthe total number of errors is: %d' % errorCount)
    print('\nthe total error rate is: %f' % (errorCount/float(mTest)))
    
handwritingClassTest()
    




                