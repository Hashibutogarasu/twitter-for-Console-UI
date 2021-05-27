import sys
import time
import tweepy

from twitterfunc import config
from twitterfunc import twitterfunc as tw


def connect():
  auth = tweepy.OAuthHandler(config.ck, config.cs)
  auth.set_access_token(config.at, config.ats)
  api = tweepy.API(auth)
  try:
    me = api.me()
  except:
  	print("キーが間違っています。")
  	sys.exit()
  return api


COMMANDS = {
    'timeline': tw.timeline,
    'TL': tw.timeline,
    'tweet': tw.tweet,
    'retweet': tw.retweet,
    'favorite': tw.favorite,
    'follow':tw.follow,
    'unfollow':tw.unfollow,
    'user_info':tw.profile
}

def main():
    api = connect()
    while True:
        command = input(">")
        if command in COMMANDS:
            COMMANDS[command](api)

if __name__ == "__main__":
	main()
