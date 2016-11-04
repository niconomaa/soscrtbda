import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

originalData = pd.read_csv('../../1p/dmc-2016-train.txt', sep=';')

# clean data by dropping all rows that contain some N/A field
originalData = originalData.dropna()

# copy data to not work on original
data = originalData

# print(originalData)

#----------------------- default until here ---------------------

# # orders with more than 30 articles (not neccessarily different ones!) in them
# data = originalData.groupby(['orderID'])['quantity'].sum()
# data = data.reset_index()
# data = data.loc[data['quantity'] > 30]
# data = data.sort_values(['quantity'])


# # number of orders w/ 1, 2, 3, ... articles in them
# data = originalData.groupby(['orderID'])['quantity'].sum()
# data = data.reset_index()
# data = data.groupby(['quantity'])['orderID'].count()
# data = data.reset_index()
#
# noOfRows = len(data.index)
# npArrayToPlot = np.rot90(data.as_matrix())[0]

# this plot sucks ass... suggests that there are orders for every number of articles between 1 and 40...
# plt.bar(range(noOfRows), npArrayToPlot, 0.7, color='blue')
# plt.yscale('log')
# plt.show()


# # this might help reducing shipping costs: Figure out which of the most-ordered articles are returned most!
# data = data.groupby('articleID').agg({'quantity': np.sum, 'returnQuantity': np.sum})
# data = data.reset_index()
#
# data['rQdivByQ'] = pd.Series((data['returnQuantity'] / data['quantity']), index=data.index)
# # most ordered articles was ordered 27000 times, there are a bunch that were ordered more than 3000 times...
# data = data.loc[data['quantity'] > 3000]
# data = data.sort_values(['rQdivByQ'], ascending=False)

# # How many percent of the articles were returned on average in orders with 1, 2, 3, 4, ... articles in them?
data = data.groupby('orderID').agg({'quantity': np.sum, 'returnQuantity': np.sum})
data = data.reset_index()

data['rQdivByQ'] = pd.Series((data['returnQuantity'] / data['quantity']), index=data.index)

data = data.groupby('quantity')['rQdivByQ'].mean()
data = data.reset_index()

noOfRows = len(data.index)
npArrayToPlot = np.rot90(data.as_matrix())[0]

plt.bar(range(noOfRows), npArrayToPlot, 0.7, color='red')
plt.show()
# # not surprising but still rather interesting plot: up to around 16 items per order, people tend to send back more articles the more articles they ordered

# ---------------------- default again --------------------------

print(data)
