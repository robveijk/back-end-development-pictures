from pymongo import MongoClient

def get_connection():
    # TODO: Configure this
    connecturl = "mongodb://127.0.0.1:27017/"

    # connect to mongodb server
    # TODO: Log instead of print
    print("Connecting to mongodb server")
    return MongoClient(connecturl)
