from tracemalloc import start
import instaloader
import pandas as pd
from flask import Flask, jsonify
import json
import time
usr = 'fdenemefatih'
pw = '12Fatih34.'


def followers_to_csv(profile, desired_username):
    followers_list = []
    
    for followee in profile.get_followers():

        followers_list.append(followee.username)
    # df = pd.DataFrame(followers_list, columns=['Follower_list'])
    # df.to_csv(f'Instagram_Files/{desired_username}-followers.csv', index=False, encoding='utf-8')
    return followers_list

def following_list_csv(profile, desired_username):
    following_list = []
    
    for each in profile.get_followees():
        following_list.append(each.username)
    
    # df = pd.DataFrame(following_list, columns=['Followings_list'])
    
    # df.to_csv(f'Instagram_Files/{desired_username}-followings.csv', index=False, encoding='utf-8')
    return following_list


def get_nonfollowings(followers, followings):

    non_followers = {'non_followers':[]}
    for username in followings:
        if username not in followers:
            print(f'{username} is not following you back!')
            non_followers['non_followers'].append(username)
            
    return non_followers

def get_user_info(p):
    
    print(p.biography)
    print(p.full_name)
    print(p.followers)
    

bot = instaloader.Instaloader()
bot.login(user=usr, passwd=pw)
target_profile = 'fastwork.com.tr'

start_time = time.time()
profile = instaloader.Profile.from_username(bot.context, username=target_profile)
foll_list = profile.get_followers()
print(profile.full_name)
# print(len(foll_list))
print(profile.followers)

# for each in foll_list:
#     get_user_info(each)

print(time.time() - start_time)
    


# app = Flask(__name__)

# @app.route('/<string:target_profile>')
# def home(target_profile: str):
#     profile = instaloader.Profile.from_username(bot.context, username=target_profile)
    
#     profile.biography

#     print('Getting Followers')
#     followers_list = followers_to_csv(profile, target_profile)

#     print('Getting Followings')
#     following_list = following_list_csv(profile, target_profile)

#     results_dict = get_nonfollowings(followers_list, following_list)
    
#     # result = jsonify(data = results_dict)
#     return results_dict
    
    
# if __name__ =='__main__':
#     app.run(debug=True)