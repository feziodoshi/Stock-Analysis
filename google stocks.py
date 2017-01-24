import pandas as pd
import numpy as np
from sklearn import preprocessing , cross_validation ##cross_validation helps in statistics by shuffling the data
from sklearn import svm ##can use svm to do regression
from sklearn.linear_model import LinearRegression
import quandl
import pickle
import math
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


df=quandl.get('WIKI/GOOGL')
df=df[['Adj. Open' , 'Adj. High'  ,   'Adj. Low' ,  'Adj. Close'    ,  'Volume'  ]]


##save_file=open('pic_algo/quand_df.pickle','wb')
##pickle.dump(df,save_file)
##save_file.close()

open_file=open('pic_algo/quand_df.pickle','rb')
df=pickle.load(open_file)
open_file.close()

df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low']*100
df['PCT_CHG']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100
df=df[['Adj. Close','HL_PCT','PCT_CHG','Volume']]
#########however this Adj close for that day cannot be the label as it is used
########## to calculate HL_PCT and PCT_CHG
###so for the output labels what we can do is simply get adj close of future
##lets output data for about after 30 business days
##so we create a new output label
forecast_col='Adj. Close' 
forecast_val=int(math.ceil(0.01*len(df)))
df['labels']=df[forecast_col].shift(-forecast_val)
##df.fillna(-999999,inplace=True)


##FEATURES:X
##LABELS:y

X=np.array(df.drop(['labels'],1))
X=preprocessing.scale(X)
X_lately=X[-forecast_val:]
X=X[:-forecast_val]

df.dropna(inplace=True)
y=np.array(df['labels'])



X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)


##clf=LinearRegression(n_jobs = -1)
##clf.fit(X_train,y_train)

##save_file=open('pic_algo/Linear_model.pickle','wb')
##pickle.dump(clf,save_file)
##save_file.close()

open_file=open('pic_algo/Linear_model.pickle','rb')
clf=pickle.load(open_file)
open_file.close()

acc=clf.score(X_test,y_test)

forecast_output=clf.predict(X_lately)
print(forecast_output)

