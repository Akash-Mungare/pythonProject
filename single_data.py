from random import *
import datetime
from datetime import timedelta

f = open("SingleCoinData.txt", "w")
gateway = "60777138D45E"
coin = (str(10)).zfill(4)
# coin1 = ('0003','0002')
# coin = coin1
# print("======================== coin ======================", coin)
find = (str(8)).zfill(4)
# find1 = ('0003','0002')
# print("======================== find ======================", find)
rssi1 = ('C1','C2','C8','C9','CA','CB','CC','CD','CE','CF','D0','D1','D2','D3','D4','D5','D6','D7','D8','D9','DA','DB','DC','DD','DE','DF','E0','E1')
# rssi = choice(rssi1)
# print("======================== rssi ======================", rssi)
# UTCTime = datetime.datetime.now() - 19800000
utcTime = datetime.datetime.now(datetime.timezone.utc)
utc = utcTime.strftime("%Y-%m-%d %H:%M:%S")
x=60
j=4
for i in range(x):
    # coin = choice(coin1)
    # find = choice(find1)
    rssi = choice(rssi1)
    # if find == '0002':
    #     rssi1 = ('A6','A7','A8','A9','AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3', 'B4')
    #     rssi = choice(rssi1)
    # else:
    #     rssi2 = ('B3','B4','B5','B6','B7','B8','B9','BA','BB','BC','BD','BE','BF','C0','C1','C2')
    #     rssi = choice(rssi2)
    diffTime = utcTime - timedelta(hours=2, minutes=10, seconds=-j)
    # print("======================== now()======================", diffTime)
    dd = ((hex(utcTime.day).upper()).removeprefix('0X')).zfill(2)
    # dd = utcdd.zfill(2)
    # print("======================== DD ======================", dd)
    hh = ((hex(diffTime.hour).upper()).removeprefix('0X')).zfill(2)
    mm = ((hex(diffTime.minute).upper()).removeprefix('0X')).zfill(2)
    ss = ((hex(diffTime.second).upper()).removeprefix('0X')).zfill(2)
    # print("dd : ", dd, " hh: ",hh," mm: ",mm," ss: ",ss)
    dataType = "AF"
    btr = str(59)
    data = gateway+coin+find+rssi+dd+hh+mm+ss+dataType+btr
    print(data,"\n")
    print("============================length of data===================",len(data))
    f.write(data + "\n")
    j+=17
    continue
offline = str("03")
data = gateway+coin+find+offline+dd+hh+mm+ss+dataType+btr
f.write(data)

f.close()
