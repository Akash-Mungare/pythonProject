from random import *
import datetime
from datetime import timedelta

f = open("SingleCoinData.txt", "w")
gateway = "1234567890AC"
coin = (str("0A")).zfill(4)
# coin1 = ('0003','0002')
# coin = coin1
# print("======================== coin ======================", coin)
find = (str("02")).zfill(4)
# find1 = ('0003','0002')
# print("======================== find ======================", find)
rssi1 = ('C8','C9','CA','CB','CC','CD','CE','CF','D0','D1','D2','D3','D4','D5','D9','DA','DB',)
# rssi = choice(rssi1)
# print("======================== rssi ======================", rssi)
# UTCTime = datetime.datetime.now() - 19800000
utcTime = datetime.datetime.now(datetime.timezone.utc)
utc = utcTime.strftime("%Y-%m-%d %H:%M:%S")
x=20
j=4
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=0, minutes=2, seconds=-j)
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
    j+=14
    continue
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=2, minutes=22, seconds=-j)
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
    j+=15
    continue
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=1, minutes=12, seconds=-j)
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
    j+=15
    continue
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=4, minutes=42, seconds=-j)
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
    j+=15
    continue
for i in range(x):
    rssi = choice(rssi1)
    diffTime = utcTime - timedelta(hours=3, minutes=32, seconds=-j)
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
    j+=15
    continue
# offline = str("03")
# data = gateway+coin+find+offline+dd+hh+mm+ss+dataType+btr
f.write(data)

f.close()