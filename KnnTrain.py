
# coding: utf-8

# In[35]:


from sklearn import neighbors 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import time
t0=time.clock()

path = 'D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\ForKnn.csv'

DATA = pd.read_csv(path)
y = np.array(DATA['Target'])
x = DATA.drop(['CH1','CH3','CH4','CH6','CH7','CH8','Target'],axis=1).values
#x = DATA.drop('Target',axis=1).values #取Target以外的Feature值
targetNum = DATA['Target']
print "0/1 counts (0:Normal,1:UnNormal)"
print targetNum.value_counts() 

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8) #80%training 20%testing
    
knn = KNeighborsClassifier()
    
knn.fit(x_train,y_train)
    
y_predict = knn.predict(x_test)
    
print('accuracy:{0:0.5f}'.format(accuracy_score(y_test,y_predict)))
    
print('f1_score:',f1_score(y_test,y_predict))

print('auc_score:',roc_auc_score(y_test,y_predict))

print time.clock() -t0, "seconds process time"

#print x_train


# In[36]:


t0=time.clock()
DATA = pd.read_csv('D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\PulseCommand300_TestData.csv')
y = np.array(DATA['Target'])   
x = DATA.drop(['CH1','CH3','CH4','CH6','CH7','CH8','Target'],axis=1).values
#x = DATA.drop('Target',axis=1).values

p=knn.predict(x)
print ('accuracy:{0:0.5f}'.format(accuracy_score(y,p)))
print time.clock() -t0, "seconds process time"


# In[42]:


import pylab as pl
h=0.2
# Plot the decision boundary. For that, we will asign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = x_train[:,0].min() - .5, x_train[:,0].max() + .5
y_min, y_max = x_train[:,1].min() - .5, x_train[:,1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
# Put the result into a color plot
Z = y_predict.reshape(y_predict.shape)
pl.figure(1, figsize=(16, 16))
pl.set_cmap(pl.cm.Paired)
#pl.pcolormesh(xx, yy, Z)

# Plot also the training points
pl.scatter(x_train[:,0], x_train[:,1],c=y_train )
pl.xlabel('位置誤差 [PUU]')
pl.ylabel('速度命令：轉速 [r/min]')

pl.xlim(xx.min(), xx.max())
pl.ylim(yy.min(), yy.max())
pl.xticks(())
pl.yticks(())

pl.show()

