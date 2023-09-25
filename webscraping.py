import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

#Define diretório local
os.chdir("D:/PUC BD/P4/Projeto")

#Faz a raspagem dos Twitters até um limite máximo definido
maxTweets = 100000000
i = 0
tweets_list = []
for tweet in sntwitter.TwitterSearchScraper('#NetflixBrasil since:2022-09-03  until:2023-01-03').get_items():
  if i > maxTweets:
    break
  tweets_list.append([tweet.date, tweet.url, tweet.user.username, tweet.rawContent])
  i = i + 1


#Tranforma o resultado da raspagem dos dados em data frame
tweets_df = pd.DataFrame(tweets_list, columns=['date', 'url','username', 'content' ])

#Exporta data frame como .CSV para diretório local
tweets_df.to_csv('Tweet.csv', encoding = 'utf-8', index = False)
