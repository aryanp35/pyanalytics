# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
result = pd.read_csv('denco.csv')
result
result.columns
df=result

df1=df.groupby('custname').size()
df1
df2=df.groupby('custname').agg({ "custname" : ["count"] })
df2


df3=df.pivot_table(aggfunc ={'revenue':np.sum},index=['custname'])
df3.sort_values('revenue',ascending=False)


df4=df.pivot_table(index=["partnum"],aggfunc ={'revenue':np.sum})
df4.sort_values('revenue',ascending= False)

df5=df.pivot_table(index=["partnum"],aggfunc ={'margin':np.sum})
df5.sort_values('margin',ascending= False)

