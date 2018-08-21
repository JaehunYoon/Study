# coding: utf-8
 
import facebook
 
graph = facebook.GraphAPI(access_token='users-token', version="2.8")
site_info = graph.get_object(id="user-id", fields=["id","name"])
 
print(site_info)