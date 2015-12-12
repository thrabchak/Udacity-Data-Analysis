import pandas as pd

# Adding using +
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s
    
# Adding with axis='index'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='index')
    # The functions sub(), mul(), and div() work similarly to add()
    
# Adding with axis='columns'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    my_axis = 'columns'
    other_axis = 'rows'
    
    mean_df = df.mean(axis=my_axis, ddof=0)
    sub_df = df.sub(mean_df, axis=other_axis)
    std_df = df.std(axis=my_axis, ddof=0)
    standardized_df = sub_df.div(std_df, axis=other_axis)
    
    print df
    print ''
    print mean_df
    print ''
    print sub_df
    print ''
    print std_df
    print ''
    print standardized_df
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''    
    return (df - df.mean(axis=0, ddof=0)) / df.std(axis=0, ddof=0)

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''
    my_axis = 'columns'
    other_axis = 'rows'
    
    mean_df = df.mean(axis=my_axis, ddof=0)
    sub_df = df.sub(mean_df, axis=other_axis)
    std_df = df.std(axis=my_axis, ddof=0)
    standardized_df = sub_df.div(std_df, axis=other_axis)
    
    print df
    print ''
    print mean_df
    print ''
    print sub_df
    print ''
    print std_df
    print ''
    print standardized_df
    
    return standardized_df

standardize_rows(grades_df)
