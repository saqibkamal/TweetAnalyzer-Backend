from flask import Flask,jsonify,request
import pandas as pd
import numpy as np 
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import string
import nltk
import subprocess
#from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle
from twython import Twython

from sklearn.naive_bayes import MultinomialNB
app = Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict():
	try:
		content = request.get_json()			
		messageContent = str(content["tweetjson"])
		sample = [messageContent]		 		 
		x = pd.DataFrame({'Sentiment':sample})
		x['length'] = x['Sentiment'].apply(len)
		print(sample)

		#import saved model
		saved_model = open('tweets_classifier.pkl', 'rb')
		mnb = pickle.load(saved_model)

		#import saved vectorizer
		saved_vectorer = open('vettor_new.pkl', 'rb')
		vt = pickle.load(saved_vectorer)

		y = x.Sentiment.astype(str)	 
		sample2 = vt.transform(y)
		lf = x['length'].as_matrix()
		newfeat = np.hstack((sample2.todense(),lf[:, None]))
		test_pred = mnb.predict(newfeat)

	except ValueError:
	 	return jsonify("Please enter a anumber.")
	return jsonify(test_pred.tolist())

@app.route("/get_tweet",methods=['POST'])
def get_tweet():
	try:
		content=request.get_json()
		hashtag=str(content["hashtag"])
		TWITTER_APP_KEY = '76NyujZAbenxlmzrPidy3luRs' 
		TWITTER_APP_KEY_SECRET = 'OKttshVQ8DQlcuXuVvJat0IRfo4q6Ati5fxzkJaVOT64uJjMvE' 
		TWITTER_ACCESS_TOKEN = '807155853577043968-hkVyPM2QCeRyfbyZYJrXySIuXeHDUH1'
		TWITTER_ACCESS_TOKEN_SECRET = 'hrcBWIzDHTUIrjeljK4bTOEJKzf8dpbOVGCsOmzVe7NGG'

		t = Twython(app_key=TWITTER_APP_KEY, 
		            app_secret=TWITTER_APP_KEY_SECRET, 
		            oauth_token=TWITTER_ACCESS_TOKEN, 
		            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

		search = t.search(q=hashtag,count=100)

		ans=""
		result=[]

		tweets = search['statuses']
		for tweet in tweets:
			ans+=" ~~~~~~~~~~~~~~~ " + tweet['text']
			result.append(tweet['text'])

	except ValueError:
	 	return jsonify(hashtag)
	return jsonify(ans)


if __name__ == '__main__':
	app.run()
 



