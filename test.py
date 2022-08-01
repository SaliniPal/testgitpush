import pymongo
client = pymongo.MongoClient("mongodb+srv://salininilas:salininilas22@cluster0.njaikcv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "salini",
    "email": "salini@gmail.com",
    "surname": "palani"
}

db1 = client['mongodb']
coll  = db1['test']
coll.insert_one(d)