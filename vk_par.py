import vk_api
import re
import pandas as pd
import os
import threading
from time import process_time
from time import time


###################################################
# функция открытия словаря из csv
###################################################


def login_in():
    vk_session = vk_api.VkApi('', '', auth_handler=auth_handler)  # ввод токена группы
    vk_session.auth()
    return vk_session.get_api()


###################################################
# функция открытия словаря из csv
###################################################


def auth_handler():
    return input("Enter authentication code: "), True


if __name__ == '__main__':

    vk = login_in()
    print("PLEASE, WAIT...")
    list_friends = vk.friends.get()['items']
    print(vk.friends.get()['items'])
    list_for_csv = []

    for friend in list_friends:
        print(f"vk_id posts owner: {friend}")

        try:
            vk.wall.get(owner_id=friend, filter='owner')
        except:
            print('dude is closed, go ahead!')  # дебаг функция, показывает закрыт ли паблик
            continue

        for post_id in vk.wall.get(owner_id=friend, filter='owner')['items']:
            if vk.likes.isLiked(user_id=549396642, type='post', owner_id=friend, item_id=post_id['id'])['liked'] == 1:
                list_for_csv.append(f"user_id: {549396642} liked post: item_id={post_id['id']}!")

    pd.DataFrame.from_dict({'likes': list_for_csv}).to_csv(f"vk_likes_{549396642}.csv", index=False)