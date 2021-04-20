def main():

    def nowtime():
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second

        nowtime = f"{year}/{month}/{day}/{hour}:{minute}"

        return  nowtime

    try:
        ak = '' #api key
        aks = '' #api key secret
        at = '' #access token
        ats = '' #access token secret
        auth = tweepy.OAuthHandler(ak,aks)
        auth.set_access_token(at,ats)
        api = tweepy.API(auth)
        me = api.me()
        print(nowtime())
        print("Logged on")
        print(f"name:{me.name}\ndescription:{me.description}\nurl:{me.url}\nlocation:{me.location}")
    except:
        print("404 Not found")
        sys.exit()
    while True:
        cmd = input("Enter command:")
        if cmd == "update profile": #change user name
            yn = input("Are you sure to change account name?")
            if yn == "y":
                accountname = input("Enter your new account name:")
                print(f"before:\n{me.name}")
                print(f"after:\n{accountname}")
                ynsure = input(f"Are you sure?\ny/n:")
                if ynsure == "y":
                    api.update_profile(accountname)
                    print("Changed your profile")
                    api.update_status(f"Twitter for Console UI info\nChanged account name:\n{accountname}")
                elif ynsure == "n":
                    print("Canceled")
                else:
                    print("Canceled")
            elif yn == "n":
                print("Canceled")
            else:
                print("Canceled")
        elif cmd == "tweet": #tweet
            tweettext = input("Enter your tweet content:").split('//newline//')
            imagepath = input("Enter image path:")
            if(os.path.exists(imagepath)):
                try:
                    api.update_with_media(status = '\n'.join(tweettext), filename = imagepath)
                    print("Tweet sended")
                except tweepy.TweepError as e:
                    print(f"Coundn't send Tweet\nReason:{e}")
            else:
                try:
                    api.update_status('\n'.join(tweettext))
                    print("Tweet sended")
                except tweepy.TweepError as e:
                    print(f"Coundn't send Tweet\nReason:{e}")
        elif cmd == "notice": #notice
            timeline=api.mentions_timeline(count=38)
            for status in timeline:
                status_id=status.id
                status_text = status.text
                print(status.author.name + " @" + status.author.screen_name + "\n" + "返信先:" + status_text + "\n")
        elif cmd == "close":
            break
            sys.exit()
        elif cmd == "os version":
            print(platform.platform())
        elif cmd == "version":
            print("twitter for Console UI\nversion:2.0.0")
        elif cmd == "help":
            print("twitter for Console UI help")
            print("tweet:send tweet")
            print("update profile:change account name")
            print("notice:show mentions")
            print("close:close twitter for Console UI")
            print("os version:show your OS version")
            print("help:show commands")
        else:
            print("That command does not exists")

if __name__ == '__main__':
    try:
        import sys
        import os
        import platform
        import pathlib
        import traceback
        import datetime
        import calendar
        import tweepy
        main()
    except:
        traceback.print_exc()
        while True:
            print("Failed to run this application")
            kakuninn = input("Push Enter key to close...")
            sys.exit()
