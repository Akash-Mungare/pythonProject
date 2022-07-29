from unicodedata import decimal
from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime
import pandas
from Mongo_link import NPT_mongo
server_NPT = NPT_mongo

client = MongoClient(server_NPT.mongodb_NPT)
mydb=client[server_NPT.myDB_NPT]
groupdashboards=mydb[server_NPT.collection_NPT]

userId1 = '6254179f06c7ba354f495b3e'

# ==================== Shift A (IST: 7 AM To 3:30 PM) (UTC: 1:30 To 10:00) ====================
shift_A_start = datetime(2022, 7, 28, 1, 30, 0, 000)
shift_A_end = datetime(2022, 7, 28, 10, 0, 0, 000)


# ==================== Shift B (IST: 3:15 PM to 12:00 AM) (UTC: 9:45 To 18:30) ====================
shift_B_start = datetime(2022, 7, 28, 9, 45, 0, 000)
shift_B_end = datetime(2022, 7, 28, 18, 30, 0, 000)

# ==================== Shift G (IST: 9:30 AM To 6:00 PM) (UTC: 4:00 To 12:30) ====================
shift_G_start = datetime(2022, 7, 28, 4, 0, 0, 000)
shift_G_end = datetime(2022, 7, 28, 12, 30, 0, 000)

pipelineA = [
    {
        "$match":{
            "userId": ObjectId(userId1), "isDeleted": False,
            "deviceId":{"$in":[3,10,15,17,18,19,23]},
            "$or": [
                {
                    "$and": [{ "inTime": { "$gte": shift_A_start } }, { "outTime": { "$lte": shift_A_end } }]
                },
                {
                    "$and": [{ "inTime": { "$gte": shift_A_start } }, { "outTime": { "$gte": shift_A_end } }, { "inTime": { "$lte": shift_A_end } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_A_start } }, { "outTime": { "$lte": shift_A_end } }, { "outTime": { "$gte": shift_A_start } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_A_start } }, { "outTime": { "$gte": shift_A_end } }]
                }
            ]
        }
    },
    
    {
       "$group": {
            "_id": "$deviceName",
            "inTimeDate" : {"$min": "$inTime"},
            "outTimeDate" : {"$max" : "$outTime"},
            "prodTime" : {"$sum":"$totalTime"}
        }
    }
    
]

pipelineB = [
    {
        "$match":{
            "userId": ObjectId('6254179f06c7ba354f495b3e'), "isDeleted": False,
            "deviceId":{"$in":[2,6,11,12]},
            "$or": [
                {
                    "$and": [{ "inTime": { "$gte": shift_B_start } }, { "outTime": { "$lte": shift_B_end } }]
                },
                {
                    "$and": [{ "inTime": { "$gte": shift_B_start } }, { "outTime": { "$gte": shift_B_end } }, { "inTime": { "$lte": shift_B_end } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_B_start } }, { "outTime": { "$lte": shift_B_end } }, { "outTime": { "$gte": shift_B_start } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_B_start } }, { "outTime": { "$gte": shift_B_end } }]
                }
            ]
            }
    },
    {
        "$group": {
                "_id": "$deviceName",
                "inTimeDate" : {"$min": "$inTime"},
                "outTimeDate" : {"$max" : "$outTime"},
                "prodTime" : {"$sum":"$totalTime"}
        }
    }
]

pipelineG = [
    {
        "$match":{
            "userId": ObjectId(userId1), "isDeleted": False,
            "deviceId":{"$in":[1,4,5,8,9,13,20,22,28,29]},
            "$or": [
                {
                    "$and": [{ "inTime": { "$gte": shift_G_start } }, { "outTime": { "$lte": shift_G_end } }]
                },
                {
                    "$and": [{ "inTime": { "$gte": shift_G_start } }, { "outTime": { "$gte": shift_G_end } }, { "inTime": { "$lte": shift_G_end } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_G_start } }, { "outTime": { "$lte": shift_G_end } }, { "outTime": { "$gte": shift_G_start } }]
                },
                {
                    "$and": [{ "inTime": { "$lte": shift_G_start } }, { "outTime": { "$gte": shift_G_end } }]
                }
            ]
            }
    },
    {
        "$group": {
                "_id": "$deviceName",
                "inTimeDate" : {"$min": "$inTime"},
                "outTimeDate" : {"$max" : "$outTime"},
                "prodTime" : {"$sum":"$totalTime"}
        }
    }
]


