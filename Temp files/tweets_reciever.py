# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:13:54 2018

@author: Saqib kamal
"""

import numpy as np
import pandas as pd
import pickle

#import saved model
saved_model = open('tweets_classifier.pkl', 'rb')
classifier = pickle.load(saved_model)

#import saved vectorizer
saved_vectorer = open('vettor_new.pkl', 'rb')
vt = pickle.load(saved_vectorer)

sample = ['  Feeling strangely fine. Now Im gonna go listen to some Semisonic to celebrate']
x = pd.DataFrame({'Sentiment':sample})
x['length'] = x['Sentiment'].apply(len)
y = x.Sentiment.astype(str)
sample2 = vt.transform(y)
lf = x['length'].as_matrix()
newfeat = np.hstack((sample2.todense(),lf[:, None]))


test_pred = classifier.predict(newfeat)
