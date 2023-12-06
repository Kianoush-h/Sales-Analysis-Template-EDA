
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""




# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set style of visualization
sns.set_style("darkgrid")
sns.set_palette("RdBu")


# =============================================================================
# Gathering data from raw data
# =============================================================================

# read data set
data = pd.read_excel("data/Coffee Shop Sales.xlsx")

# see top 5 rows
head = data.head()


# see number of rows and columns
print(f" shape is: {data.shape}")

# check missing values
data.isna().sum()

# see quick info
data.info()

data.describe()


# check duplicated rows
data.duplicated().any()


# see unique values in each column

# 1- create new data frame with number of unique value in each column
columnValue = data.nunique().reset_index()

# 2- rename column name 
columnValue.rename(columns = {"index" : "Column _name", 0 : "Uniue values"}, inplace = True)

# 3- see columns and number of unique values of each
print(columnValue)





























