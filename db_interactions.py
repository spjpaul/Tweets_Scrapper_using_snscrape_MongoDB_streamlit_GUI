# db_interactions.py

import pymongo

def pushtodb(tweet_user, scrapd):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["scrap"]
    collection = db[tweet_user]
    collection.insert_many(scrapd)
