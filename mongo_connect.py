from pymongo import MongoClient
# user = 'root'
# password = 'MjQwOTgtcnNhbm5h' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
# host='mongo'
#create the connection url
# connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)
# Note: authSource is the database with user credentials
#       https://www.mongodb.com/docs/manual/reference/connection-string-options/#mongodb-urioption-urioption.authSource
connecturl = "mongodb://127.0.0.1:27017/"

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# print the database names

for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")

# close the server connecton
connection.close()