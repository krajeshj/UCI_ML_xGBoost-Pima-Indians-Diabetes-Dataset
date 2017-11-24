
# Repository : UCI_ML_xGBoost-Pima-Indians-Diabetes-Dataset

## Title: PIMA INDIANS DIABETES - UCI MACHINE LEARNING REPOSITORY
## Abstract
This dataset has been used to predict an onset of Diabetes in a sample of poulation of Pima Indians. xGboost algorith has been used to perform Binary classification.
The test data set has is 33% of the total data. This produced an accuracy of 77% on the test data.

# 

|    |   |
|:---|:---|
Data Set Characteristics|  Multivariate
Number of Instances|768
Characteristics|Integer, Real 
Number of Attributes|8 
Date Donated|1990-05-09 
Associated Tasks|Classification 
Missing Values|Yes 
### Source:
|Sources|Details|
|:---:|:---:|
|Original Owners|National Institute of Diabetes and Digestive and Kidney Diseases|
|Donor of database|Vincent Sigillito (vgs '@' aplcen.apl.jhu.edu) Research Center, RMI Group Leader Applied Physics Laboratory The Johns Hopkins University Johns Hopkins Road Laurel, MD 20707 (301) 953-6231|


#### Problem to Solve 
Predict the onset of Diabetes given  data such as plasama glucose concentration, bllod pressure, skin fold thikcness, BMI, diabetes Pedigree and Age

#### Client 
A client could be any doctor, medical  research professional,  public policy agencies interested in understanding the factors affecting health in certain demographic or medical insurance agencies needing to profile potential subscribers to analyze or forecast costs.
#### Data
The data used for the analysis will be as outlined in the Data Set Information below. The data will have 7 input variables and a 1 binary output 1 or 0 indicating onset of diabetes or not

#### Appraoch 
xGBoostClassifier will be used to perform binary classification on the dataset. The entire data set will be split into train and  test setin 67:33 ratio. A model will be created. The feature importance will be plotted.  And accuracy of the model will be measured


#### Deliverables
1. Jupyter notebook
2. Report outlining findings

### Data Set Information:
Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

#### Attribute Information:
|Feature Label | Description |
|:---:|:---|
F0 | Number of times pregnant
F1 | Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
F2 | Diastolic blood pressure (mm Hg) 
F3 |Triceps skin fold thickness (mm) F4 - 2-Hour serum insulin (mu U/ml)
F5 | Body mass index (weight in kg/(height in m)^2) 
F6 | Diabetes pedigree function
F7 | Age (years) Class variable (0 or 1)

### Files and Directories
|Directories | Description|
|:---:|:---|
|.| contains  this README.md file and the python notebook
|code| sub-directory to hold the Python code saved from Jupyter notebook
|data| sub-directory to hold   repository
|reports| final reports|

|File|Description
|---------|-------------------------------------------------------------------------------------------------------------------
|./xGBoost_pima_indians_diabetes.ipynb| Jupyter notebook viewable with nbviewer
|code/xGBoost_pima_indians_diabetes.py | Main python program  file saved from notebook
|data/pima-indians-diabetes.txt|  Text file containing the data seperated by comma
 
 |Sl. no. |Reference |
 :---|:---|
 1|<https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes>
 
 



