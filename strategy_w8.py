#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:14:31 2018

@author: jiayipan
"""

import pandas as pd
'''
Our strategy makes use of MACD to make decision
Whenever the short-window line cross the long-window line from below to above, we intepret it as a bullish signal and we long
Whenever the short line cross the long line from above to below, we short the coins
In this strategy, we trade all 4 types of crytocurrencies.
We incorporate a parameter called limit, which is the numbers of minutes we will trade after observing the signals
this 'limit' parameter is now set for 1, i.e. we trade only on the minute when the signal appear
actually, you can negelect this parameter for now, as we develop for later use in case we need it
'''

asset_index = [0,1,2,3] # we consider all 4 types of crytocurrency
mid_window = 26  # the long-window period, set to be 26 minutes
short_window = 9  # the short-window period, set to be 12 minute
extra_memry = 4  # the number of extra data we will record in memory, this is the span of exponential weighted moving average of the difference of short minus long
memry_length = mid_window + extra_memry
limit = 1



# Here is your main strategy function
# Note:
# 1. DO NOT modify the function parameters (time, data, etc.)
# 2. The strategy function AWAYS returns two things - position and memory:
# 2.1 position is a np.array (length 4) indicating your desired position of four crypto currencies next minute
# 2.2 memory is a class containing the information you want to save currently for future use


def handle_bar(counter,  # a counter for number of minute bars that have already been tested
               time,  # current time in string format such as "2018-07-30 00:30:00"
               data,  # data for current minute bar (in format 2)
               init_cash,  # your initial cash, a constant
               transaction,  # transaction ratio, a constant
               cash_balance,  # your cash balance at current minute
               crypto_balance,  # your crpyto currency balance at current minute
               total_balance,  # your total balance at current minute
               position_current,  # your position for 4 crypto currencies at this minute
               memory  # a class, containing the information you saved so far
               ):


    # Get position of last minute
    position_new = position_current  # to record the current position
    
    # Since we do not want a large memory to crash the program, we need to set up an index 'r' first
    if (counter == 0):
        memory.timer=[0,0,0,0]#this is a list of timer to count the number of minutes we trade after observing the signals, when this number reaches limit, we stop
        memory.increment=[0,0,0,0]#the increment for counting use, when sginals appear, we make it to 1, so that the timer can start to count
        memory.buy_sell=[None, None, None, None]
        memory.dataframe_collection = {} #creat a dataframe library to store totally 8 dataframes for calculating MACD, the 2k and 2k+1 dataframes are for one type of coins, where k =0,1,2,3
        for i in [0,2,4,6]:#initalizing dataframes
            memory.dataframe_collection[i]=pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume'])
            memory.dataframe_collection[i+1]=pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume'])

    for i in [0,2,4,6]:
        memory.dataframe_collection[i].loc[counter]=data[asset_index[int(i/2)],]#read and store data to the 2k dataframe
        memory.dataframe_collection[i+1].loc[counter]=memory.dataframe_collection[i].loc[counter]#read the date to the 2k+1 dataframe for manipulating
    
    if (counter >= 100):
        #the below lines calculate the MACD for each crytocurrencies, so we need a loop
        for i in [0,2,4,6]:
            memory.dataframe_collection[i+1]['average'] = (memory.dataframe_collection[i+1]['close'] + memory.dataframe_collection[i+1]['high']\
                                       + memory.dataframe_collection[i+1]['low'] + memory.dataframe_collection[i+1]['open']) / 4
            memory.dataframe_collection[i+1]['short_ema'] = memory.dataframe_collection[i+1].average.ewm(span=short_window).mean()
            memory.dataframe_collection[i+1]['mid_ema'] = memory.dataframe_collection[i+1].average.ewm(span=mid_window).mean()
            memory.dataframe_collection[i+1]['MACD'] = memory.dataframe_collection[i+1]['short_ema'] - memory.dataframe_collection[i+1]['mid_ema']
            memory.dataframe_collection[i+1]['Nine']=memory.dataframe_collection[i+1].MACD.ewm(span=4).mean()
            memory.dataframe_collection[i+1]['diff']=memory.dataframe_collection[i+1]['MACD']-memory.dataframe_collection[i+1]['Nine']
            #This is when we observe bullish signal
            if (memory.dataframe_collection[i+1].iloc[len(memory.dataframe_collection[i+1]) - 2]['diff'] < 0 and\
                memory.dataframe_collection[i+1].iloc[len(memory.dataframe_collection[i+1]) - 1]['diff'] > 0):
                memory.increment[int(i/2)]=1
                memory.buy_sell[int(i/2)]=True#True represents buying action should be taken
            #this is when we observe bearish signal
            elif (memory.dataframe_collection[i+1].iloc[len(memory.dataframe_collection[i+1]) - 2]['diff'] > 0 and\
                  memory.dataframe_collection[i+1].iloc[len(memory.dataframe_collection[i+1]) - 1]['diff'] < 0):
                memory.increment[int(i/2)]=1
                memory.buy_sell[int(i/2)]=False#False represents selling
            memory.timer[int(i/2)]+=memory.increment[int(i/2)]
            if(memory.buy_sell[int(i/2)]and memory.timer[int(i/2)]>0 and memory.timer[int(i/2)]<=limit):
                #we set our cash buffer to be 20000, whenever our cash is lower than 20000, we only do position clearing
                if(cash_balance>20000):
                    if(position_new[asset_index[int(i/2)]]>=0):
                        position_new[asset_index[int(i/2)]]+=(cash_balance-20000)/4/memory.dataframe_collection[i+1].iloc[counter]['average']
                    else:
                        position_new[asset_index[int(i/2)]]=-position_new[asset_index[int(i/2)]]+(cash_balance-20000)/4/memory.dataframe_collection[i+1].iloc[counter]['average']
                else:
                    if(position_new[asset_index[int(i/2)]]< 0):
                        position_new[asset_index[int(i/2)]] =0
            if(not memory.buy_sell[int(i/2)]and memory.timer[int(i/2)]>0 and memory.timer[int(i/2)]<=limit):
                if(cash_balance>20000):
                    if(position_new[asset_index[int(i/2)]]<=0):
                        position_new[asset_index[int(i/2)]]-=(cash_balance-20000)/4/memory.dataframe_collection[i+1].iloc[counter]['average']
                    else:
                        position_new[asset_index[int(i/2)]]=-position_new[asset_index[int(i/2)]]-(cash_balance-20000)/4/memory.dataframe_collection[i+1].iloc[counter]['average']
                else:
                    if(position_new[asset_index[int(i/2)]]>0):
                        position_new[asset_index[int(i/2)]]=0
            if(memory.timer[int(i/2)]==limit):
                memory.increment[int(i/2)]=0
                memory.timer[int(i/2)]=0
    # End of strategy
    return position_new, memory
