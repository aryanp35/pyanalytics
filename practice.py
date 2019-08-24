# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:31:34 2019

@author: Aryan
"""

#myplot.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.savefig('plot2.png')
plt.savefig('D:\pyWork\plots\plot1.png')
plt.show(); # import when running from script

import matplotlib.image as mpimg
img = mpimg.imread('plot2.png')
print(img)
imgplot = plt.imshow(img)
