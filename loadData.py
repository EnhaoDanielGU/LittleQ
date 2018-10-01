# this script is to load and define the data
# it may take several seconds to run this script

## First, we import some useful packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py
import pandas as pd

# load the data in 201801-201808
data11 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201801.h5")
data12 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201802.h5")
data13 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201803.h5")
data14 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201804.h5")
data15 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201805.h5")
data16 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201806.h5")
data17 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201807.h5")
data18 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_201808.h5")
data191 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_20180901_20180909.h5")
data192 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_20180909_20180916.h5")
data193 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_20180916_20180923.h5")
data194 = pd.HDFStore("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format1_20180923_20180930.h5")

# to transfer the data to something we can use
btc11 = pd.DataFrame(data11['BTC-USD'])
bch11 = pd.DataFrame(data11['BCH-USD'])
ltc11 = pd.DataFrame(data11['LTC-USD'])
eth11 = pd.DataFrame(data11['ETH-USD'])

btc12 = pd.DataFrame(data12['BTC-USD'])
bch12 = pd.DataFrame(data12['BCH-USD'])
ltc12 = pd.DataFrame(data12['LTC-USD'])
eth12 = pd.DataFrame(data12['ETH-USD'])

btc13 = pd.DataFrame(data13['BTC-USD'])
bch13 = pd.DataFrame(data13['BCH-USD'])
ltc13 = pd.DataFrame(data13['LTC-USD'])
eth13 = pd.DataFrame(data13['ETH-USD'])

btc14 = pd.DataFrame(data14['BTC-USD'])
bch14 = pd.DataFrame(data14['BCH-USD'])
ltc14 = pd.DataFrame(data14['LTC-USD'])
eth14 = pd.DataFrame(data14['ETH-USD'])

btc15 = pd.DataFrame(data15['BTC-USD'])
bch15 = pd.DataFrame(data15['BCH-USD'])
ltc15 = pd.DataFrame(data15['LTC-USD'])
eth15 = pd.DataFrame(data15['ETH-USD'])

btc16 = pd.DataFrame(data16['BTC-USD'])
bch16 = pd.DataFrame(data16['BCH-USD'])
ltc16 = pd.DataFrame(data16['LTC-USD'])
eth16 = pd.DataFrame(data16['ETH-USD'])

btc17 = pd.DataFrame(data17['BTC-USD'])
bch17 = pd.DataFrame(data17['BCH-USD'])
ltc17 = pd.DataFrame(data17['LTC-USD'])
eth17 = pd.DataFrame(data17['ETH-USD'])

btc18 = pd.DataFrame(data18['BTC-USD'])
bch18 = pd.DataFrame(data18['BCH-USD'])
ltc18 = pd.DataFrame(data18['LTC-USD'])
eth18 = pd.DataFrame(data18['ETH-USD'])

btc191 = pd.DataFrame(data191['BTC-USD'])
bch191 = pd.DataFrame(data191['BCH-USD'])
ltc191 = pd.DataFrame(data191['LTC-USD'])
eth191 = pd.DataFrame(data191['ETH-USD'])

btc192 = pd.DataFrame(data192['BTC-USD'])
bch192 = pd.DataFrame(data192['BCH-USD'])
ltc192 = pd.DataFrame(data192['LTC-USD'])
eth192 = pd.DataFrame(data192['ETH-USD'])

btc193 = pd.DataFrame(data193['BTC-USD'])
bch193 = pd.DataFrame(data193['BCH-USD'])
ltc193 = pd.DataFrame(data193['LTC-USD'])
eth193 = pd.DataFrame(data193['ETH-USD'])

btc194 = pd.DataFrame(data194['BTC-USD'])
bch194 = pd.DataFrame(data194['BCH-USD'])
ltc194 = pd.DataFrame(data194['LTC-USD'])
eth194 = pd.DataFrame(data194['ETH-USD'])

# to calculate the trading price for all minutes
btc11["price"] = (btc11.close + btc11.high + btc11.low + btc11.open)*0.25
btc12["price"] = (btc12.close + btc12.high + btc12.low + btc12.open)*0.25
btc13["price"] = (btc13.close + btc13.high + btc13.low + btc13.open)*0.25
btc14["price"] = (btc14.close + btc14.high + btc14.low + btc14.open)*0.25
btc15["price"] = (btc15.close + btc15.high + btc15.low + btc15.open)*0.25
btc16["price"] = (btc16.close + btc16.high + btc16.low + btc16.open)*0.25
btc17["price"] = (btc17.close + btc17.high + btc17.low + btc17.open)*0.25
btc18["price"] = (btc18.close + btc18.high + btc18.low + btc18.open)*0.25
btc191["price"] = (btc191.close + btc191.high + btc191.low + btc191.open)*0.25
btc192["price"] = (btc192.close + btc192.high + btc192.low + btc192.open)*0.25
btc193["price"] = (btc193.close + btc193.high + btc193.low + btc193.open)*0.25
btc194["price"] = (btc194.close + btc194.high + btc194.low + btc194.open)*0.25

