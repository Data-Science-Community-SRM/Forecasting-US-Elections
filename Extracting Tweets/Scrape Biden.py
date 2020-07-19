import tweepy 
import pandas as pd

consumer_key= "XXX"
consumer_secret  = "XXX"
access_token ="XXX"
access_token_secret= "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth,wait_on_rate_limit = True)


date1 = "2020-07-09"
date2 = "2020-07-19"


date =[]
user_id = []
verified = []
text = []
user = []
location = []
source = []
likes = []
followers = []
following = []
retweets = []


def get_tweets(date1,date2,word):
    count = 0
    for tweet in tweepy.Cursor(api.search , q=word,count =1000,lang="en",since_id = date1,until = date2).items():
        print(tweet.created_at)
        date.append(tweet.created_at)
        print(tweet.id)
        user_id.append(tweet.id)
        print(tweet.user.verified)
        verified.append(tweet.user.verified)
        print(tweet.text)
        text.append(tweet.text)
        print(tweet.user.screen_name)
        user.append(tweet.user.screen_name)
        print(tweet.user.location)
        location.append(tweet.user.location)
        print(tweet.source)
        source.append(tweet.source)
        print(tweet.favorite_count)
        likes.append(tweet.favorite_count)
        print(tweet.user.followers_count)
        followers.append(tweet.user.followers_count)
        print(tweet.user.friends_count)
        following.append(tweet.user.friends_count)
        print(tweet.retweet_count)
        retweets.append(tweet.retweet_count)
    
        print('<--------------------------------------------------->')
        count+=1
        print(count)
    
get_tweets(date1,date2,"#joebiden")  
           
data1 = list(zip(date,user_id,verified,text,user,location,source,likes,followers,following,retweets))
df1 = pd.DataFrame(data =data1, columns =["Date","Tweet_id","Verified","Tweet",
                                   "User","Location","Source","Likes","Followers","Following","Retweets"])

df1.to_csv('tweets_biden.csv')    