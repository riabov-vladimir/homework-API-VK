from friends_get import friends_get

access_token = 'f10874588a9af88d782aeacdc3cca2fb85a3e72b23200f3bb07d5f0d3abdaf8d67a15a19ccbfbfb40ef64'


class User:

	def __init__(self, user_id: int, access_token: str) -> None:
		self.token = access_token
		self.user_id = user_id

	def	get_params(self):
		return {
			'access_token': self.token,
			'v': 5.107,
			'user_id': self.user_id
		}

	def friends_list(self) -> list:
		result = friends_get(self.user_id)
		return result

	def __and__(self, other_user):
		mutual_friends_ids = list(set(self.friends_list()).intersection(other_user.friends_list()))
		result = map(lambda x: User(x, access_token), mutual_friends_ids)
		return list(result)

	def __str__(self):
		return 'https://vk.com/id{}'.format(self.user_id)
