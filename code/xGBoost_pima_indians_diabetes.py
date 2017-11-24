
# coding: utf-8

# ### PIMA INDIANS DIABETES - UCI MACHINE LEARNING REPOSITORY
# 
# Abstract: From National Institute of Diabetes and Digestive and Kidney Diseases; 
# 
# Data Set Characteristics:  Multivariate
# Number of Instances:768
# Area:Life
# Attribute Characteristics:Integer, Real
# Number of Attributes:8
# Date Donated:1990-05-09
# Associated Tasks:Classification
# Missing ValuesYes
# Number of Web Hits:339124
# 
# Source:
# Original Owners: 
# 
# National Institute of Diabetes and Digestive and Kidney Diseases 
# 
# Donor of database: 
# 
# Vincent Sigillito (vgs '@' aplcen.apl.jhu.edu) 
# Research Center, RMI Group Leader 
# Applied Physics Laboratory 
# The Johns Hopkins University 
# Johns Hopkins Road 
# Laurel, MD 20707 
# (301) 953-6231
# 
# Data Set Information:
# Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage. ADAP is an adaptive learning routine that generates and executes digital analogs of perceptron-like devices. It is a unique algorithm; see the paper for details.
# 
# 
# #### Attribute Information:
# F0 - Number of times pregnant 
# F1 - Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
# F2 - Diastolic blood pressure (mm Hg) 
# F3 - Triceps skin fold thickness (mm) 
# F4 - 2-Hour serum insulin (mu U/ml) 
# F5 - Body mass index (weight in kg/(height in m)^2) 
# F6 - Diabetes pedigree function 
# F7 - Age (years) 
# Class variable (0 or 1) 
.
# ##### import the packages 

# In[1]:

from xgboost import XGBClassifier
import numpy as np
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score 
from matplotlib import pyplot 
from xgboost import plot_importance




# In[ ]:

###### read in the data into a np array


# In[ ]:

dataset = np.genfromtxt('../data/pima-indians-diabetes.txt',delimiter=",")
X=  dataset[:,0:8]
Y = dataset[:,8]


# ####### partition the data into training set and test holdout sets

# In[3]:

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=test_size, random_state=seed)


# ######## use a XGBoost classifer 

# In[ ]:

model=XGBClassifier(learning_rate=0.001, silent=False)
model.fit(X_train, y_train, verbose=True, eval_metric="error")


# ##### Plot the imortant features of the model

# In[4]:


plot_importance(model)
pyplot.show()


# In[ ]:

F0 - Number of times pregnant 
F1 - Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
F2 - Diastolic blood pressure (mm Hg) 
F3 - Triceps skin fold thickness (mm) 
F4 - 2-Hour serum insulin (mu U/ml) 
F5 - Body mass index (weight in kg/(height in m)^2) 
F6 - Diabetes pedigree function 
F7 - Age (years) 


# In[5]:

X_train[:3,:]


# In[6]:

print(model)


# In[7]:

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]


# In[8]:

accuracy = accuracy_score(y_test, predictions)


# In[9]:

print("Accuracy: %.2f%%" %(accuracy * 100.00))


# In[ ]:




# In[ ]:




# In[ ]:



