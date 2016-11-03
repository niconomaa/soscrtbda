import pandas as pd 

data_set = pd.read_csv('dmc-2016-train.txt', sep=';')

# Let's select the rows that have no null values. 
cleaned_data = data_set[data_set.notnull().all(axis=1)]  
