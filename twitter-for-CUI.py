import sys
import time
import tweepy

from twitterfunc import config
from twitterfunc import twitterfunc as tw


def connect():
  auth = tweepy.OAuthHandler(config.ck, config.cs)
  auth.set_access_token(config.at, config.ats)
  api = tweepy.API(auth)
  me = api.me()
  return api


def twchelp(api):
	content = ("twitter-for-CUI help\ntimeline:タイムラインを表示出来ます。\ntweet:ツイートが出来ます。\nretweet:リツイートが出来ます。\nfavorite:いいねが出来ます。\nfollow:フォローが出来ます。\nunfollow:フォロー解除が出来ます。\nuser_info:ユーザーの詳細を確認できます。\n更なる詳細は\nhttps://github.com/Hashibutogarasu/twitter-for-Console-UI\nで確認できます。")
	print(content)


COMMANDS = {
    'timeline': tw.timeline,
    'TL': tw.timeline,
    'tweet': tw.tweet,
    'retweet': tw.retweet,
    'favorite': tw.favorite,
    'follow':tw.follow,
    'unfollow':tw.unfollow,
    'user_info':tw.profile,
    'help':twchelp,
    'destroytweet':tw.tweetdestroy,
    'user_timeline':tw.user_timeline
}

def main():
    api = connect()
    while True:
        command = input(">")
        if command in COMMANDS:
            COMMANDS[command](api)

if __name__ == "__main__":
	main()
