# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:07:20 2018

@author: Saqib kamal
"""

import numpy as np
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Sentiment Analysis Dataset.csv', error_bad_lines=False , encoding='latin-1')
dataset = dataset.drop('SentimentSource', 1)
dataset = dataset.drop('ItemID', 1)
dataset=dataset.drop(dataset.index[[i+1 for i in range(30000,1578610)]])
dataset['length'] = dataset[ 'SentimentText'].apply(len)
text_feat = dataset['SentimentText'].copy()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer("english")
features = vectorizer.fit_transform(text_feat)
lf = dataset['length'].as_matrix()
newfeat = np.hstack((features.todense(),lf[:, None]))

#saving the vectorizer with pickle
import pickle
vt = vectorizer.fit(text_feat)
vettorizer = 'vettor_new.pkl'
llamas = open(vettorizer, 'wb')
pickle.dump(vt, llamas)
llamas.close()

#Splitting dataset into Trainig set and Test set
from sklearn.cross_validation import train_test_split 
X_train,X_test,Y_train,Y_test=train_test_split(newfeat,dataset['Sentiment'],train_size=0.75,random_state=30)

#Fitting the Classifier to the Training set
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB(alpha=0.3)
classifier.fit(X_train, Y_train)

#Predicting the test set result
Y_pred=classifier.predict(X_test)

#Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,Y_pred)


import pickle
tweets_classifier = 'tweets_classifier.pkl'
samas = open(tweets_classifier, 'wb')
pickle.dump(classifier, samas)
samas.close()





