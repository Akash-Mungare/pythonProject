from pymongo import MongoClient

client = MongoClient("mongodb://rootReadUser:readAtpt1234@ct.sensegiz.com:27017/newsensegizCT?authSource=newsensegizCT")
mydb=client['newsensegizCT']
information=mydb.groupdashboards
print("connection sucessful")
client.close()