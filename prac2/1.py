import pandas
import matplotlib.pyplot as plt
frame = pandas.read_csv('dmc-2016-cleaned.csv')

# 1

# adds monthOfYear feature
frame["monthOfYear"] = frame["orderDate"].str.extract('(-\d{2}-)').str.replace('-', '')

# adds totalOrderPrice feature
sumGroup = frame.groupby(["orderID"], as_index=False).sum()[["orderID", "price"]]

sumGroup.columns = ["orderID", "totalOrderPrice"]
frame = pandas.merge(frame, sumGroup, on="orderID")

print(frame)


frame.plot(x="totalOrderPrice", y="returnQuantity")
^
# this thr
# frame.plot(x="monthOfYear", y="returnQuantity")

plt.show()
