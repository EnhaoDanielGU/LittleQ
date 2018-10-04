# Here you can
# 1. import necessary python packages for your strategy
# 2. Load your own facility files containing functions, trained models, extra data, etc for later use
# 3. Set some global constants
# Note:
# 1. You should put your facility files in the same folder as this strategy.py file
# 2. When load files, ALWAYS use relative path such as "data/facility.pickle"
# DO NOT use absolute path such as "C:/Users/Peter/Documents/project/data/facility.pickle"

import pandas as pd
# from sklearn.externals import joblib

# model = joblib.load('model.pkl')#####

asset_index = 1  # only consider BTC (the **second** crypto currency in dataset)
mid_window = 26 # the middle-length average period
short_window = 13 # the short-length average period
extra_memry = 1 # the number of extra data we will record in memory
memry_length = mid_window + extra_memry # we add one to check the change of Moving Averages, more details below
#enlarge_para = 1.05
#shrinken_para = 0.95
switch_long=False
switch_short=False


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
    position_new = position_current # to record the current position
                                    # However, I don't know whether this sentence is really necessary

# Since we do not want a large memory to crash the program, we need to set up an index 'r' first    
    if (counter == 0):
        memory.data_save = pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume']) # to create an empty DataFrame with column names
        memory.data_save2 = pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume']) # to create an empty DataFrame with column names

    r = counter % memry_length # This is to record the order of this data recorded in our memory        
    memory.data_save.loc[r] = data[asset_index,] # record the first data we met in the memory

# When the number of data recorded exceed the length of the memory we desire, we can start to make decisions about buying and selling.
    if (counter >= memry_length - 1 and counter % 13 == 0): 
#    if (counter >= memry_length - 1): 
    
        for i in range(0, memry_length):
            # we set up a new memory recording the past few data in the order of time
            memory.data_save2.loc[i] = memory.data_save.loc[(i+r+1)%memry_length] #? not sure if it works yet
        
        bar = pd.DataFrame(memory.data_save2) #? not sure if it works yet
        bar['price']= (bar['close']+bar['high']+bar['low']+bar['open'])/4 # to add a new column vertically to the DataFrame 'bar'. This columns shows the trading price

# these 2 sentences calculate all the means for a whole column
#        roll_short = bar['price'].rolling(window=short_window).mean() # to apply 'rolling' to construct a fixed window to calculate the mean needed
#        roll_mid = bar['price'].rolling(window=mid_window).mean()
        
# we apply a simpler method to calculate the mean
        
        # we calculate the long and short mean at 'counter' (now)
#        if (counter == memry_length - 1):
#            roll_short_old = bar.price.iloc[memry_length - short_window  - extra_memry : memry_length - extra_memry - 1].mean()
#            roll_mid_old = bar.price.iloc[memry_length - mid_window - extra_memry : memry_length - extra_memry - 1].mean()
        roll_short_old = bar.price.iloc[memry_length - short_window  - extra_memry : memry_length - extra_memry - 1].mean()
        roll_mid_old = bar.price.iloc[memry_length - mid_window - extra_memry : memry_length - extra_memry - 1].mean()
        roll_short = bar.price.iloc[memry_length - short_window : memry_length - 1].mean()
        roll_mid = bar.price.iloc[memry_length - mid_window : memry_length - 1].mean()
        
        
# I temporarily deleted these 2 sentences        
#        bar['short_mavg'] = roll_short
#        bar['mid_mavg'] = roll_mid

#        if(bar[memry_length-2,'short_mavg']<bar[memry_length-2,'mid_mavg'] and bar[memry_length-1,'short_mavg']>bar[memry_length-1,'mid_mavg']):
        if(roll_short_old <= roll_mid_old and roll_short > roll_mid):
            switch_long=True
            switch_short=False
        if(position_new[asset_index]<10 and switch_long):
            position_new[asset_index] = 10
#        if(bar[memry_length-2,'short_mavg']>bar[memry_length-2,'mid_mavg'] and bar[memry_length-1,'short_mavg']<bar[memry_length-1'mid_mavg']):
        elif(roll_short_old >= roll_mid_old and roll_short < roll_mid):
            switch_short=True
            swtich_long=False
        if(position_new[asset_index]>-8 and switch_short):
            position_new[asset_index] = -8
        
#        roll_short_old = roll_short
#        roll_mid_old = roll_mid


    # End of strategy
    return position_new, memory

