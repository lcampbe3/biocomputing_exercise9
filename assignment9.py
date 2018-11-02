#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:38:52 2018

@author: lcampbe3
"""
import numpy
import pandas
from plotnine import *

#1 Time Studied vs Test Score
study=pandas.read_csv("studying.txt", sep='\t',header=0)

a=ggplot(study, aes("Minutes Studied", "Test Score"))
a+geom_point()+coord_cartesian()+stat_smooth(method="lm")

#2
data=pandas.read_csv("data.txt", sep=',',header=0)
b=ggplot(data, aes(x="factor(region)",y="observations"))
b+geom_bar(stat="summary", fun_y=numpy.mean)+ylab("mean of observations")+xlab("region")

b+geom_point()+coord_cartesian()+geom_jitter()+xlab("region")

#Do the bar and scatter plots tell different stories?
#The bar graph of the averages makes it seem like all the regions have
#similar data. In the scatter plot, it is clear that there are
#nuances in the distribution of observations (for example the south has two
#distinct population groups, while the east and west are mor variable).