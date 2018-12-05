
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd 
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.grid_search import GridSearchCV  
from sklearn import cross_validation, metrics 
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
get_ipython().run_line_magic('matplotlib', 'inline')

#Process Start#
t0=time.clock()
#--#
train= pd.read_csv('D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\PulseCommand300_All.csv')  
target='Target'  
IDcol= 'CH1' 
print "0/1 counts (0:Normal,1:UnNormal)"
print train['Target'].value_counts() 

x_columns = [x for x in train.columns if x not in [target]]  
X = train[x_columns]  
y = train['Target']  
   
# 測試AUC Score
rf0 = RandomForestClassifier(oob_score=True, random_state=10)  
rf0.fit(X,y)  
print rf0.oob_score_  
y_predprob = rf0.predict_proba(X)[:,1]  
print "AUC Score (Train): %f" % metrics.roc_auc_score(y,y_predprob) 

#對n_estimators進行最佳化搜尋  
param_test1= {'n_estimators':range(10,71,10)}  
gsearch1= GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,  
                                 min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10),  
                       param_grid =param_test1, scoring='roc_auc',cv=5)  
gsearch1.fit(X,y)  
print gsearch1.grid_scores_,gsearch1.best_params_, gsearch1.best_score_  

#對決策樹最大深度max_depth和内部節點再劃分所需最小樣本數min_samples_split進行最佳化搜尋
param_test2= {'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)}  
gsearch2= GridSearchCV(estimator = RandomForestClassifier(n_estimators= 60,  
                                 min_samples_leaf=20,max_features='sqrt' ,oob_score=True,random_state=10),  
   param_grid = param_test2,scoring='roc_auc',iid=False, cv=5)  
gsearch2.fit(X,y)  
print gsearch2.grid_scores_,gsearch2.best_params_, gsearch2.best_score_ 

#

#Process Over#
print time.clock() -t0, "seconds process time"


# In[1]:


import numpy as np
import pandas as pd 
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.grid_search import GridSearchCV  
from sklearn import cross_validation, metrics 
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
get_ipython().run_line_magic('matplotlib', 'inline')

#Process Start#
t0=time.clock()
#--#
train= pd.read_csv('D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\PulseCommand300_All.csv')  
target='Target'  
IDcol= 'CH1' 
print "0/1 counts (0:Normal,1:UnNormal)"
print train['Target'].value_counts() 

x_columns = [x for x in train.columns if x not in [target]]  
X = train[x_columns]  
y = train['Target']  

#利用第一次超參數最佳化測試結果帶入測試 OOB Score 
#{'n_estimators': 10} {'min_samples_split': 50, 'max_depth': 3} 
rf1= RandomForestClassifier(n_estimators= 10, max_depth=3, min_samples_split=50,  
                                 min_samples_leaf=20,max_features='sqrt' ,oob_score=True,random_state=10)  
rf1.fit(X,y)  
print rf1.oob_score_  

#Process Over#
print time.clock() -t0, "seconds process time"


# In[4]:


#Process Start#
t0=time.clock()

#min_samples_split和min_samples_leaf調教
param_test3= {'min_samples_split':range(80,150,20), 'min_samples_leaf':range(10,60,10)}  
gsearch3= GridSearchCV(estimator = RandomForestClassifier(n_estimators= 10,max_depth=3,  
                                 max_features='sqrt' ,oob_score=True, random_state=10),  
   param_grid = param_test3,scoring='roc_auc',iid=False, cv=5)  
gsearch3.fit(X,y)  
print gsearch3.grid_scores_,gsearch3.best_params_, gsearch3.best_score_ 

#Process Over#
print time.clock() -t0, "seconds process time"


# In[17]:


#Process Start#
t0=time.clock()

#max_features調教 
#with {'min_samples_split': 80, 'min_samples_leaf': 10} 
param_test4= {'max_features':range(1,9,1)}  
gsearch4= GridSearchCV(estimator = RandomForestClassifier(n_estimators= 10,max_depth=3, min_samples_split=80,  
                                 min_samples_leaf=10 ,oob_score=True, random_state=10),  
   param_grid = param_test4,scoring='roc_auc',iid=False, cv=5)  

gsearch4.fit(X,y)  
print gsearch4.grid_scores_,gsearch4.best_params_, gsearch4.best_score_  

#Process Over#
print time.clock() -t0, "seconds process time"


# In[16]:


#Process Start#
t0=time.clock()

rf2= RandomForestClassifier(n_estimators= 10, max_depth=3, min_samples_split=80,  
                                 min_samples_leaf=10,max_features=7 ,oob_score=True,random_state=10)  
rf2.fit(X,y)  
print rf2.oob_score_

#Process Over#
print time.clock() -t0, "seconds process time"


# In[30]:


from sklearn.metrics import accuracy_score,f1_score,roc_auc_score

t0=time.clock()
DATA = pd.read_csv('D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\PulseCommand300_TestData.csv')
y = np.array(DATA['Target'])   
#x = DATA.drop(['CH1','CH3','CH4','CH6','CH7','CH8','Target'],axis=1).values
x = DATA.drop('Target',axis=1).values

p=rf2.predict(x)
print ('accuracy:{0:0.5f}'.format(accuracy_score(y,p)))
print time.clock() -t0, "seconds process time"


# In[31]:


from sklearn.externals import joblib
# save the model to disk
filename = 'D:\RFdata\DeltaData\PulseCommandDatas\Finalize_model\\finalized_model1.sav'
joblib.dump(rf2, filename, compress=3)
#使用compress去壓縮learing model
# load the model from disk
loaded_model = joblib.load(filename)
p=loaded_model.predict(x)
print ('accuracy:{0:0.5f}'.format(accuracy_score(y,p)))


# In[33]:


t0=time.clock()
DATA = pd.read_csv('D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\PulseCommand300_TestData150_1.csv')
y = np.array(DATA['Target'])   
#x = DATA.drop(['CH1','CH3','CH4','CH6','CH7','CH8','Target'],axis=1).values
x = DATA.drop('Target',axis=1).values
# load the model from disk
loaded_model = joblib.load(filename)
p1=loaded_model.predict(x)
print ('accuracy:{0:0.5f}'.format(accuracy_score(y,p1)))
print time.clock() -t0, "seconds process time"

