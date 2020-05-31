from pymongo import MongoClient
client = MongoClient()
client = MongoClient('192.168.15.63', 27017)
mydatabase = client['test_nosql_db']
# mydatabase = client.name_of_the_database
print(mydatabase)

mycollection = mydatabase['test_table']

record={
'title': 'MongoDB and Python',
'description': 'MongoDB is no SQL database',
'tags': ['mongodb', 'database', 'NoSQL'],
'viewers': 104
}
rec = mydatabase.myTable.insert_one(record)

print(rec)

for i in mydatabase.myTable.find({'title': 'MongoDB and Python'}):
    print(i)

print(i['tags'])