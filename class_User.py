from pprint import pprint
from urllib.parse import urlencode
import requests
# print('?'.join(
# 	(oauth_url, urlencode(oauth_parms))
# ))
# set_params = params.copy()
# set_params['text'] = 'текст переданный интерпритатором'
#

access_token = 'f10874588a9af88d782aeacdc3cca2fb85a3e72b23200f3bb07d5f0d3abdaf8d67a15a19ccbfbfb40ef64'

oauth_url = 'https://oauth.vk.com/authorize'

oauth_parms = {
	'client_id': 7500138,
	'display': 'page',
	'scope': 'video,status',
	'response_type': 'token',
	'v': 5.107
}


class User:
	def __init__(self, token: str) -> None:
		self.token = token

	def	get_params(self):
		return {
			'access_token': access_token,
			'v': 5.107
		}

	def set_status(self, text: str) -> str:
		params = self.get_params()
		params['text'] = text
		response = requests.get(
			'https://api.vk.com/method/status.set',
			params
		)
		return response.json()['response']

	def get_status(self) -> str:
		params = self.get_params()
		response = requests.get(
			'https://api.vk.com/method/status.get',
			params
		)
		return response.json()['response']['text']


user1 = User(access_token)
print(user1.set_status('PyCharm classes'))

