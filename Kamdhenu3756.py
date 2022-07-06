from random import *
import datetime
from datetime import timedelta

f = open("SingleCoinData.txt", "w")
gateway = "607771C67400"
coin = (str(10)).zfill(4)
# coin1 = ('0003','0002')
# coin = coin1
# print("======================== coin ======================", coin)
find = (str(2)).zfill(4)
# find1 = ('0003','0002')
# print("======================== find ======================", find)
rssi1 = ('C8','C9','CA','CB','CC','CD','CE','CF','D0','D1','D2','D3','D4','D5','D9','DA','DB',)
# rssi = choice(rssi1)
# print("======================== rssi ======================", rssi)
# UTCTime = datetime.datetime.now() - 19800000
utcTime = datetime.datetime.now(datetime.timezone.utc)
utc = utcTime.strftime("%Y-%m-%d %H:%M:%S")
x=26
j=4
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=0, minutes=10, seconds=-j)
    dd = ((hex(utcTime.day).upper()).removeprefix('0X')).zfill(2)
    hh = ((hex(diffTime.hour).upper()).removeprefix('0X')).zfill(2)
    mm = ((hex(diffTime.minute).upper()).removeprefix('0X')).zfill(2)
    ss = ((hex(diffTime.second).upper()).removeprefix('0X')).zfill(2)
    dataType = "AF"
    btr = str(59)
    data = gateway+coin+find+rssi+dd+hh+mm+ss+dataType+btr
    print(data,"\n")
    print("============================length of data===================",len(data))
    f.write(data + "\n")
    j+=21
    continue
offline = str("03")
# data = gateway+coin+find+offline+dd+hh+mm+ss+dataType+btr
f.write(data)

f.close()