# pipeline = [
#     {
#         "$match":{
#             "userId": ObjectId(userId1), "isDeleted": False,
#             "deviceId":{"$in":[3,10,15,17,18,19,23]},
#             "$or": [
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_A_start } }, { "outTime": { "$lte": shift_A_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_A_start } }, { "outTime": { "$gte": shift_A_end } }, { "inTime": { "$lte": shift_A_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_A_start } }, { "outTime": { "$lte": shift_A_end } }, { "outTime": { "$gte": shift_A_start } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_A_start } }, { "outTime": { "$gte": shift_A_end } }]
#                 }
#             ]
#         },
#     },
#     {
#         "$group": {
#                 "_id": "$deviceName",
#                 "inTimeDate" : {"$min": "$inTime"},
#                 "outTimeDate" : {"$max" : "$outTime"},
#                 "prodTime" : {"$sum":"$totalTime"}
#         }
#     },
#     # ==================== Shift B (IST: 3:15 PM to 12:00 AM) (UTC: 9:45 To 18:30) ====================
#     {
#         "$match":{
#             "userId": ObjectId(userId1), "isDeleted": False,
#             "deviceId":{"$in":[2,6,11,12]},
#             "$or": [
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_B_start } }, { "outTime": { "$lte": shift_B_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_B_start } }, { "outTime": { "$gte": shift_B_end } }, { "inTime": { "$lte": shift_B_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_B_start } }, { "outTime": { "$lte": shift_B_end } }, { "outTime": { "$gte": shift_B_start } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_B_start } }, { "outTime": { "$gte": shift_B_end } }]
#                 }
#             ]
#         },
#     },
#     {
#         "$group": {
#                 "_id": "$deviceName",
#                 "inTimeDate" : {"$min": "$inTime"},
#                 "outTimeDate" : {"$max" : "$outTime"},
#                 "prodTime" : {"$sum":"$totalTime"}
#         }
#     },
    
#     # ==================== Shift G (IST: 9:30 AM To 6:00 PM) (UTC: 4:00 To 12:30) ====================
#     {
#         "$match":{
#             "userId": ObjectId(userId1), "isDeleted": False,
#             "deviceId":{"$in":[1,4,5,8,9,13,20,22,28,29]},
#             "$or": [
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_G_start } }, { "outTime": { "$lte": shift_G_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$gte": shift_G_start } }, { "outTime": { "$gte": shift_G_end } }, { "inTime": { "$lte": shift_G_end } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_G_start } }, { "outTime": { "$lte": shift_G_end } }, { "outTime": { "$gte": shift_G_start } }]
#                 },
#                 {
#                     "$and": [{ "inTime": { "$lte": shift_G_start } }, { "outTime": { "$gte": shift_G_end } }]
#                 }
#             ]
#         }
    
#     },
#     {
#         "$group": {
#                 "_id": "$deviceName",
#                 "inTimeDate" : {"$min": "$inTime"},
#                 "outTimeDate" : {"$max" : "$outTime"},
#                 "prodTime" : {"$sum":"$totalTime"}
#         }
#     }
# ]

cursor = groupdashboards.aggregate(pipelineB)
# count = dataCollections.count_documents({"createdAt":{"$gte":start}})
list_cursor = list(cursor)
docs = pandas.DataFrame(columns=["_id","inTimeDate","outTimeDate","prodTime"])

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
docs.to_csv("Mahindra.csv",index=False)
print("------docs",docs)