bch11["price"] = (bch11.close + bch11.high + bch11.low + bch11.open)*0.25
bch12["price"] = (bch12.close + bch12.high + bch12.low + bch12.open)*0.25
bch13["price"] = (bch13.close + bch13.high + bch13.low + bch13.open)*0.25
bch14["price"] = (bch14.close + bch14.high + bch14.low + bch14.open)*0.25
bch15["price"] = (bch15.close + bch15.high + bch15.low + bch15.open)*0.25
bch16["price"] = (bch16.close + bch16.high + bch16.low + bch16.open)*0.25
bch17["price"] = (bch17.close + bch17.high + bch17.low + bch17.open)*0.25
bch18["price"] = (bch18.close + bch18.high + bch18.low + bch18.open)*0.25
bch191["price"] = (bch191.close + bch191.high + bch191.low + bch191.open)*0.25
bch192["price"] = (bch192.close + bch192.high + bch192.low + bch192.open)*0.25
bch193["price"] = (bch193.close + bch193.high + bch193.low + bch193.open)*0.25
bch194["price"] = (bch194.close + bch194.high + bch194.low + bch194.open)*0.25

ltc11["price"] = (ltc11.close + ltc11.high + ltc11.low + ltc11.open)*0.25
ltc12["price"] = (ltc12.close + ltc12.high + ltc12.low + ltc12.open)*0.25
ltc13["price"] = (ltc13.close + ltc13.high + ltc13.low + ltc13.open)*0.25
ltc14["price"] = (ltc14.close + ltc14.high + ltc14.low + ltc14.open)*0.25
ltc15["price"] = (ltc15.close + ltc15.high + ltc15.low + ltc15.open)*0.25
ltc16["price"] = (ltc16.close + ltc16.high + ltc16.low + ltc16.open)*0.25
ltc17["price"] = (ltc17.close + ltc17.high + ltc17.low + ltc17.open)*0.25
ltc18["price"] = (ltc18.close + ltc18.high + ltc18.low + ltc18.open)*0.25
ltc191["price"] = (ltc191.close + ltc191.high + ltc191.low + ltc191.open)*0.25
ltc192["price"] = (ltc192.close + ltc192.high + ltc192.low + ltc192.open)*0.25
ltc193["price"] = (ltc193.close + ltc193.high + ltc193.low + ltc193.open)*0.25
ltc194["price"] = (ltc194.close + ltc194.high + ltc194.low + ltc194.open)*0.25

eth11["price"] = (eth11.close + eth11.high + eth11.low + eth11.open)*0.25
eth12["price"] = (eth12.close + eth12.high + eth12.low + eth12.open)*0.25
eth13["price"] = (eth13.close + eth13.high + eth13.low + eth13.open)*0.25
eth14["price"] = (eth14.close + eth14.high + eth14.low + eth14.open)*0.25
eth15["price"] = (eth15.close + eth15.high + eth15.low + eth15.open)*0.25
eth16["price"] = (eth16.close + eth16.high + eth16.low + eth16.open)*0.25
eth17["price"] = (eth17.close + eth17.high + eth17.low + eth17.open)*0.25
eth18["price"] = (eth18.close + eth18.high + eth18.low + eth18.open)*0.25
eth191["price"] = (eth191.close + eth191.high + eth191.low + eth191.open)*0.25
eth192["price"] = (eth192.close + eth192.high + eth192.low + eth192.open)*0.25
eth193["price"] = (eth193.close + eth193.high + eth193.low + eth193.open)*0.25
eth194["price"] = (eth194.close + eth194.high + eth194.low + eth194.open)*0.25

# to add the "time" column to the data. more convenient to draw graphs
# btc11["time"] = pd.DataFrame(btc11.index) # I commented this part temporarily because something went wrong

# to load the data for format2
data21 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201801.h5', mode = 'r') 
data22 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201802.h5', mode = 'r') 
data23 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201803.h5', mode = 'r') 
data24 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201804.h5', mode = 'r') 
data25 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201805.h5', mode = 'r') 
data26 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201806.h5', mode = 'r') 
data27 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201807.h5', mode = 'r') 
data28 = h5py.File('D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_201808.h5', mode = 'r') 
data291 = h5py.File("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_20180901_20180909.h5", mode = 'r')
data292 = h5py.File("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_20180909_20180916.h5", mode = 'r')
data293 = h5py.File("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_20180916_20180923.h5", mode = 'r')
data294 = h5py.File("D:/HKUSTyear1-1/MAFS5140/project/projectdata/data_format2_20180923_20180930.h5", mode = 'r')

#list(data21.keys())[:10] 
#data21["2018-01-01 00:00:00"]
#data21["2018-01-01 00:00:00"][:,:]
#data21.close()
