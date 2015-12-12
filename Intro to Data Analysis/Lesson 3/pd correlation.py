import pandas as pd

filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    x_mean = x.mean()
    x_std = x.std(ddof=0)
    x_normalized = (x - x_mean) / x_std
    
    y_mean = y.mean()
    y_std = y.std(ddof=0)
    y_normalized = (y - y_mean) / y_std
    
    #return (x_normalized * y_normalized).mean()
    return x.corr(y)

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print correlation(entries, rain)
print correlation(entries, temp)
print correlation(rain, temp)

print correlation(entries, cum_entries)
