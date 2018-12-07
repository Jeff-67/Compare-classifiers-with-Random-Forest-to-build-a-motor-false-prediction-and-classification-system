# Using Random forest to design an on-line electrical motor false classifying and predicting system
# Abstract
  Electric motors are the important power source for intelligent manufacturing; however, motor eccentric is a serious problem that will occurs when robots or machine have operate for a while. This fault will cause damage to power modules, but traditional solutions were mostly depends on expensive sensors and the are not able to make a precise presdiction. In this project, we will foucus on the eccentricity fault by collecting big data and do the further classification and prediction based on Random Forest.
# Guide line
> [Data introduction](#data-introduction) 

> [Data processing](#data-processing)

  - Real time raw data
  
  - Features extraction
 

> [Model training](#model-training) 

  - Algorism intriduction
  
  - hyper parameter tunning

> [Why Random Forest?](#why-random-forest)

  - Compare with other algorithm

> [Conclusion](#conclusion)

# Data introduction
A proper data of electrical motor false classification consists of the real-time operating raw data and controlling command of rolling element bearings via the acquisition station (shown in Fig.1), data processing, feature extraction from the data sets and classification into functional (State0) or defective (State1, State2, State3) status (shown in Fig.2) of rolling element bearing. To be more specific, I get the data from a real packing machine motor.

| <a>**Entire process of collecting big data**</a> | <a>**Status definitions**</a> 
| :---: |:---:| 
|![screen shot 2018-12-07 at 4 25 40 pm](https://user-images.githubusercontent.com/36265245/49637409-4490ee80-fa40-11e8-8e07-9aeb9335f3f8.png)    | ![screen shot 2018-12-07 at 4 29 11 pm](https://user-images.githubusercontent.com/36265245/49637415-465ab200-fa40-11e8-83f6-2790bd4622c2.png)
| <a>**Fig.1**</a> | <a>**Fig.2**</a> 

# Data processing
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
# Why Random Forest?
# Conclusion
