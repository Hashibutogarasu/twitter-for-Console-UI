print('Twitter for CUIを起動しています...')
import sys
import tweepy
import webbrowser
import urllib
from selenium import webdriver
import time
print('インポートが完了しました。')

API_KEY = '**********'  
API_KEY_SECRET = '*********'

def get_oauth_token(url:str)->str:
    querys = urllib.parse.urlparse(url).query
    querys_dict = urllib.parse.parse_qs(querys)
    return querys_dict["oauth_token"][0]

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print( "リクエストトークンの取得に失敗しました。")


    oauth_token = get_oauth_token(redirect_url)
    auth.request_token['oauth_token'] = oauth_token

    webbrowser.open(redirect_url)

    verifier = input("ブラウザに表示されているPINコードを入力してください。:")
    verifier_none = verifier.strip()
    #PINコードに含まれている空白を削除

    auth.request_token['oauth_token_secret'] = verifier_none

    if len(verifier_none) == 0:
        print('PINコードが未入力です。')
        sys.exit()
        #未入力の場合強制終了する

    try:
        auth.get_access_token(verifier_none)
    except tweepy.TweepError:
        print("アクセストークンの入手に失敗しました。")
        sys.exit()

    with open("auth_info.txt",mode="w") as file:
        text = "key:{}\nsecret:{}".format(auth.access_token,auth.access_token_secret)
        file.write(text)
    

    if auth.access_token is None :
        if auth.access_token_secret is None :
            print('PINコードが間違っています。')
            print('Twitter python for crowを終了します。')
            time.sleep(2)
            sys.exit()

    print("認証が完了しました。")

auth.set_access_token(auth.access_token, auth.access_token_secret)

api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True
)

me = api.me()
print('ようこそ',me.name,me.screen_name)

while True:
    twitter_cui_command=input("コマンドを入力...\nhelpコマンドでコマンドの一覧を表示できます。\n")
    if (twitter_cui_command == "Tweet") :
        select=input("画像を添付しますか？y/n\nDefault→n\nlogoutコマンドで終了できます。\n")
        if (select == "y") :
            tweet_content_with_image=input("ツイートする内容を入力してください。\n何も入力しないでエンターキーを押すと画像のみを送信できます。\nまた、logoutコマンドで終了もできます。")
            if (tweet_content_with_image == "logout") :
                break
            file_names='./images/tweet.png'
            api.update_with_media(filename=file_names,status=tweet_content_with_image) 
            print("imagesフォルダ内にあるtweet.pngを添付してツイートを送信しました。")
        elif (select == "n") :
            tweet_content=input("ツイートする内容を入力してください。")
            api.update_status(tweet_content)
            print("ツイートを送信しました。")
        elif (select == "logout" ) :
            break
        else :
            tweet_content_with_image=input("ツイートする内容を入力してください。")
            file_names='./images/tweet.png'
            api.update_with_media(filename=file_names,status=tweet_content_with_image) 
            print("imagesフォルダ内にあるtweet.pngを添付してツイートを送信しました。")
    elif (twitter_cui_command == "login as"):
        me = api.me()
        print("ログイン中のアカウント=>",me.name,me.screen_name)
    elif (twitter_cui_command == "help") :
        print("\nTwitter Python Help\n")
        print("Tweet=>ツイートを送信するコマンド。\n")
        print("login as=>ログイン中のアカウントを表示するコマンド。\n")
        print("logout=>Twitter for CUIを終了するコマンド。\n")
    elif (twitter_cui_command == "logout") :
        print('Twitter for Pythonを終了します。')
        break
    else :
        print("コマンドを入力してください。\n入力したコマンド","「",twitter_cui_command,"」は存在しません。")
