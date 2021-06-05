import json

def timeline(api):
  try:
    for status in api.home_timeline():
    
      if (("RT" in status.text) == False):

        print("-"*42)

        if status.user.verified == True:
          print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
        else:
        	print(status.user.name + " @" + status.user.screen_name)

        print(status.text.replace("https://t.co","\nhttps://t.co"))
        print(f"いいね:{status.favorite_count} リツイート:{status.retweet_count}")
        if status.favorited == True:
          print("いいね済み")
        elif status.favorited ==True and status.retweeted == True:
          print("いいね済み リツイート済み")
        elif status.favorited == False and status.retweeted == True:
          print("リツイート済み")
        else:
          pass

        print(str(status.created_at)+ " " +status.source)
        print()
        print(f"ツイートid:{status.id}")
        print(f"ユーザーid:{status.user.id}")
        print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")

    limit_data = api.rate_limit_status()
    print("\nタイムライン取得残り回数:"+str(limit_data['resources']['statuses']['/statuses/home_timeline']['remaining']))

    print("\nリセットまで:"+(str(limit_data['resources']['statuses']['/statuses/home_timeline']['reset'])))  
  
  except:
    limit_data = api.rate_limit_status()
    print("APIの呼び出し制限を超えました。\nしばらくしてからもう一度やり直してください。")
    print(limit_data['resources']['statuses']['/statuses/home_timeline']['remaining'])
      

def tweet(api):

  json_open = open('./twitterfunc/key_config.json', 'r')
  json_load = json.load(json_open)

  default_image_path = json_load['default_image_path']

  print(default_image_path)
	
  fav = False
  
  me = api.me()

  content = input("tweet_content:")
  
  if len(content) == 0:
    print("ツイートの内容は一文字以上にして下さい。")
    return
  
  image_path = input("image path:")

  if len(image_path) == 0:
    image_tweet = False #画像無しツイート
  else:
    image_tweet = True #画像ありツイート

  image_path = default_image_path + image_path #デフォルトのパスに画像を追加

  id = input("tweet_id:")
  
  if len(id) != 0:
    confirm = input("いいねしますか？\nyes/no:")
    if confirm == "yes":
      fav = True
    else:
      fav = False
      
  if fav == True and image_tweet == False: #いいねと画像無しツイート
    try:
      api.create_favorite(id)
      print("いいねしました。")
    except:
      pass
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像無し
      print("ツイートしました。")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("ツイートid:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("ツイートの送信に失敗しました。")
      return

  elif fav == True and image_tweet == True: #いいねと画像ありツイート
    try:
      api.create_favorite(id)
      print("いいねしました。")
    except:
      pass
    try:
      api.update_with_media(status = content,filename=image_path, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像あり
      print("ツイートしました。")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("ツイートid:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("ツイートの送信に失敗しました。")
      return

  elif fav == False and image_tweet == False: #いいねなしと画像無しツイート
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像無し
      print("ツイートしました。")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("ツイートid:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("ツイートの送信に失敗しました。")
      return

  elif fav == False and image_tweet == True: #いいねなしと画像ありツイート
    try:
      api.update_with_media(status = content,filename=image_path, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像あり
      print("ツイートしました。")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("ツイートid:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("ツイートの送信に失敗しました。")
      return
  
  else:
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像無し
      print("ツイートしました。")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("ツイートid:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("ツイートの送信に失敗しました。")
      return
      

def tweetdestroy(api):
  id = input("tweet_id:")
  try:
    api.destroy_status(id)
    print("ツイ消ししました。")
  except:
    print("ツイ消しに失敗しました。")

def favorite(api):
	
  id = input("tweet_id:")
  
  try:
    api.create_favorite(id)
    print("いいねしました。")
  except:
    api.destroy_favorite(id)
    print("いいねを解除しました。")

def retweet(api):

  id = input("tweet_id:")

  try:
    if not len(id) == 0:
      api.retweet(id)
      print("リツイートしました。")
    else:
      print("キャンセルしました。")
  except:
    confirm = input("リツイートを取り消しますか？")
    if confirm == "yes":
      
      
      status = api.get_status(id, include_my_retweet=1)

      if status.retweeted == True:
          api.destroy_status(status.current_user_retweet['id'])
          
      print("リツイートを取り消しました。")

    else:
      print("キャンセルしました。")

def follow(api):
	
  follow_id = input("screen_name:")
  
  try:
    api.create_friendship(screen_name=follow_id)
    print("フォローしました。")
  except:
  	print("フォロー出来ませんでした。")

def unfollow(api):
	
  follow_id = input("screen_name:")
  
  confirm = input("フォロー解除しますか？\nyes or no\n:")
  
  if confirm == "yes":
    try:
      api.destroy_friendship(follow_id)
      print("フォロー解除しました。")
    except:
  	  print("フォロー解除出来ませんでした。")
  else:
    print("キャンセルしました。")

def profile(api):
	
  user_id = input("user_id:")
  
  user = api.get_user(user_id)
  
  print(user.name + f"\n@{user.screen_name}")
  
  print(user.description)
  
  print("場所:" + user.location)
  
def user_timeline(api):
  user_id = input("user_id:")
	
  for status in api.user_timeline(user_id):
    if (("RT" in status.text) == False):

      print("\n")	
      print("-"*42)
      
      if status.user.verified == True:
        print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
      else:
      	print(status.user.name + " @" + status.user.screen_name)

      print(status.text.replace("https://t.co","\nhttps://t.co"))
      print(f"いいね:{status.favorite_count} リツイート:{status.retweet_count}")
      if status.favorited == True:
        print("いいね済み")
      elif status.favorited ==True and status.retweeted == True:
        print("いいね済み リツイート済み")
      elif status.favorited == False and status.retweeted == True:
        print("リツイート済み")
      else:
        pass

      print(str(status.created_at)+ " " +status.source)
      print()
      print(f"ツイートid:{status.id}")
      print(f"ユーザーid:{status.user.id}")
      print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")

def search(api):
  search_text=input("search:")

  word = [search_text]
  set_count = 10
  results = api.search(q=word, count=set_count)

  for status in results:
    if (("RT" in status.text) == False):

      print("\n")	
      print("-"*42)
      
      if status.user.verified == True:
        print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
      else:
      	print(status.user.name + " @" + status.user.screen_name)

      print(status.text.replace("https://t.co","\nhttps://t.co"))
      print(f"いいね:{status.favorite_count} リツイート:{status.retweet_count}")
      if status.favorited == True:
        print("いいね済み")
      elif status.favorited ==True and status.retweeted == True:
        print("いいね済み リツイート済み")
      elif status.favorited == False and status.retweeted == True:
        print("リツイート済み")
      else:
        pass

      print(str(status.created_at)+ " " +status.source)
      print()
      print(f"ツイートid:{status.id}")
      print(f"ユーザーid:{status.user.id}")
      print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")

def loginas(api):
  me = api.me()
  print(f"名前:{me.name}")
  print(f"スクリーンネーム:{me.screen_name}")
  print(f"ユーザーID:{me.id}")

def twchelp(api):
	content = ("twitter-for-CUI help\ntimeline:タイムラインを表示出来ます。\ntweet:ツイートが出来ます。\nretweet:リツイートが出来ます。\nfavorite:いいねが出来ます。\nfollow:フォローが出来ます。\nunfollow:フォロー解除が出来ます。\nuser_info:ユーザーの詳細を確認できます。\n更なる詳細は\nhttps://github.com/Hashibutogarasu/twitter-for-Console-UI\nで確認できます。")
	print(content)