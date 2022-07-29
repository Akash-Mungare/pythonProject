from unicodedata import decimal
from pymongo import MongoClient
from datetime import datetime
import pandas
from Mongo_link import CT_mongo

server_CT = CT_mongo

client = MongoClient(server_CT.mongodb_CT)
mydb=client[server_CT.myDB_CT]
dataCollections=mydb[server_CT.collection_CT]

start = datetime(2022, 7, 25, 19, 00, 0, 000)
# end = datetime(2022, 7, 23, 23, 30, 3, 381)
cursor = dataCollections.find({"createdAt":{"$gte":start}})
# count = dataCollections.count_documents({"createdAt":{"$gte":start}})


# [
#     {
#         "createdAt":{"$gte":start},
#         "coins": { "$substr": [ "$data", 13, 16 ] }
#          # "quarterSubtring": { "$substr": [ "$quarter", 2, -1 ] }
#     }
# ])

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

pipeline = [

{
  "_id":0,
  "coins": { "$substr": [ "$data", 13, 4 ] },
}
]


split_data = dataCollections.aggregate(pipeline)
docs['gateway'] = split_data

print("------docs",split_data)