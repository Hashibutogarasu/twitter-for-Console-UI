from pip._internal import main as _main
import importlib

def _import(name, module, ver=None):
    try:
        globals()[name] = importlib.import_module(module)
    except ImportError:
        try:
            if ver is None:
                _main(['install', module])
            else:
                _main(['install', '{}=={}'.format(module, ver)])
            globals()[name] = importlib.import_module(module)
        except:
            print("can't import: {}".format(module))
import os
print("[INFO]osライブラリをインポートしました。")

import sys
print("[INFO]sysライブラリをインポートしました。")

import time
print("[INFO]timeライブラリをインポートしました。")

try:
    import tweepy
    print("[INFO]tweepyライブラリをインポートしました。")
except:
    print("[WARN]お使いのPythonライブラリにtweepyライブラリがインストールされていません。")
    imp = input("[INFO]tweepyをインストールしますか？\nyでインストール\n")
    if (imp == "y"):
        _import('pd','tweepy', '3.10.0')
        print(pd)
        print("インストールが完了しました。\n一旦終了します。")
        time.sleep(1)
        sys.exit()
    else:
        print("キャンセルしました。")   
        time.sleep(1)
        sys.exit()

import webbrowser
print("[INFO]webbrowserライブラリをインポートしました。")

import urllib
print("[INFO]urllibライブラリをインポートしました。")

#キーなど
API_KEY = ''
API_KEY_SECRET = ''
access_token = ''
access_token_secret = ''


if __name__ == '__main__':

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True
    )
    
    try:
        me = api.me()
        print("\n認証が完了しました。\n")
        print('ようこそ  {}  @{}\n'.format(me.name,me.screen_name))
    except:
        print("ユーザー名を取得できませんでした。")
        print("キーがセットされていないまたはアカウントが使用不可になっている可能性があります。")
        print("Twitter for CUIを終了します。")
        time.sleep(1)
        sys.exit()
        
    while True:
        twitter_cui_command=input("Twitter for CUI:")
        if (twitter_cui_command == "Tweet") :
            select=input("画像を添付しますか？y/n\nDefault→n\nlogoutコマンドで終了できます。\n")
            if (select == "y") :
                tweet_content_with_image=input("ツイートする内容を入力してください。\ncancelコマンドで終了ができます。")
                if (tweet_content_with_image == "cancel") :
                    print("キャンセルしました。")
                else:
                    try:
                        file_names='./images/tweet.png'
                        api.update_with_media(filename=file_names,status=tweet_content_with_image) 
                        print("imagesフォルダ内にあるtweet.pngを添付してツイートを送信しました。")
                    except:    
                        print("tweet.pngが見つかりませんでした。")
                        api.update_status(status=tweet_content_with_image)
                        print("画像無しでツイートを送信しました。") 

            elif (select == "n") :
                tweet_content=input("ツイートする内容を入力してください。")
                api.update_status(tweet_content)
                print("ツイートを送信しました。")
            elif (select == "cancel" ) :
                print("キャンセルしました。")
            else :
                print("キャンセルしました。")
        elif (twitter_cui_command == "timeline") :
            public_tweets = api.home_timeline()
            for tweet in public_tweets:
                print('-------------------------')
                print(tweet.text)
        elif (twitter_cui_command == "search") :
            api = tweepy.API(auth)
            search_word = input()
            for tweet in tweepy.Cursor(api.search, q=search_word).items(5):
                print("\n{}\n".format(tweet.user.name))
                print(tweet.text,"\n")
        elif (twitter_cui_command == "login as"):
            me = api.me()
            print("\nログイン中のアカウント:{}\n".format(me.name,me.screen_name))
        elif (twitter_cui_command == "about me"):
            me = api.me()
            print("\nアカウント名:{}\n".format(me.name))
            print("ユーザーID:{}\n".format(me.screen_name))
            print("概要:{}\n".format(me.description))
            print("アイコンのURL:{}\n".format(me.profile_image_url_https))
        
        elif (twitter_cui_command == "release note"):
            print("\nTwitter for CUI v1.2.0\n")
            print("変更点その１:ライブラリまたはモジュールをインポートするとき、対象がインストールされていない場合、インストールできるようにしました。\nちなみにインストールをしたとき再起動する必要があります。")
            print("変更点その２:画像付きでツイートをする時、フォルダが存在しない、または対象の画像が存在しない場合は画像なしでツイートできるようにしました。")
            print("変更点その３:APIキーなどが入力されていない場合、正常に終了するようにしました。")
            print("変更点その４:about meコマンドを追加しました。ログイン中のアカウントの詳細を表示できます。")
            print("変更点その５:release noteコマンドを追加しました。現在のバージョンと変更点を表示できます。")
            print("変更点その６:今更ですがPINログイン機能を廃止し、アクセストークンとアクセストークンシークレットを入力して認証するようにしました。\nいちいちログイン認証するの面倒くさいし（）")
        elif (twitter_cui_command == "help") :
            print("")
            print("*"*50)
            print("\nTwitter for CUI Help\n")
            print("Tweet:ツイートを送信するコマンド。\n")
            print("login as:ログイン中のアカウントを表示するコマンド。\n")
            print("about me:ログイン中のアカウントの詳細を表示するコマンド。\n")
            print("release note:リリースノートを表示するコマンド")
            print("logout:Twitter for CUIを終了するコマンド。\n")
            print("*"*50)
            print("")
        elif (twitter_cui_command == "logout") :
            print('Twitter for Pythonを終了します。')
            break
        else :
            print("コマンドを入力してください。入力したコマンド:{} は存在しません。".format(twitter_cui_command))
