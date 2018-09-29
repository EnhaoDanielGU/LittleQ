# Here you can
# 1. import necessary python packages for your strategy
# 2. Load your own facility files containing functions, trained models, extra data, etc for later use
# 3. Set some global constants
# Note:
# 1. You should put your facility files in the same folder as this strategy.py file
# 2. When load files, ALWAYS use relative path such as "data/facility.pickle"
# DO NOT use absolute path such as "C:/Users/Peter/Documents/project/data/facility.pickle"
from auxiliary import generate_bar
import pandas as pd
from sklearn.externals import joblib

    model = joblib.load('model.pkl')#####
    asset_index = 1  # only consider BTC (the **second** crypto currency in dataset)
    mid_window = 26
    short_window = 13
    bar_length = mid_window+3


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
    # 
    #
    
    # Get position of last minute
    position_new = position_current
    
    r = (counter + 1) % bar_length - 1
    # Generate OHLC data for every 30 minutes
    if (counter == 0):
    # memory.data_save = np.zeros((bar_length, 5))#, dtype=np.float64)
        memory.data_save = pd.DataFrame(columns = ['close', 'high', 'low', 'open', 'volume'])####edited
        memory.data_save.loc[0] = data[asset_index,]
    elif (counter >= bar_length):           
        memory.data_save.loc[r] = data[asset_index,]
    
       for i in range(0, bar_length):
           memory.data_save2.loc[i] = memory.data_save.loc[(i+r+1)%bar_length] #?
        
        bar = generate_bar(memory.data_save2) #?
        bar['average']= (bar['close']+bar['high']+bar['low']+bar['open'])/4

        roll_short = bar['average'].rolling(window=short_window).mean()
        roll_long = bar['average'].rolling(window=mid_window).mean()
        bar['short_mavg'] = roll_m13
        bar['mid_mavg'] = roll_m26

        if(bar_X[bar_length-2,'short_mavg']<bar_X[bar_length-2,'mid_mavg'] and bar_X[bar_length-1,'short_mavg']>bar_X[bar_length-1,'mid_mavg']):
            position_new[asset_index] += 1
        if(bar_X[bar_length-2,'short_mavg']>bar_X[bar_length-2,'mid_mavg'] and bar_X[bar_length-1,'short_mavg']<bar_X[bar_length-1'mid_mavg']):
            position_new[asset_index] -= 1
    else:
        memory.data_save.loc[r] = data[asset_index,]


    # End of strategy
    return position_new, memory

