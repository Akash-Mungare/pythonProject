from unicodedata import decimal
from pymongo import MongoClient
from datetime import datetime
import pandas
from Mongo_link import CT_mongo
server_CT = CT_mongo

client = MongoClient(server_CT.mongodb_CT)
mydb=client[server_CT.myDB_CT]
dataCollections=mydb[server_CT.collection_CT]

start = datetime(2022, 7, 26, 17, 40, 0, 000)
# end = datetime(2022, 7, 23, 23, 30, 3, 381)
pipeline = [
    {
        "$match":{
            "createdAt":{"$gte":start}
            }
    },
    {
        "$project": {
                "createdAt":1,
                "data":1,
                "status":1,
                "updatedAt":1,
                "coins": { "$substr": [ "$data", 12, 4 ] },
                "find": { "$substr": [ "$data", 16, 4 ] },
                "rssi": { "$substr": [ "$data", 20, 2 ] },
                "dd": { "$substr": [ "$data", 22, 2 ] },
                "hh": { "$substr": [ "$data", 24, 2 ] },
                "mm": { "$substr": [ "$data", 26, 2 ] },
                "ss": { "$substr": [ "$data", 28, 2 ] },
                "type": { "$substr": [ "$data", 30, 2 ] }
        }
    }]

cursor = dataCollections.aggregate(pipeline)
# count = dataCollections.count_documents({"createdAt":{"$gte":start}})
list_cursor = list(cursor)
docs = pandas.DataFrame(columns=["_id","createdAt","data","status","updatedAt"])

for num, doc in enumerate( list_cursor ):
    # convert ObjectId() to str
    doc["_id"] = str(doc["_id"])
    # get document _id from dict
    doc_id = doc["_id"]
    # create a Series obj from the MongoDB dict
    series_obj = pandas.Series(doc, name=doc_id)
    # append the MongoDB Series obj to the DataFrame obj
    docs = docs.append( series_obj )
csv_export = docs.to_csv(sep=",")
print("\nCSV Data:", csv_export)
docs.to_csv("dataCollectionK.csv",index=False)
print("------docs",docs)
# left1 = "=Left(c"
# leftend= ",12)"

# docs = pandas.SparseDtype
# for idx,x in enumerate(docs['gateway']):
#     print("------------>>>>>>>>",docs['gateway'][idx]);
# docs['gateway'] = 

# docs['gateway'] = docs['data'].str[:12]
# docs['coin'] = (docs['data'].str[13:16])
# coins = docs['coin'].str[:4]
# print("==========================================",coins)



# docs['coin'] = int(coins,16)
# docs['coin'] = docs['data'].str[13:16]
# docs['coin'] = int(str(docs['coin']),16)

# docs['find'] = docs['data'].str[17:20]
# docs['RSSI'] = docs['data'].str[21:22]
# docs['DD'] = docs['data'].str[23:24]
# docs['HH'] = docs['data'].str[25:26]
# docs['MM'] = docs['data'].str[27:28]
# docs['SS'] = docs['data'].str[29:30]
# docs['Type'] = docs['data'].str[31:32]
# docs[':'] = ":"

# docs.assign(gateway = lambda x: "=LEFT(x,12)")

# docs1 = pandas.read_csv("C:\Users\SenseGiz\PycharmProjects\pythonProject\All_Server\dataCollectionK.csv")

# docs1['gateway'] = docs1['data'].str[:12]
# docs1['coin'] = (docs1['data'].str[13:16])
# coins = docs['coin'].str[:4]
# print("==========================================",coins)

# docs.to_csv("dataCollectionK.csv",index=False)
# print("------docs",docs)