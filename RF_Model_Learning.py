
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd 
import csv
import time
from sklearn.model_selection import train_test_split 
from sklearn import cross_validation, metrics 
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score
from sklearn.externals import joblib


#Variable Setting========================================#
CSVFile = r'D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\120BagPerMin\PulseCommand120_Peak_100k.csv'
Save_Learning_Model = 'D:\RFdata\DeltaData\PulseCommandDatas\Finalize_model\ALLRFModel120_Peak_100k_t70.sav'
#Variable Setting End====================================#

#Process Start#
t0=time.clock()

#吃進Training資料並顯示各狀態資料筆數
Train= pd.read_csv(CSVFile)  
target='Target'  
print ("State / counts")
print (Train['Target'].value_counts()) 

#TraingData PreProcessing
x = Train.drop(['Target'],axis=1).values    
y = Train['Target'] 
   
# RF for Learning Model
RF = RandomForestClassifier(n_estimators=70, oob_score=True, random_state=10)  
RF.fit(x,y) 
# Show OOB_Score, AUC_Score 
print ('OOB_Score:',RF.oob_score_)  

#存取Learing Model
joblib.dump(RF, Save_Learning_Model, compress=3) #使用compress去壓縮learing model


#Process Over#
print ('{0:0.5f}'.format(time.clock() -t0), "seconds process time")


# In[26]:


import numpy as np
import pandas as pd 
import csv
import time
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score
from sklearn.externals import joblib

#Testing Data Process Start#
t0=time.clock()
print ('Testing Process and Results Showing:\n')
#Variable Setting========================================#
CSVFile0 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_0.csv'
CSVFile1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_1.csv'
CSVFile2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_2.csv'
CSVFile3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_3.csv'
Learning_Model_Name = 'D:\RFdata\DeltaData\PulseCommandDatas\Finalize_model\ALLRFModel120_Peak_100k_t100.sav'
#Variable Setting End====================================#

# load the model from disk
loaded_model = joblib.load(Learning_Model_Name)

def TrainingData_Preprocessing_Result(TestData,State):
    x_test = TestData.drop(['CH8','Target'],axis=1).values 
    y_test = TestData['Target']
    result =loaded_model.predict(x_test)
    print ('=====State',State,'Predict Result=====')
    print ('accuracy:{0:0.5f}'.format(accuracy_score(y_test,result)))
    print ('================================\n')

#load Testing data and show data info
TestData0 = pd.read_csv(CSVFile0)
TestData1 = pd.read_csv(CSVFile1)
TestData2 = pd.read_csv(CSVFile2)
TestData3 = pd.read_csv(CSVFile3)
print ("State / counts")
print (TestData0['Target'].value_counts())
print (TestData1['Target'].value_counts())
print (TestData2['Target'].value_counts())
print (TestData3['Target'].value_counts(),'\n')

# load the model from disk
loaded_model = joblib.load(Learning_Model_Name)

# Do TrainingData Preprocessing and Results Showing
TrainingData_Preprocessing_Result(TestData0,'0')
TrainingData_Preprocessing_Result(TestData1,'1')
TrainingData_Preprocessing_Result(TestData2,'2')
TrainingData_Preprocessing_Result(TestData3,'3')

#Process Over#
print ('{0:0.5f}'.format(time.clock() -t0), "seconds process time")

