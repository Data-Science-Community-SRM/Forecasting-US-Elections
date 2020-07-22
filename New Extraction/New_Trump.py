import tweepy 
import pandas as pd

consumer_key= "XXX"
consumer_secret  = "XXX"
access_token ="XXX"
access_token_secret= "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth,wait_on_rate_limit = True)


date1 = "2020-07-09"  #Date from which you need to extract tweets
date2 = "2020-07-22"  #Date till when you need to extract tweets

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
    for tweet in tweepy.Cursor(api.search , q=word,count =1000,lang="en",since_id = date1,until = date2,tweet_mode = 'extended').items():
        print(tweet.created_at)  #Date at which it was tweet
        date.append(tweet.created_at)
        print(tweet.id)          #Unique ID of tweet
        user_id.append(tweet.id)
        print(tweet.user.verified)   #If user who tweet is verified or not
        verified.append(tweet.user.verified)
        print(tweet.full_text)   #To get full text of the tweet
        text.append(tweet.full_text)
        print(tweet.user.screen_name)  #User screen name
        user.append(tweet.user.screen_name)
        print(tweet.user.location)     #Location from where the tweet came
        location.append(tweet.user.location)
        print(tweet.source)            #Which twitter application was used to tweet
        source.append(tweet.source)
        print(tweet.favorite_count)     #Number of likes on the tweet
        likes.append(tweet.favorite_count)
        print(tweet.user.followers_count)    #Number of followers of the user
        followers.append(tweet.user.followers_count)
        print(tweet.user.friends_count)      #Number of following by the user
        following.append(tweet.user.friends_count)
        print(tweet.retweet_count)               #Number of the retweets of the original tweet
        retweets.append(tweet.retweet_count)
    
        print('<--------------------------------------------------->')
        count+=1
        print(count)
    
get_tweets(date1,date2,"#trump"+" -filter:retweets") #Filtering out retweets to avoid duplication
           
data = list(zip(date,user_id,verified,text,user,location,source,likes,followers,following,retweets))
df = pd.DataFrame(data =data, columns =["Date","Tweet_id","Verified","Tweet",
                                   "User","Location","Source","Likes","Followers","Following","Retweets"])
df.to_csv('Trump_No_Retweet_Full_Text.csv',index = False)

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
    for tweet in tweepy.Cursor(api.search , q=word,count =1000,lang="en",since_id = date1,until = date2,tweet_mode = 'extended').items():
        print(tweet.created_at)
        date.append(tweet.created_at)
        print(tweet.id)
        user_id.append(tweet.id)
        print(tweet.user.verified)
        verified.append(tweet.user.verified)
        print(tweet.full_text)
        text.append(tweet.full_text)
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
    
get_tweets(date1,date2,"#trump"+" -filter:retweets") 

           
data = list(zip(date,user_id,verified,text,user,location,source,likes,followers,following,retweets))
df1 = pd.DataFrame(data =data, columns =["Date","Tweet_id","Verified","Tweet",
                                   "User","Location","Source","Likes","Followers","Following","Retweets"])
df1.to_csv('Trump_No_Retweet_Full_Text_2.csv',index=False)         


date1 = "2020-07-13"
date2 = "2020-07-16"

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
    for tweet in tweepy.Cursor(api.search , q=word,count =1000,lang="en",since_id = date1,until = date2,tweet_mode = 'extended').items():
        print(tweet.created_at)
        date.append(tweet.created_at)
        print(tweet.id)
        user_id.append(tweet.id)
        print(tweet.user.verified)
        verified.append(tweet.user.verified)
        print(tweet.full_text)
        text.append(tweet.full_text)
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
    
get_tweets(date1,date2,"#trump"+" -filter:retweets") 

           
data = list(zip(date,user_id,verified,text,user,location,source,likes,followers,following,retweets))
df2 = pd.DataFrame(data =data, columns =["Date","Tweet_id","Verified","Tweet",
                                   "User","Location","Source","Likes","Followers","Following","Retweets"])
df2.to_csv('Trump_No_Retweet_Full_Text_3.csv',index=False)