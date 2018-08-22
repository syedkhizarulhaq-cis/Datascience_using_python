#https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/

#http://pandas.pydata.org/pandas-docs/stable/10min.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Creating a Series by passing a list of values, letting pandas create a default integer index:

s=pd.Series([1,3,5,np.nan,6,8])

#print(s)

dates = pd.date_range('20130101', periods=6)

#print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)


