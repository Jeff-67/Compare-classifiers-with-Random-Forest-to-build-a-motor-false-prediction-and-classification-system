
# coding: utf-8

# In[4]:


#-*-coding:utf-8 -*-
#Get Peak Value Training Data
import csv
import time
import numpy as np
import pandas as pd
t0=time.clock()

#RawDataName&CSVFilesName Setting
rawdata0_0= "/Users/Apple/Desktop/MLData/rawdata0_0.csv"
rawdata1_0= "/Users/Apple/Desktop/MLData/rawdata1_0.csv"
rawdata2_0= "/Users/Apple/Desktop/MLData/rawdata2_0.csv"
rawdata3_0= "/Users/Apple/Desktop/MLData/rawdata3_0.csv"
rawdata0_1= "/Users/Apple/Desktop/MLData/rawdata0_1.csv"
rawdata1_1= "/Users/Apple/Desktop/MLData/rawdata1_1.csv"
rawdata2_1= "/Users/Apple/Desktop/MLData/rawdata2_1.csv"
rawdata3_1= "/Users/Apple/Desktop/MLData/rawdata3_1.csv"
rawdata0_2= "/Users/Apple/Desktop/MLData/rawdata0_2.csv"
rawdata1_2= "/Users/Apple/Desktop/MLData/rawdata1_2.csv"
rawdata2_2= "/Users/Apple/Desktop/MLData/rawdata2_2.csv"
rawdata3_2= "/Users/Apple/Desktop/MLData/rawdata3_2.csv"
rawdata0_3= "/Users/Apple/Desktop/MLData/rawdata0_3.csv"
rawdata1_3= "/Users/Apple/Desktop/MLData/rawdata1_3.csv"
rawdata2_3= "/Users/Apple/Desktop/MLData/rawdata2_3.csv"
rawdata3_3= "/Users/Apple/Desktop/MLData/rawdata3_3.csv"
rawdata0_4= "/Users/Apple/Desktop/MLData/rawdata0_4.csv"
rawdata1_4= "/Users/Apple/Desktop/MLData/rawdata1_4.csv"
rawdata2_4= "/Users/Apple/Desktop/MLData/rawdata2_4.csv"
rawdata3_4= "/Users/Apple/Desktop/MLData/rawdata3_4.csv"
rawdata0_5= "/Users/Apple/Desktop/MLData/rawdata0_5.csv"
rawdata1_5= "/Users/Apple/Desktop/MLData/rawdata1_5.csv"
rawdata2_5= "/Users/Apple/Desktop/MLData/rawdata2_5.csv"
rawdata3_5= "/Users/Apple/Desktop/MLData/rawdata3_5.csv"
rawdata0_6= "/Users/Apple/Desktop/MLData/rawdata0_6.csv"
rawdata1_6= "/Users/Apple/Desktop/MLData/rawdata1_6.csv"
rawdata2_6= "/Users/Apple/Desktop/MLData/rawdata2_6.csv"
rawdata3_6= "/Users/Apple/Desktop/MLData/rawdata3_6.csv"
rawdata0_7= "/Users/Apple/Desktop/MLData/rawdata0_7.csv"
rawdata1_7= "/Users/Apple/Desktop/MLData/rawdata1_7.csv"
rawdata2_7= "/Users/Apple/Desktop/MLData/rawdata2_7.csv"
rawdata3_7= "/Users/Apple/Desktop/MLData/rawdata3_7.csv"
rawdata0_8= "/Users/Apple/Desktop/MLData/rawdata0_8.csv"
rawdata1_8= "/Users/Apple/Desktop/MLData/rawdata1_8.csv"
rawdata2_8= "/Users/Apple/Desktop/MLData/rawdata2_8.csv"
rawdata3_8= "/Users/Apple/Desktop/MLData/rawdata3_8.csv"
rawdata0_9= "/Users/Apple/Desktop/MLData/rawdata0_9.csv"
rawdata1_9= "/Users/Apple/Desktop/MLData/rawdata1_9.csv"
rawdata2_9= "/Users/Apple/Desktop/MLData/rawdata2_9.csv"
rawdata3_9= "/Users/Apple/Desktop/MLData/rawdata3_9.csv"

