from class_User import User
from pprint import pprint
access_token = 'f10874588a9af88d782aeacdc3cca2fb85a3e72b23200f3bb07d5f0d3abdaf8d67a15a19ccbfbfb40ef64'

user1_id = 145656  # мой профиль

user2_id = 355070  # 20 общих друзей с моим профилем

user1 = User(user1_id, access_token)

user2 = User(user2_id, access_token)

print(user1)

print(user2)

pprint(user1 & user2)

