import requests
print("YES")
BASE_URL = "http://127.0.0.1:5000" 
url = "http://127.0.0.1:5000/tweetfetch.php" 


years_exp = {"hashtag": '#hello'}

#response = requests.post("{}/predict".format(BASE_URL), json = years_exp)

response = requests.post("{}/get_tweet".format(BASE_URL), json = years_exp)

print(response)

#print(response.json())