# Using Random forest to design an on-line electrical motor false classifying and predicting system
# Abstract
  Electric motors are the important power source for intelligent manufacturing; however, motor eccentric is a serious problem that will occurs when robots or machine have operate for a while. This fault will cause damage to power modules, but traditional solutions were mostly depends on expensive sensors and the are not able to make a precise presdiction. In this project, we will foucus on the eccentricity fault by collecting big data and do the further classification and prediction based on Random Forest.
  
  <a href="https://github.com/JEFF0824/Using-Random-forest-to-design-an-on-line-electrical-motor-false-diagnose-and-predict-system/blob/master/ProjectForALL%20.py" target="_blank">Here</a> is the code!!
  
# Guide line

> [Data introduction](#data-introduction) 

  - Real time raw data
  
  - Features extraction
 

> [Model training](#model-training) 

  - Random Forest algorithm intriduction
  
  - training and test data preprocessing
  
  - Feature filtering
  
  - Data size choosing
  
  - hyper parameter tunning
  
  - Status Voting Method

> [Why Random Forest?](#why-random-forest)

  - Compare with other algorithm

> [Conclusion](#conclusion)

# Data introduction
A proper data of electrical motor false classification consists of the real-time operating raw data and controlling command of rolling element bearings via the acquisition station (shown in Fig.1), data processing, feature extraction from the data sets and classification into functional (State0) or defective (State1, State2, State3) status (shown in Fig.2) of rolling element bearing. To be more specific, I get the data from a real packing machine motor.

| <a>**Entire process of collecting big data**</a> | <a>**Status definitions**</a> 
| :---: |:---:| 
|![screen shot 2018-12-07 at 4 25 40 pm](https://user-images.githubusercontent.com/36265245/49637409-4490ee80-fa40-11e8-8e07-9aeb9335f3f8.png)    | ![screen shot 2018-12-07 at 4 29 11 pm](https://user-images.githubusercontent.com/36265245/49637415-465ab200-fa40-11e8-83f6-2790bd4622c2.png)
| <a>**Fig.1**</a> | <a>**Fig.2**</a> 

- Real time raw data

  Acquisitions of the rolling element bearing’s real-time raw data and controlling command from servo motor driver were performed on the     oscilloscope which is shown in Fig. 3. It provides 8 channels which have 16 bytes memory and 4KHz sampling frequency for each. Fig. 4     displays the acquisition’s rule of the training data which was set for appropriate experimental temperature, working time and             experimental station running speed.

  | <a>**Oscilloscope and command interface**</a> | <a>**Acquisition’s rule**</a> 
  | :---: |:---:| 
  |![screen shot 2018-12-07 at 4 29 41 pm](https://user-images.githubusercontent.com/36265245/49638044-00065280-fa42-11e8-9ef4-8c0de60c9a6f.png)  | ![screen shot 2018-12-07 at 4 47 12 pm](https://user-images.githubusercontent.com/36265245/49638046-009ee900-fa42-11e8-8d96-f227b8fa0909.png)
  | <a>**Fig.3**</a> | <a>**Fig.4**</a> 
  
- Features extraction

  Servo Driver provides many of real-time signals and commands which can be obtained from oscilloscope. I choose 8 motor related real-time information (all are in time domain) to be the features for model learning(shown in Fig.5).

  | <a>**The description of 8 channels for data acquisitions**</a> | 
  | :---: |
  |![screen shot 2018-12-07 at 5 11 02 pm](https://user-images.githubusercontent.com/36265245/49638483-36909d00-fa43-11e8-8106-825213179e31.png) | 
  | <a>**Fig.5**</a> | 
  
# Model training
Scikit-learn is an open-source machine learning software, which is easy to use. Scikit-learn provides classification, regression, clustering and dimensionality reduction libraries for python programming. I used Scikit-learn and random forests algorithm to classify rolling element bearing and motor condition and make prediction.

  - Random Forest algorithm intriduction
  
    <a href="https://github.com/JEFF0824/Using-Random-forest-to-design-an-on-line-electrical-motor-false-diagnose-and-predict-system/blob/master/RF_Model_Learning.py" target="_blank">Here</a> is the code!!
  
    The characteristics of random forest are adding an additional layer of randomness to bagging that constructing each tree using a different bootstrap sample of the data. Bagging is a well- known type of classification trees, which is that successive trees do not depend on earlier trees. Each tree is independently constructed using a bootstrap sample of the data set. In the end, a simple majority vote is taken for prediction. In standard decision trees, each node is split using the best split among all variables. In random forests, each node is split using the best among a subset of predictors randomly chosen at that node. This strategy makes random forest performing better than many other classifiers, including decision trees, discriminant analysis and support vector machines. Random forest is also robust against overfitting.
    
    ![screen shot 2018-12-07 at 9 58 15 pm](https://user-images.githubusercontent.com/36265245/49651837-4623dc00-fa6b-11e8-9c3c-39e30422af09.png)
    
  - training and test data preprocessing
 
    <a href="https://github.com/JEFF0824/Using-Random-forest-to-design-an-on-line-electrical-motor-false-diagnose-and-predict-system/blob/master/Txt2Csv_PulseCommandData.py" target="_blank">Here</a> is the code!!
   
    The training data used in this part are collected from the 10 groups of original training data sets which contains the four motor states and I selected 2500 volumes of data from every state containing the information about CH1 ~ CH8 randomly. Finally, a group of 10000 training data containing four states was obtained. The purpose of this step is to make the collection of training data become more various, so as to prove the credibility of training data.
    
    (Note: I deal with the test data in the same way, the volume of test data is 10000 at first also).
    
    ![screen shot 2018-12-07 at 10 33 23 pm](https://user-images.githubusercontent.com/36265245/49653522-2511ba00-fa70-11e8-8726-5c8b6851fc00.png)
    
    
    In addition to normal data preprocessing, I do the advance data preprocessing (Shown in Fig.6) and get the better prediction accuracy (Shown in Fig.7).
    
    CH1max :The maximum value of CH1 in the training data set 
    
    CH1min : The minimum value of CH1 in the training data set 
    
    CH1peak :The peak value of CH1 in the training data set 
    
    CH1peak = CH1max -((CH1max -CH1min)*2%)
   
    | <a>**Advance data preprocessing by focusing on the peak value**</a> | <a>**The comparison of different data preprocessing**</a> 
    | :---: |:---:| 
    | ![screen shot 2018-12-07 at 10 24 50 pm](https://user-images.githubusercontent.com/36265245/49653558-48d50000-fa70-11e8-9caa-0e5c8c9cf0d7.png)| ![screen shot 2018-12-07 at 10 38 22 pm](https://user-images.githubusercontent.com/36265245/49682922-71540d00-faf7-11e8-9feb-dacec4a853c5.png)
    | <a>**Fig.6**</a> | <a>**Fig.7**</a> 
    
  - Feature filtering
  
    In this part, I seperate all the features into four gruops (Shown in Fig.8 below), each of them is: speed relative features, location related features, torque related features and the other feature.
    After, I combine those feature cluster in various way (Shown in Fig.9 below), the result indicates that the combination of all features get the highest OOB_Score, thus I regard CH1~CH8 as the data features.
    
    | <a>**Features cluster**</a> | <a>**Result**</a> 
    | :---: |:---:| 
    |![screen shot 2018-12-07 at 10 53 23 pm](https://user-images.githubusercontent.com/36265245/49654558-18db2c00-fa73-11e8-9657-3b208bd6716e.png)| ![screen shot 2018-12-07 at 10 54 15 pm](https://user-images.githubusercontent.com/36265245/49654559-1a0c5900-fa73-11e8-93d5-5ed43ae589e9.png)
    | <a>**Fig.8**</a> | <a>**Fig.9**</a> 
    
  - Data size choosing
    
    The results of six kinds of data size are shown below, we can see that the prediction accuracy is the highest when the amount of training data is 100K, which proves that the more the amount of training data is, the better the training model will be.
    
    | <a>**The comparison of different data size**</a> | 
    | :---: |
    |![screen shot 2018-12-07 at 10 38 34 pm](https://user-images.githubusercontent.com/36265245/49682928-96e11680-faf7-11e8-967c-d9cb1c32a854.png)| 
    
  - hyper parameter tunning
  
    <a href="https://github.com/JEFF0824/Using-Random-forest-to-design-an-on-line-electrical-motor-false-diagnose-and-predict-system/blob/master/RFparametersTest.py" target="_blank">Here</a> is the code!!
    
    After doing proper feature extraction, training data preprocessing and deciding proper training data size, model improving is through hyper parameter tunning and determining the proper one by OOB_Score. I use the powerful function called `sklearn.model_selection.GridSearchCV` to run all the parameters fisrt and then narrow down to the parameter 'n_estimators'. Fig. 10 shows that in the case of n_estimators=70, the OOB_Score is 0.9389, which is the best score between n_estimators=10~80. At last, it can be seen in Fig. 11 that the prediction accuracy of each state of n_estimators=70 is 0.998, 0.9981, 0.9989 and 0.998, all are better than the case of n_estimators=10. Consequently, the learning model of this project is based on 8 features of real-time raw data and controlling command from servo motor driver, 100k pieces of training data size, advance data preprocessing of CH1 peak value and n_estimators=70.
    
    | <a>**OOB_Score of different n_estimators**</a> | <a>**Prediction accuracy of n_estimators=10,70**</a> 
    | :---: |:---:| 
    |![screen shot 2018-12-07 at 10 38 43 pm](https://user-images.githubusercontent.com/36265245/49683015-fb50a580-faf8-11e8-8498-0683f3132ec0.png)| ![screen shot 2018-12-07 at 10 38 53 pm](https://user-images.githubusercontent.com/36265245/49683016-fb50a580-faf8-11e8-9a12-f6dbca07cca5.png)
    | <a>**Fig.10**</a> | <a>**Fig.11**</a> 
    
  - Status Voting Method
  
    After constructing the learning model by random forest algorithm, status voting method is designed to make sure that the diagnosis prediction results are precise. Fig. 12 displays how the status voting method works, and beneath shows the algorithm:
    
    w0 = State0 votesnumber
    
    w1  = State1 votes number 
    
    w2  = State2 votes number
    
    w3  = State3 votes number
    
    w + w + w + w = 1000(totalvotesnumber)

    w  = max(w0,w1,w2,w3) 
    
    State_result = State(wmax)
    
    | <a>**The comparison of different data size**</a> | 
    | :---: |
    |![screen shot 2018-12-08 at 3 03 45 pm](https://user-images.githubusercontent.com/36265245/49683111-79617c00-fafa-11e8-9f51-dd7e2b035558.png)| 
    | <a>**Fig.12**</a> |
  
# Why Random Forest?
# Conclusion
