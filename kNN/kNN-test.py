# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:37:46 2016

@author: Administrator
"""

datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
print(datingLabels)



fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
#print(15.0*array(datingLabels))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax2.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
