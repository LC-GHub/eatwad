import certifi
import pymongo 
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://lionel1712:keatkeat@cluster0.fafyz.mongodb.net/Eatwad?retryWrites=true&w=majority", tlsCAFile = certifi.where())

db = cluster.Eatwad
collection = db["Food"]

post = {"_id": 0, "name": "test", "address": "Some address"}
collection.insert_one(post)

