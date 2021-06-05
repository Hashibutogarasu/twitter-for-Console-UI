import sys
import time
import json
import tweepy

from twitterfunc import twitterfunc as tw

def connect():
    try:
        json_open = open('./twitterfunc/key_config.json', 'r')
        json_load = json.load(json_open)

        ck = json_load['api_key']
        cs = json_load['api_key_secret']
        at = json_load['access_token']
        ats = json_load['access_token_secret']
        
        auth = tweepy.OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)
        api = tweepy.API(auth)
        me = api.me()
        return api
    except:
        print('[Error]keyが設定されていません。\nkey_config.jsonに正しいキーを入力してください。')
        key_data = {'api_key': '', 'api_key_secret': '', 'access_token': '','access_token_secret':''}

        with open('./twitterfunc/key_config.json', 'w') as f:
            json.dump(key_data, f, indent=2, ensure_ascii=False)
        
        sys.exit()


def twchelp(api):
	content = ("twitter-for-CUI help\ntimeline:タイムラインを表示出来ます。\ntweet:ツイートが出来ます。\nretweet:リツイートが出来ます。\nfavorite:いいねが出来ます。\nfollow:フォローが出来ます。\nunfollow:フォロー解除が出来ます。\nuser_info:ユーザーの詳細を確認できます。\n更なる詳細は\nhttps://github.com/Hashibutogarasu/twitter-for-Console-UI\nで確認できます。")
	print(content)

def close(api):
    sys.exit()


COMMANDS = {
    'timeline': tw.timeline,
    'TL': tw.timeline,
    'tweet': tw.tweet,
    'destroytweet':tw.tweetdestroy,
    'favorite': tw.favorite,
    'retweet': tw.retweet,
    'follow':tw.follow,
    'unfollow':tw.unfollow,
    'user_info':tw.profile,
    'user_timeline':tw.user_timeline,
    'search':tw.search,
    'loginas':tw.loginas,
    'help':twchelp,
    'close':close

}

def main():
    api = connect()
    while True:
        command = input(">")
        if command in COMMANDS:
            COMMANDS[command](api)

if __name__ == "__main__":
    try:
	    main()
    except KeyboardInterrupt:
        print("Ctrl+Cが押されました。")