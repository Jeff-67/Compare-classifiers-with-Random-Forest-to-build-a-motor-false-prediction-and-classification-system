#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:35:10 2018

@author: JEFF
"""
 
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn.externals import joblib 

path = '/Users/Apple/Desktop/MLData/PulseCommand120_Peak.csv'
path1 = '/Users/Apple/Desktop/MLData/PulseCommand_TestData120_Peak_0.csv'
path2 = '/Users/Apple/Desktop/MLData/PulseCommand_TestData120_Peak_1.csv'
path3 = '/Users/Apple/Desktop/MLData/PulseCommand_TestData120_Peak_2.csv'
path4 = '/Users/Apple/Desktop/MLData/PulseCommand_TestData120_Peak_3.csv'
saved_model1 = '/Users/Apple/Desktop/MLData/AllKNNMODEL_120_Peak.sav'

def main():
    
    DATA = pd.read_csv(path)
    data = pd.read_csv(path1)
    data1 = pd.read_csv(path2)
    data2 = pd.read_csv(path3)
    data3 = pd.read_csv(path4)
    
    y_train = np.array(DATA['Target'])
    
    x_train = DATA.drop('Target',axis=1).values
    
    y_test1 = np.array(data['Target'])
    
    x_test1 = data.drop('Target',axis=1).values
    
    y_test2 = np.array(data1['Target'])
    
    x_test2 = data1.drop('Target',axis=1).values
    
    y_test3 = np.array(data2['Target'])
    
    x_test3 = data2.drop('Target',axis=1).values
    
    y_test4 = np.array(data3['Target'])
    
    x_test4 = data3.drop('Target',axis=1).values
    
    knn = KNeighborsClassifier()
    
    knn.fit(x_train,y_train)
    
    y_predict_knn1 = knn.predict(x_test1)
    
    y_predict_knn2 = knn.predict(x_test2)
    
    y_predict_knn3 = knn.predict(x_test3)
    
    y_predict_knn4 = knn.predict(x_test4)
    
    dct = DecisionTreeClassifier()
    
    dct.fit(x_train,y_train)
    
    y_predict_dct1 = dct.predict(x_test1)
    
    y_predict_dct2 = dct.predict(x_test2)
    
    y_predict_dct3 = dct.predict(x_test3)
    
    y_predict_dct4 = dct.predict(x_test4)
    
    svm = SVC()
    
    svm.fit(x_train,y_train)
    
    y_predict_svm1 = svm.predict(x_test1)
    
    y_predict_svm2 = svm.predict(x_test2)
    
    y_predict_svm3 = svm.predict(x_test3)
    
    y_predict_svm4 = svm.predict(x_test4)
    
    
    joblib.dump(knn,saved_model1,compress=3)
        
    a = {accuracy_score(y_test1,y_predict_knn1),accuracy_score(y_test2,y_predict_knn2),accuracy_score(y_test3,y_predict_knn3),accuracy_score(y_test4,y_predict_knn4)}
    

        
    yy1 = np.array([accuracy_score(y_test1,y_predict_knn1),accuracy_score(y_test2,y_predict_knn2),accuracy_score(y_test3,y_predict_knn3),accuracy_score(y_test4,y_predict_knn4)])
    yy2 = np.array([accuracy_score(y_test1,y_predict_dct1),accuracy_score(y_test2,y_predict_dct2),accuracy_score(y_test3,y_predict_dct3),accuracy_score(y_test4,y_predict_dct4)])
    yy3 = np.array([accuracy_score(y_test1,y_predict_svm1),accuracy_score(y_test2,y_predict_svm2),accuracy_score(y_test3,y_predict_svm3),accuracy_score(y_test4,y_predict_svm4)])
    yy4 = np.array([0.99932,0.73406,1,0.80921])
    plt.plot(xx,yy4,'r',label='Random_Forest',linewidth=7.0)
    plt.plot(xx,yy2,'g',label='Decision_Tree')
    plt.plot(xx,yy1,'y',label='KNN')
    plt.plot(xx,yy3,'b',label='SVM')
    plt.xticks([0,1,2,3])
    plt.ylim(0.5,1)
    plt.ylabel("accuracy")
    plt.xlabel("data_case")
    plt.title("Acuuracy scores compared with several methods")
    plt.legend(loc='best')
    plt.show()
    
    print('knn_accuracy_for_state_0:{0:0.5f}'.format(accuracy_score(y_test1,y_predict_knn1)))
    print('knn_accuracy_for_state_1:{0:0.5f}'.format(accuracy_score(y_test2,y_predict_knn2)))
    print('knn_accuracy_for_state_2:{0:0.5f}'.format(accuracy_score(y_test3,y_predict_knn3)))
    print('knn_accuracy_for_state_3:{0:0.5f}'.format(accuracy_score(y_test4,y_predict_knn4)))
    print('dct_accuracy_for_state_0:{0:0.5f}'.format(accuracy_score(y_test1,y_predict_dct1)))
    print('dct_accuracy_for_state_1:{0:0.5f}'.format(accuracy_score(y_test2,y_predict_dct2)))
    print('dct_accuracy_for_state_2:{0:0.5f}'.format(accuracy_score(y_test3,y_predict_dct3)))
    print('dct_accuracy_for_state_3:{0:0.5f}'.format(accuracy_score(y_test4,y_predict_dct4)))
    print('svm_accuracy_for_state_0:{0:0.5f}'.format(accuracy_score(y_test1,y_predict_svm1)))
    print('svm_accuracy_for_state_1:{0:0.5f}'.format(accuracy_score(y_test2,y_predict_svm2)))
    print('svm_accuracy_for_state_2:{0:0.5f}'.format(accuracy_score(y_test3,y_predict_svm3)))
    print('svm_accuracy_for_state_3:{0:0.5f}'.format(accuracy_score(y_test4,y_predict_svm4)))
    
    print('knn_f1_score:',roc_auc_score(y_test1,y_predict_knn1))
    
    print('dct_f1_score:',roc_auc_score(y_test1,y_predict_dct1))
    
    print('svm_f1_score:',roc_auc_score(y_test1,y_predict_svm1))
    
    xx = np.array([0,1,2,3])
    yy1 = np.array([accuracy_score(y_test1,y_predict_knn1),accuracy_score(y_test1,y_predict_knn2),y_test3,y_predict_knn3,y_test4,y_predict_knn4])
    yy2 = np.array([accuracy_score(y_test1,y_predict_dct1,accuracy_score(y_test2,y_predict_dct2,accuracy_score(y_test3,y_predict_dct3,accuracy_score(y_test4,y_predict_dct4])
    yy3 = np.array([accuracy_score(y_test1,y_predict_svm1,accuracy_score(y_test2,y_predict_svm2,accuracy_score(y_test3,y_predict_svm3,accuracy_score(y_test4,y_predict_svm4])
    yy4 = np.array([randomforest_1,randomforest_2,randomforest_3,randomforest_4])
    plt.plot(xx,yy1,'y',label='Speed(CH1+CH5+CH6)	')
    plt.plot(xx,yy2,'g',label='Torque(CH3+CH4+CH7)')
    plt.plot(xx,yy3,'b',label='Speed+Torque')
    plt.plot(xx,yy4,'r',label='Speed+Torque+Position+Vbus')
    plt.xticks([0,1,2,3])
    plt.ylim(0,1)
    plt.ylabel("accuracy")
    plt.xlabel("data_case")
    plt.title("Acuuracy scores depends on various features")
    plt.legend(loc=4)
    plt.show()
if __name__ == '__main__':
    
    main()
    
    
