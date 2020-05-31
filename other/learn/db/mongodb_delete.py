from pymongo import MongoClient
client = MongoClient()
client = MongoClient('192.168.15.63', 27017)
mydatabase = client['test_db']
mycollection = mydatabase['test_table']

record={
'title': 'MongoDB and Python',
'description': 'MongoDB is no SQL database',
'tags': ['mongodb', 'database', 'NoSQL'],
'viewers': 104
}

# rec = mydatabase.myTable.insert_one(record)

mycollection.delete_many({'title': 'MongoDB and Python'})
mycollection.insert_one(record)


count = 0
for i in mycollection.find({'title': 'MongoDB and Python'}):
    # print(i)
    count+=1

# for i in mydatabase.myTable.find({'title': 'MongoDB and Python'}):
#     # print(i)
#     count+=1

print("count", count)