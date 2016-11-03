import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

originalData = pd.read_csv('dmc-2016-train.txt', sep=';')

# clean data by dropping all rows that contain some N/A field
originalData = originalData.dropna()

# copy data to not work on original
data = originalData

# print(originalData)

#----------------------- default until here ---------------------

# # orders with more than 30 articles (not neccessarily different ones!) in them
data = originalData.groupby(['orderID'])['quantity'].sum()
data = data.reset_index()
data = data.loc[data['quantity'] > 30]
data = data.sort_values(['quantity'])


# # number of orders w/ 1, 2, 3, ... articles in them
data = originalData.groupby(['orderID'])['quantity'].sum()
data = data.reset_index()
data = data.groupby(['quantity'])['orderID'].count()
data = data.reset_index()

noOfRows = len(data.index)
npArrayToPlot = np.rot90(data.as_matrix())[0]

# this plot sucks ass... suggests that there are orders for every number of articles between 1 and 40...
plt.bar(range(noOfRows), npArrayToPlot, 0.7, color='blue')
plt.yscale('log')
plt.show()


# # what items are returned the most? doesn't work yet
data = originalData
data.groupby(['articleID'])
data = data.reset_index()

# ---------------------- default again --------------------------

print(data)
