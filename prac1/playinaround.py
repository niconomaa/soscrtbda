# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib

matplotlib.style.use('ggplot')

# now you know where i save my uni stuff
df = pd.read_csv("/Users/nicoscordialo/Library/Mobile Documents/com~apple~CloudDocs/Hasso Plattner Institut/Academics/Semester III/Big Data Analytics/Übungen/Praktisch/1/dmc-2016-train.txt", sep=";")

# ex 1
#  BS

# ex 2
# plots average price of product category, quite cool
product_group = df.groupby("productGroup")["price"].mean()
print(product_group)
product_group.plot(kind="bar")

# ex 3
# plots return quantity against...

#
# price
df.plot(x="price", y="returnQuantity", kind="scatter" )

# product category
df.plot(x="productGroup", y="returnQuantity", kind="scatter" )

# color
df.plot(x="colorCode", y="returnQuantity", kind="scatter" )

# size
df.plot(x="sizeCode", y="returnQuantity", kind="scatter" )


#___
# found this more interesting than looking at obscure scatter plots:
# this way you ceate categories for you data
# a sample price categorisation:

 def label_price (row):
    if row['price'] <= 20.00:
       return "Less than 20"
    if row['price'] > 20.00 and row['price'] <= 50.00 :
       return "Less than 50"
    if row['price'] > 50.00 and row['price'] <= 100.00 :
       return "Less than 50"
    else:
        return "Daaaamn"

 df["price_label"] = df.apply (lambda row: label_price (row),axis=1)
