import requests

from pprint import pprint

access_token = '1f537a7712ebb37dec7e05b35cd46de6203b36a44e658da7e0f5d4a7c946b65531da896b6b8cc9df1ec4d' # scope_friends


def friends_get(user_id: int) -> list:
	request_url = 'https://api.vk.com/method/friends.get'
	params = {
		'access_token': access_token,
		'v': 5.107,
		'user_id': user_id,
		# 'count': 10,
		# 'order': 'name'
	}

	response = requests.get(request_url, params=params)
	json_ = response.json()['response']['items']
	return json_


if __name__ == "__main__":

	pprint(friends_get(355070))