PeakValueFrom = 'D:\RFdata\FFT\TrainingData\Normal600rpm_1.csv'
CSVFile = r'D:\RFdata\FFT\TrainingData\PulseCommand600_Peak_10k.csv'
DataSize = 2500
PeakValue = 0
OpenFileFlag = True
#====================================================
def findPeakValue(RawData, PeakValueFrom):
    CSVFileTem = PeakValueFrom
    txtRead=open(RawData,'r')
    lines=txtRead.readlines()
    out=open(CSVFileTem,'wb')
    csv_write=csv.writer(out,dialect='excel')
    columns=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','Target'] #0:Normal; 1,2,3:UnNormal
    csv_write.writerow(columns)
    
    for line in lines[10:]:    
        listTem=[]
        listTem.append(line.split()+['0'])
        csv_write.writerows(listTem)
    out.close()
    txtRead.close()
    
    PeakData = pd.read_csv(PeakValueFrom) 
    MaxValue = max(PeakData['CH1'])
    MinValue = min(PeakData['CH1'])
    PeakValueTem = MaxValue-((MaxValue-MinValue)*0.02)
    print 'Max=',MaxValue,'\n','Min=',MinValue,'\n','PeakValue=',PeakValueTem,'\n'
    return PeakValueTem
#====================================================

#====================================================
def makeLearningData(RawData, CSVFile, State, PeakValue, DataSize, OpenFileFlag):
    CSVFileTem=CSVFile
    txtRead=open(RawData,'r')
    lines=txtRead.readlines()
    
    if OpenFileFlag:
        out=open(CSVFileTem,'wb')
        csv_write=csv.writer(out,dialect='excel')
        columns=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','Target'] #0:Normal; 1,2,3:UnNormal
        csv_write.writerow(columns)
        #OpenFileFlag = False
    else:
        out=open(CSVFileTem,'ab+')
        csv_write=csv.writer(out,dialect='excel')
    
    DataNum = 0
    
    for line in lines[10:]:    
        if DataNum < DataSize:
            if int(line.split()[0]) > PeakValue:
                listTem=[]
                listTem.append(line.split()+[State])
                csv_write.writerows(listTem)
                DataNum = DataNum+1
        
    out.close()
    txtRead.close()   
    print 'Get state',State,' ',DataSize,'piece of data!'
    return False
#====================================================
#====================================================
def addVibrationData(RawData, CSVFile, State, DataSize):
    CSVFileTem=CSVFile
    txtRead=open(RawData,'r')
    lines=txtRead.readlines()
    
    
        columns=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','Target'] #0:Normal; 1,2,3:UnNormal
        csv_write.writerow(columns)

    out=open(CSVFileTem,'ab+')
    csv_write=csv.writer(out,dialect='excel')
    
    DataNum = 0
    
    for line in lines[:]:    
        if DataNum < DataSize:
            listTem=[]
            listTem.append(line.split())
            csv_write.writerows(listTem)
            DataNum = DataNum+1
        
    out.close()
    txtRead.close()   
    print 'Get state',State,' ',DataSize,'piece of data!'
    return False
#====================================================
PeakValue = findPeakValue(RawData0, PeakValueFrom)
OpenFileFlag = makeLearningData(RawData0, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData0_1, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_1, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)

print time.clock() -t0, "seconds process time"


# In[8]:


