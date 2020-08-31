#-*- coding:utf-8 -*-
from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
test0=np.load('ex0_pcov.npy')
b=test0[np.lexsort(np.rot90(-test0))]
b.sort()
row=len(test0[0])
low=len(test0)
c=b[0:(row//100):,-(low//100):]
Max=c.max()
#a=np.where(test0<Max,0,test0)#小于最大值的所有值变成0
#a=np.log(test0) #取对数
#a=np.exp(test0) #取指数
np.savetxt('a.csv',c,fmt='%s',newline='\n')
test=np.loadtxt('a.csv')
S=np.argwhere(c==Max)
print(S)
sns.heatmap(test, cmap='Spectral_r')
for i in S:
    plt.scatter(i[1],i[0],marker='o',c='',edgecolors='r')#圈出最大值
plt.show()


