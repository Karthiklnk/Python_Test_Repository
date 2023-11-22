#!/usr/bin/env python
# coding: utf-8

# <div style="background-color: #104F60; padding: 20px; text-align: center;">
#     <h1 style="color: #ffdf; font-size: 32px; font-weight: bold; letter-spacing: 1px; margin: 0;">Performing data analysis in Python with the Pandas library and saving the results to MySQL Workbench.</h1>
# </div>

# In[3]:


# Import the required libraries

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pymysql


# In[4]:


#Read csv file into a Datafram 'df'

df = pd.read_csv("youtube_dataset.csv")


# In[5]:


# Verify if the dataset is loaded properly

df.head()


# In[6]:


df.tail()


# In[7]:


# Verify the no. of rows and columns of the dateset

df.shape


# In[8]:


# Verify the characteristics of the columns/variables

df.dtypes


# <div style="background-color: #204F60; padding: 20px; text-align: center;">
#     <h1 style="color: #fff; font-size: 24px; font-weight: bold; letter-spacing: 1px; margin: 0;">Create a function to calculate the distribution of channeltype from the top 1000 records.
# </h1>
# </div>

# In[9]:


# Define the function

def dist_channel_1000records(dataset):
    
    # Take the top 1000 records i.e, the top 1000 channels
    df_top_1000_records = dataset[:1000]
    
    # 'NaN' values in the column 'channeltype' are replaced with string 'N.A'    
    df_top_1000_records.channeltype = df_top_1000_records.channeltype.fillna('N.A')
    
    # Calculate the distribution of channel type from the top 1000 records and store it in a dictionary
    channel_type_dist = df_top_1000_records['channeltype'].value_counts().to_dict()
    
    # Return the values of the distribution
    return channel_type_dist


# In[10]:


# Call the function and print the result

df_top1000_records = dist_channel_1000records(df)
print(df_top1000_records)


# In[11]:


# Plot the Distribution of the 1000 channels

def plot_distribution(df_top1000_records):
    # Extract the values from the dictionary into two lists
    channel_types = list(df_top1000_records.keys())
    frequency = list(df_top1000_records.values())

    # Set the graph size
    plt.figure(figsize=(10, 6))  

    # Create the barplot
    plt.bar(channel_types, frequency, color='springgreen')

    # Set labels and title
    plt.xlabel('Channel Type')
    plt.ylabel('Frequency')
    plt.title('Distribution of Channel Types of top 1000 youtube channels')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()


# In[12]:


# Call the function and plot the graph

plot_distribution(df_top1000_records)


# <div style="background-color: #204F60; padding: 20px; text-align: center;">
#     <h1 style="color: #fff; font-size: 24px; font-weight: bold; letter-spacing: 1px; margin: 0;">Load only the top 1000 records of the original 4000 into a separate CSV file, and to a database table. (You have to export the csv file from python and load the file into MYSQL).
# </h1>
# </div>

# <div style="background-color: #204F60; padding: 10px; text-align: center;">
#     <h1 style="color: #fff; font-size: 20px; font-weight: normal;">A connection is established between Python and MySQL workbench. The User Name, Password and Database name are given as agruments in the function create_engine</h1>
# </div>

# In[13]:


# Create engine
# REPLACE THE FOLLOWING
# User_name:password WITH YOUR USER NAME AND PASSWORD
# youtube WITH YOUR DATABASE NAME

engine = create_engine('mysql+pymysql://User_name:password@localhost/youtube')


# In[14]:


# Specify the connection string
conn = engine.connect()


# In[15]:


# Take the top 1000 records i.e, the top 1000 channels
df_top_1000_records = df[:1000]


# In[16]:


# Create a CSV file from the DataFrame
df_top_1000_records.to_csv('csv_top1000_records')


# In[33]:


# Load CSV file into MySQL table
df_csv = pd.read_csv("csv_top1000_records")
df_csv.to_sql('csv_top1000_records', conn, if_exists='replace', index=False)

