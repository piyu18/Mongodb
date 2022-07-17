# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymongo as pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:Priya1803@cluster0.rxtbh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

dict1 = {
    'name' : 'Priya',
    'email' : 'priya@gmail.com',
    'last_name' : 'Priya'

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(dict1)
