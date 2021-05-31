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


def favorite(api):
	
  id = input("tweet_id:")
  
  try:
    api.create_favorite(id)
    print("いいねしました。")
  except:
    api.destroy_favorite(id)
    print("いいねを解除しました。")

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


def timeline(api):
  for status in api.home_timeline():
	
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




def tweet(api):
	
  fav = False
  
  me = api.me()

  content = input("tweet_content:")
  
  if len(content) == 0:
    print("ツイートの内容は一文字以上にして下さい。")
    return
  
  id = input("tweet_id:")
  
  if len(id) != 0:
    confirm = input("いいねしますか？\nyes/no:")
    if confirm == "yes":
      fav = True
    else:
      fav = False
      
  if fav == True:
    try:
      api.create_favorite(id)
      print("いいねしました。")
    except:
      pass
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
      print("ツイートしました。")
    except:
      print("ツイートの送信に失敗しました。")
      return
  
  else:
    api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
    print("ツイートしました。") 
  for status in api.user_timeline(id=me.screen_name,count = 1):
    print("ツイートid:"+str(status.id))
    print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))


def tweetdestroy(api):
  id = input("tweet_id:")
  try:
    api.destroy_status(id)
    print("ツイ消ししました。")
  except:
    print("ツイ消しに失敗しました。")
    
def search(api):
  search_text=input("search:")

  word = [search_text]
  set_count = 10
  results = api.search(q=word, count=set_count)

  for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    print("ユーザーID："+str(user_id))
    user = result.user.name
    print("ユーザー名："+user)
    tweet = result.text
    print("ユーザーのコメント："+tweet)
