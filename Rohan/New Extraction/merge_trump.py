import pandas as pd

df = pd.read_csv(r'C:\Users\ROSHAN\DSC Project\Trump_No_Retweet_Full_Text.csv')

df1 = pd.read_csv(r'C:\Users\ROSHAN\DSC Project\Trump_No_Retweet_Full_Text_2.csv')

df2 = pd.read_csv(r'C:\Users\ROSHAN\DSC Project\Trump_No_Retweet_Full_Text_3.csv')

concat = [df, df1, df2]

result= pd.concat(concat)
result.to_csv('Trump_No_Retweet_Full_Text_Final.csv',index = False)

