import facebook

graph = facebook.GraphAPI(access_token='users-token', version="2.8")

permissions = graph.get_permissions(user_id=12345)
print('public_profile' in permissions)