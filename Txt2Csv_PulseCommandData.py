
# coding: utf-8

# In[3]:


#-*-coding:utf-8 -*-
#This Program for Making Origin Training Data 
import csv
import time
t0=time.clock()

#RawDataName&CSVFilesName Setting
RawData = r'D:\RFdata\Others\1T.txt'
CSVFile1 = r'D:\RFdata\Others\1T.csv'

RawData0 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120.txt'
RawData1 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1.txt'
RawData2 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2.txt'
RawData3 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3.txt'
CSVFile = r'D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\120BagPerMin\PulseCommand120_10k_new.csv'
DataSize = 2500
DataNum = 0
OpenFileFlag = True
#====================================================
def makeLearningData(RawData, CSVFile, State, DataSize, OpenFileFlag):
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
            listTem=[]
            listTem.append(line.split()+[State])
            csv_write.writerows(listTem)
            DataNum = DataNum+1
        
    out.close()
    txtRead.close()   
    print("Write file over！")
    return False
#====================================================
#OpenFileFlag = makeLearningData(RawData0, CSVFile,'0', DataSize,OpenFileFlag)
#OpenFileFlag = makeLearningData(RawData1, CSVFile,'1', DataSize,OpenFileFlag)
#OpenFileFlag = makeLearningData(RawData2, CSVFile,'2', DataSize,OpenFileFlag)
#OpenFileFlag = makeLearningData(RawData3, CSVFile,'3', DataSize,OpenFileFlag)

CSVFileTem=CSVFile1
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



print time.clock() -t0, "seconds process time"


# In[27]:


#-*-coding:utf-8 -*-
#This Program for Making Origin Testing Data 
import csv
import time
t0=time.clock()

#RawDataName&CSVFilesName Setting
RawData0 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_NormalData120_Test.txt'
RawData1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_1_Test.txt'
RawData2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_2_Test.txt'
RawData3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_3_Test.txt'
Testdata0 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_0_ALLData.csv'
Testdata1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_1_ALLData.csv'
Testdata2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_2_ALLData.csv'
Testdata3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_3_ALLData.csv'
DataSize = 10000
RawData=''
TestData=''
#====================================================
def makeTestData(RawData, Testdata, State, DataSize):
    TestDataTem=Testdata
    txtRead=open(RawData,'r')
    out=open(TestDataTem,'wb') 
    csv_write=csv.writer(out,dialect='excel') 
    lines=txtRead.readlines()
    #各資訊名稱寫入第一行
    columns=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','Target'] #0:Normal; 1,2,3:UnNormal
    csv_write.writerow(columns)
    DataNum = 0
    
    for line in lines[50000:]:    
        if DataNum < DataSize:
            listTem=[]
            listTem.append(line.split()+[State])
            csv_write.writerows(listTem)
            DataNum = DataNum+1
        
    out.close()
    txtRead.close()   
    print("Write file over！")
#====================================================
makeTestData(RawData0,Testdata0,'0',DataSize)
makeTestData(RawData1,Testdata1,'1',DataSize)
makeTestData(RawData2,Testdata2,'2',DataSize)
makeTestData(RawData3,Testdata3,'3',DataSize)


print time.clock() -t0, "seconds process time"


# In[21]:


#-*-coding:utf-8 -*-
#Get Peak Value Training Data 
import csv
import time
import numpy as np
import pandas as pd
t0=time.clock()

#RawDataName&CSVFilesName Setting
RawData0 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120.txt'
RawData1 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1.txt'
RawData2 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2.txt'
RawData3 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3.txt'

RawData0_1 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_1.txt'
RawData1_1 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_1.txt'
RawData2_1 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_1.txt'
RawData3_1 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_1.txt'

RawData0_2 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_2.txt'
RawData1_2 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_2.txt'
RawData2_2 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_2.txt'
RawData3_2 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_2.txt'

RawData0_3 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_3.txt'
RawData1_3 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_3.txt'
RawData2_3 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_3.txt'
RawData3_3 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_3.txt'

RawData0_4 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_4.txt'
RawData1_4 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_4.txt'
RawData2_4 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_4.txt'
RawData3_4 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_4.txt'

RawData0_5 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_5.txt'
RawData1_5 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_5.txt'
RawData2_5 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_5.txt'
RawData3_5 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_5.txt'

RawData0_6 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_6.txt'
RawData1_6 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_6.txt'
RawData2_6 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_6.txt'
RawData3_6 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_6.txt'

