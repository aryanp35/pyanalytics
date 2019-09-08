# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:35:15 2019

@author: Aryan
"""

from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')

df1 = mtcars[['mpg','wt','hp']]
IV = df1[['wt','hp']].values
IV
DV= df1['mpg'].values
DV
IV_train, IV_test, DV_train, DV_test = train_test_split(IV, DV,test_size=0.2, random_state=123)
IV_train

MTmodel2a = lm.LinearRegression()
MTmodel2a.fit(IV_train, DV_train)
MTmodel2a.intercept_
MTmodel2a.coef_
predicted2a = MTmodel2a.predict(IV_test)
predicted2a


