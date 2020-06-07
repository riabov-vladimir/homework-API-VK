from pprint import pprint
from urllib.parse import urlencode
import requests
from friends_get import friends_get

access_token = 'f10874588a9af88d782aeacdc3cca2fb85a3e72b23200f3bb07d5f0d3abdaf8d67a15a19ccbfbfb40ef64'


class User:
	def __init__(self, user_id: int, access_token: str) -> None:
		self.token = access_token
		self.user_id = user_id
		self.friends = friends_get(user_id)

	def	get_params(self):
		return {
			'access_token': self.token,
			'v': 5.107,
			'user_id': self.user_id
		}

	def friends_in_common(self, other) -> list:
		result = list(set(self.friends).intersection(other.friends))
		return result

