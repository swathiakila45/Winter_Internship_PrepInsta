import numpy as np 
import pandas as pd 


# Importing the data from  TSV file into a DataFrame object.

data = pd.read_csv("chipotle.tsv",delimiter='\t')

#Creating a copy of the imported data 

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
print(grouped_df.head(5))