RawData0_7 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_7.txt'
RawData1_7 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_7.txt'
RawData2_7 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_7.txt'
RawData3_7 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_7.txt'

RawData0_8 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_8.txt'
RawData1_8 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_8.txt'
RawData2_8 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_8.txt'
RawData3_8 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_8.txt'

RawData0_9 = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120_9.txt'
RawData1_9 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal1\PulseCommand_UnNormalData120_1_9.txt'
RawData2_9 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal2\PulseCommand_UnNormalData120_2_9.txt'
RawData3_9 = 'D:\RFdata\DeltaData\PulseCommandDatas\UnNormal3\PulseCommand_UnNormalData120_3_9.txt'

PeakValueFrom = 'D:\RFdata\DeltaData\PulseCommandDatas\Normal\PulseCommand_NormalData120.csv'
CSVFile = r'D:\RFdata\DeltaData\PulseCommandDatas\CsvFiles\120BagPerMin\PulseCommand120_Peak_100k.csv'
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
PeakValue = findPeakValue(RawData0, PeakValueFrom)

OpenFileFlag = makeLearningData(RawData0, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_1, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_1, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_1, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_1, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_2, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_2, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_2, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_2, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_3, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_3, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_3, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_3, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_4, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_4, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_4, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_4, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_5, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_5, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_5, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_5, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_6, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_6, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_6, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_6, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_7, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_7, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_7, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_7, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_8, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_8, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_8, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_8, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

OpenFileFlag = makeLearningData(RawData0_9, CSVFile,'0', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData1_9, CSVFile,'1', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData2_9, CSVFile,'2', PeakValue, DataSize,OpenFileFlag)
OpenFileFlag = makeLearningData(RawData3_9, CSVFile,'3', PeakValue, DataSize,OpenFileFlag)

print time.clock() -t0, "seconds process time"


# In[25]:


#-*-coding:utf-8 -*-
#This Program for Making Peak Testing Data 
import csv
import time
t0=time.clock()

#RawDataName&CSVFilesName Setting
RawData0 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_NormalData120_Test.txt'
RawData1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_1_Test.txt'
RawData2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_2_Test.txt'
RawData3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_3_Test.txt'

RawData0_1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_NormalData120_Test1.txt'
RawData1_1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_1_Test1.txt'
RawData2_1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_2_Test1.txt'
RawData3_1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_3_Test1.txt'

RawData0_2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_NormalData120_Test2.txt'
RawData1_2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_1_Test2.txt'
RawData2_2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_2_Test2.txt'
RawData3_2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_3_Test2.txt'

RawData0_3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_NormalData120_Test3.txt'
RawData1_3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_1_Test3.txt'
RawData2_3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_2_Test3.txt'
RawData3_3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\TestRawData\PulseCommand_UnNormalData120_3_Test3.txt'

TestData0 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_0.csv'
TestData1 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_1.csv'
TestData2 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_2.csv'
TestData3 = r'D:\RFdata\DeltaData\PulseCommandDatas\TestData\120BagPerMin\PulseCommand_TestData120_Peak_3.csv'
DataSize = 2500
PeakValue = 350.96
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
#Get State 0 for 10000 piece of Test Data
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData0, TestData0, '0', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData0_1, TestData0, '0', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData0_2, TestData0, '0', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData0_3, TestData0, '0', PeakValue, DataSize, OpenFileFlag)
#Get State 1 for 10000 piece of Test Data
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData1, TestData0, '1', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData1_1, TestData0, '1', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData1_2, TestData0, '1', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData1_3, TestData0, '1', PeakValue, DataSize, OpenFileFlag)
#Get State 2 for 10000 piece of Test Data
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData2, TestData0, '2', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData2_1, TestData0, '2', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData2_2, TestData0, '2', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData2_3, TestData0, '2', PeakValue, DataSize, OpenFileFlag)
#Get State 1 for 10000 piece of Test Data
OpenFileFlag = True
OpenFileFlag = makeTestData(RawData3, TestData0, '3', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData3_1, TestData0, '3', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData3_2, TestData0, '3', PeakValue, DataSize, OpenFileFlag)
OpenFileFlag = makeTestData(RawData3_3, TestData0, '3', PeakValue, DataSize, OpenFileFlag)


print time.clock() -t0, "seconds process time"