#-*-coding:utf-8 -*-
#This Program for Making Peak Testing Data 
import csv
import time
t0=time.clock()
#====================================================
RawData0 = 'D:\RFdata\FFT\TestData\Normal600rpm_3.txt'
RawData1 = 'D:\RFdata\FFT\TestData\UnNormal600rpm_3.txt'
TestData0 = 'D:\RFdata\FFT\TestData\Normal600rpm_1k.csv'
TestData1 = 'D:\RFdata\FFT\TestData\UnNormal600rpm_1k.csv'
DataSize = 1000
PeakValue = 1737.14
OpenFileFlag = True
RawData=''
TestData=''
#====================================================
def makeTestData(RawData, TestData, State, PeakValue, DataSize, OpenFileFlag):
    CSVFileTem=TestData
    txtRead=open(RawData,'r')
    lines=txtRead.readlines()
    
    if OpenFileFlag:
        out=open(CSVFileTem,'wb')
        csv_write=csv.writer(out,dialect='excel')
        columns=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','Target'] #0:Normal; 1,2,3:UnNormal
        csv_write.writerow(columns)
        #OpenFileFlag = False
    else:
        out=open(CSVFileTem,'ab+')
        csv_write=csv.writer(out,dialect='excel')
    
    DataNum = 0
    
    for line in lines[10:]:    
        if DataNum < DataSize:
            if int(line.split()[0]) > PeakValue:
                listTem=[]
                listTem.append(line.split()+[State])
                csv_write.writerows(listTem)
                DataNum = DataNum+1
        
    out.close()
    txtRead.close()   
    print 'Get state',State,' ',DataSize,'piece of data!'
    return False
#====================================================
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData0, TestData0, '0', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData1, TestData1, '1', PeakValue, DataSize, OpenFileFlag)

print time.clock() -t0, "seconds process time"


# In[28]:


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
CSVFile = r'D:\RFdata\FFT\TrainingData\PulseCommand600_Peak_OK_10k.csv'
Save_Learning_Model = r'D:\RFdata\FFT\FinalModel\PulseCommand600_Peak_OK_10k.sav'
#Variable Setting End====================================#

#Process Start#
t0=time.clock()

#load training data
Train= pd.read_csv(CSVFile)  
target='Target'  
print ("State / counts")
print (Train['Target'].value_counts()) 

#TraingData PreProcessing
x = Train.drop(['Target'],axis=1).values    
y = Train['Target'] 
   
# RF for Learning Model
RF = RandomForestClassifier(oob_score=True, random_state=10)  
RF.fit(x,y) 
# Show OOB_Score, AUC_Score 
print ('OOB_Score:',RF.oob_score_)  
#y_predprob = RF.predict_proba(x)[:,1]  
#print "AUC Score (Train): %f" % metrics.roc_auc_score(y,y_predprob) 

#saving Learing Model
joblib.dump(RF, Save_Learning_Model, compress=3) #使用compress去壓縮learing model


#Process Over#
print ('{0:0.5f}'.format(time.clock() -t0), "seconds process time")


# In[29]:


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
CSVFile0 = 'D:\RFdata\FFT\TestData\Normal600rpm_OK_1k.csv'
CSVFile1 = 'D:\RFdata\FFT\TestData\UnNormal600rpm_OK_1k.csv'
Learning_Model_Name = r'D:\RFdata\FFT\FinalModel\PulseCommand600_Peak_OK_10k.sav'
#Variable Setting End====================================#

# load the model from disk
loaded_model = joblib.load(Learning_Model_Name)

def TrainingData_Preprocessing_Result(TestData,State):
    x_test = TestData.drop(['Target'],axis=1).values 
    y_test = TestData['Target']
    result =loaded_model.predict(x_test)
    print ('=====State',State,'Predict Result=====')
    print ('accuracy:{0:0.5f}'.format(accuracy_score(y_test,result)))
    print ('================================\n')

#load Testing data and show data info
TestData0 = pd.read_csv(CSVFile0)
TestData1 = pd.read_csv(CSVFile1)
print ("State / counts")
print (TestData0['Target'].value_counts())
print (TestData1['Target'].value_counts(),'\n')


# load the model from disk
loaded_model = joblib.load(Learning_Model_Name)

# Do TrainingData Preprocessing and Results Showing
TrainingData_Preprocessing_Result(TestData0,'0')
TrainingData_Preprocessing_Result(TestData1,'1')

#Process Over#
print ('{0:0.5f}'.format(time.clock() -t0), "seconds process time")

