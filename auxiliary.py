def generate_bar(data):
    ## Data is a pandas dataframe
    import pandas as pd

    OHLC = pd.DataFrame(data, columns = ['open', 'high', 'low', 'close', 'volume_ave'])
 
   
    
    return OHLC