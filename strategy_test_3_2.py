""""This is the 3-2 strategy (week 3, second improvement). when signals of buying or selling appear, 
we buy for several minute for as much as possible. Thie length of time is denoted by t
Remark: This strategy trades too frequent, the transition cost (4100+) is almost equal to the loss of balance(test sample : 2018-9-23:29
"""

import pandas as pd
import numpy as np

asset_index = 1  # only consider BTC (the **second** crypto currency in dataset)
mid_window = 26  # the middle-length average period
short_window = 12  # the short-length average period
extra_memry = 9  # the number of extra data we will record in memory
memry_length = mid_window + extra_memry  # we add one to check the change of Moving Averages, more details below
t = 3

# enlarge_para = 1.05
# shrinken_para = 0.95


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
    # We use Moving Average Convergence Divergence to indicate when to long and when to short.
    # Every time we decide what to do, we calculate the mean of the past few minutes.
    # Let's call the 26-minute average as "mid", and the 13-minute average as "short"
    # once "short" surpasses "mid", it is a to-long signal
    # once "mid" surpasses "short", it is a to-short signal
    # otherwise we do nothing
    # in order to lower the transition cost, we receive the signal every 13 minutes
    # (in the beginning, we receive the signal every minute, but the transition cost is high, so we kept losing money)
    # once we receive the signal, we long/short everything we have, in order to amplify the effect

    # Get position of last minute
    position_new = position_current  # to record the current position

    # Since we do not want a large memory to crash the program, we need to set up an index 'r' first
    if (counter == 0):
        memory.data_save = pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume']) # to create an empty DataFrame with column names
        memory.data_save2 = pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume']) # to create an empty DataFrame with column names
        memory.signal_buy=None
        memory.signal_sell=None
        memory.t_increment=0
        memory.t=0
    #r = counter % memry_length # This is to record the order of this data recorded in our memory        
    memory.data_save.loc[counter] = data[asset_index,] # record the first data we met in the memory

# When the number of data recorded exceed the length of the memory we desire, we can start to make decisions about buying and selling.

    if (counter >= memry_length): 
        for i in range(0, memry_length):
            # we set up a new memory recording the past few data in the order of time
            memory.data_save2.loc[i] = memory.data_save.loc[len(memory.data_save)-memry_length+i] 

        memory.data_save2['average'] = (memory.data_save2['close'] + memory.data_save2['high'] + memory.data_save2['low'] + memory.data_save2['open']) / 4
        memory.data_save2['short_ema'] = memory.data_save2.average.ewm(span=short_window).mean()
        memory.data_save2['mid_ema'] = memory.data_save2.average.ewm(span=mid_window).mean()
        memory.data_save2['MACD'] = memory.data_save2['short_ema'] - memory.data_save2['mid_ema']
        memory.data_save2['Nine']=memory.data_save2.MACD.ewm(span=9).mean()
        memory.data_save2['diff']=memory.data_save2['MACD']-memory.data_save2['Nine']
        if (memory.data_save2.iloc[len(memory.data_save2) - 2]['diff'] < 0 and memory.data_save2.iloc[len(memory.data_save2) - 1]['diff'] > 0):
            memory.t_increment=1
            memory.signal_buy=True
            memory.signal_sell=False
        elif (memory.data_save2.iloc[len(memory.data_save2) - 2]['diff'] > 0 and memory.data_save2.iloc[len(memory.data_save2) - 1]['diff'] < 0):
            memory.t_increment=1
            memory.signal_buy=False
            memory.signal_sell=True
#        if (aa):
#            memory.t_increment = 1
#            memory.signal_buy = False
#            memory.signal_sell = False
        memory.t += memory.t_increment
        if(memory.t>0 and memory.t<=t and memory.signal_buy == True and memory.signal_sell == False):
            position_new[asset_index] = 8
        if(memory.t>0 and memory.t<=t and memory.signal_sell == False and memory.signal_buy == True):
            position_new[asset_index] = -3
#        if(memory.signal_sell == False and memory.signal_buy == False):
#            position_new[asset_index] = 0
        if(memory.t==t):
            memory.t_increment=0
            memory.t=0
            
    #        roll_short_old = roll_short
    #        roll_mid_old = roll_mid

    # End of strategy
    return position_new, memory



