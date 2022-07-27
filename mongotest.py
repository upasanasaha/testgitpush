#pip install pymongo
#pip install "pymongo[srv]"
import pymongo
client = pymongo.MongoClient("mongodb+srv://UpasanaSaha:11$Upcellent@cluster0.svnl1cl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={'name':"upasana",
   'email':'upasanasaha40@gmail.com',
   'surname':'Saha'}
d={'name':"upasana",
   'email':'upasanasaha40@gmail.com',
   'surname':'Saha'}
db1= client['mongotest']
coll=db1['test']
coll.insert_one(d)
