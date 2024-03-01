import numpy as np 
import pandas as pd 


# Importing the data from  CSV file into a DataFrame object.

data = pd.read_csv("Data-cleaning-for-beginners-using-pandas.csv")

#Creating a copy of the imported data 

data_frame= data.copy()

#Gettign the info on columns 

print("Data table info")
print()
# data_frame.info()

#Starting to work on each column 
#Column 1 : Index it is not necessary so I am dropping it 

data_frame.drop(columns=["Index"],inplace=True)

print("Data table info after dropping the first index  column")
print()
# data_frame.info()
data_frame.dropna(subset=["Age"], inplace=True)

# data_frame.info()

# After dropping rows with na there are a total of 22 rows 

#Column 2 : Age initially has 22 non-null values with float as data type 
#Will convert this column in integer since age should be an integer value

data_frame['Age']=data_frame['Age'].astype(int)


# data_frame.info()

#Column 3 : Salary 
#1 Replace k with 0's 
#2 Remove $ from salary and keep only numbers 

#3 Convert the column into integers


data_frame['Salary']=data_frame['Salary'].apply(lambda x:x.replace('k','000'))

data_frame['Salary']=data_frame['Salary'].apply(lambda x:x.replace('$',''))


data_frame = data_frame.rename(columns={'Salary': 'Salary($)'}) #Renaming the columns for better understanding

# data_frame.info()

#Column 4: Rating 
#Calculating the mean value
mean_rating=data_frame.Rating.mean().round(1)

#Filling Nan values with mean value 
data_frame.Rating.fillna(mean_rating)


#Filling -1 or 0 with mean value 
data_frame['Rating']=data_frame['Rating'].replace({-1:mean_rating,0:mean_rating})

data_frame['Location']=data_frame['Location'].apply(lambda x:x.replace(',',' '))

data_frame['Location']=data_frame['Location'].apply(lambda x:x[::-1].replace(' ',',',1)[::-1])

data_frame['Location'] = data_frame['Location'].apply(lambda x: x.split(',')[0])


#To retrive only the short forms 
# data_frame['Location'] = data_frame['Location'].apply(lambda x: x.split(',')[1])

data_frame.reset_index()

#Column 5: Extablishment Remove all the rows with -1 as entry  in this column

data_frame=data_frame.drop(data_frame[data_frame['Established'] == -1].index)

data_frame=data_frame

print(data_frame.head(5))
# data_frame.info()