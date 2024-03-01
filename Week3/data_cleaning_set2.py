import numpy as np 
import pandas as pd 


# Importing the data from  TSV file into a DataFrame object.

data = pd.read_csv("chipotle.tsv",delimiter='\t')

#Creating a copy of the imported data 

# print(data.head(1))
df= data.copy()

#Step1: Convert item_price to float

df['item_price'] = df['item_price'].str.replace('$','').astype(float)
# df['item_price'] = pd.to_numeric(df['item_price'])


#Step2 : Missing Values:
#Only Choice_Description column has null values and since the corresponding item name ofthe choice_description does not have description elsewhere moving forward to next step

#Step 4 : Duplicated Entries 

#To remove duplicated order_id values I hav grouped them into one order id and stored it in new data_frame

grouped_df = df.groupby('order_id').agg({
    'quantity': list,
    'item_name': list,
    'choice_description': list,
    'item_price': list
}).reset_index()

# Display the grouped DataFrame
# print(grouped_df.head(5))

# Quantity for Each Item and top 5 items with most quantity ordered 

c=df.groupby('item_name').sum()
c=c.sort_values(['quantity'],ascending=False)

# print(c.head(5))
# #Output
#                      order_id  quantity                                 choice_description  item_price
# item_name
# Chicken Bowl           713926       761  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...     7342.73
# Chicken Burrito        497303       591  [Tomatillo-Green Chili Salsa (Medium), [Pinto ...     5575.82
# Chips and Guacamole    449959       506                                                  0     2201.04
# Steak Burrito          328437       386  [Tomatillo Red Chili Salsa, [Fajita Vegetables...     3851.43
# Canned Soft Drink      304753       351  [Coke][Sprite][Coke][Coke][Lemonade][Sprite][D...      438.75

#most ordered based on choice_description 

cd=df.groupby('choice_description').sum()
cd=cd.sort_values(['quantity'],ascending=False)
# print(cd[['item_name','quantity']].head(1))
# #Output
#  item_name  quantity

# [Diet Coke]      159

#total orders in total 
total_order= df.quantity.sum()
print(total_order)

#Output 4972

#Total revenue 
total_revenue = df.item_price.sum()
print(total_revenue)

#Output 34500.16

#total orders made in the period 
total_order_based_on_orderid = df.order_id.value_counts().count()
print(total_order_based_on_orderid )

#Output 1834 

df['revenue']=df['quantity']*df['item_price']


ar=df.groupby(by=['order_id']).sum()

print(ar['revenue'].head(5))

print(ar['revenue'].mean())


#Output : 21.39423118865867

#How many different items are sold 
different_items_sold= df.item_name.nunique()
print(different_items_sold)

#Output : 50








