import os
import sys
import json
import tweepy

from twitterfunc import twitterfunc as tw

try:
    for env in os.environ:
        if str(env + ' : ' + os.environ.get(env)).startswith("USERPROFILE") == True:
            config_path = ((os.environ.get(env))+"\\twitter\\key_config.json")
            config_path = (config_path.replace("\\","/"))
            config_dir = (os.environ.get(env))+"\\twitter\\"
            config_dir = (config_dir.replace("\\","/"))
except:
    print("パスの取得に失敗しました。")
    sys.exit()


def connect():
    try:
        json_open = open(config_path, 'r')
        json_load = json.load(json_open)

        ck = json_load['api_key']
        cs = json_load['api_key_secret']
        at = json_load['access_token']
        ats = json_load['access_token_secret']

        default_image_path = json_load['default_image_path']

        json_open.close
        
        auth = tweepy.OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)
        api = tweepy.API(auth)
        me = api.me()
        print(f"ようこそ{me.name}さん")
        return api
    except:
        try:
            os.mkdir(config_dir)
        except:
            pass
        print('[Error]keyが設定されていません。\nkey_config.jsonに正しいキーを入力してください。')
        print('ここで設定を変更してください。\n',config_path)

        key_data = {'api_key': '', 'api_key_secret': '', 'access_token': '','access_token_secret':'','default_image_path':''}

        with open(config_path, 'w') as f:
            json.dump(key_data, f, indent=2, ensure_ascii=False)

        sys.exit()


def close(api):
    sys.exit()

def setting_path(api):
    json_path = config_path
    print("設定ファイルの場所:"+json_path)
    return json_path


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
    'help':tw.twchelp,
    'path':setting_path,
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
        print("\ntwitterを終了します。")