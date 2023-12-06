
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

# See quick info of numeric data
data.describe()

# see quick info of categorical data
data.describe(include = object)

# check duplicated rows
data.duplicated().any()


# see unique values in each column

# 1- create new data frame with number of unique value in each column
columnValue = data.nunique().reset_index()

# 2- rename column name 
columnValue.rename(columns = {"index" : "Column _name", 0 : "Uniue values"}, inplace = True)

# 3- see columns and number of unique values of each
print(columnValue)


# drop some columns such as "product_id", "transaction_id" and "store_id"
data.drop(columns = ["transaction_id", "store_id", "product_id"], inplace = True)



# =============================================================================
# Analysis & Visualizations 
# =============================================================================

# create function to visualized categorical column using count plot

def count_plot(x_axis = None, y_axis = None, hue = None, rotation = 0, top = None):
    """
    1) input : x_axis, column name, data type must be object or categorical
    3) output : cout plot using seaborn modules, unique values in x-axis and frequency in y-axis
    4) use bar_label to show frequency of each unique values above each column in graph
    5) top parameter i use it to specify indexes i want to see it
    """
    if x_axis: # if we neet to visualized in x-axis
        order = data[x_axis].value_counts().iloc[:top].index
        
    else : # if we neet to visualized in y-axis
        order = data[y_axis].value_counts().iloc[:top].index
        
    graph = sns.countplot(x = x_axis, y = y_axis, data = data, hue = hue, order = order, palette = "RdBu")
    for container in graph.containers:
        graph.bar_label(container)
        
        
    plt.xticks(rotation = rotation)
    plt.show()
# create function that visualized categorical column using pie plot

def pie_plot(column_name, explodeIndex = None):
    """
    1) input : column name, column data type must be object or categorical
    2) explodeIndex, is the index i need to explode it 
    2) output : circle chart that shows size of each unique values and percentage 
    """
    # Create explode list with zeros of size equal to the number of unique values
    explodeList = [0] * data[column_name].nunique()
    
    # Check and set explodeIndex value 
    if explodeIndex is not None:
        explodeList[explodeIndex] = 0.1
    
    # Create pie plot
    plt.pie(data[column_name].value_counts(), labels = data[column_name].value_counts().index, shadow = True, autopct = "%1.1f%%",  explode = explodeList)
    plt.show()


# =============================================================================
# PART 1: Discovering transaction_date column
# =============================================================================



# Extract some information such as year , month and day

# add new column year
data["year"] = data["transaction_date"].dt.year

# add new column month
data["month"] = data["transaction_date"].dt.month_name()

# add new column day
data["day"] = data["transaction_date"].dt.day_name()



# =============================================================================
# PART 2: transactions over months 
# =============================================================================

# see number of transaction in each month
count_plot(x_axis = "month")
plt.title("Sales Over Months")

# =============================================================================
# PART 3: transactions over days of week
# =============================================================================

# see top 5 day of transaction
# set figure size
plt.figure(figsize = (10,6))

# call function i create it in cell 12
count_plot(x_axis = "day")
plt.title("Transaction Over Days of Week")


# =============================================================================
# PART 4: transactions over hours
# =============================================================================

data["hour"] = data["transaction_time"].apply(lambda x : x.hour)

# see distribution

sns.kdeplot(data["hour"])
plt.show()
plt.title("Transaction Over Hours")


# =============================================================================
# PART 5: Discovering transaction_qty column
# =============================================================================

# see number of sales quantity  
count_plot(x_axis = "transaction_qty")
plt.title("Sales Over Transaction Quantity")




# =============================================================================
# PART 6: Discovering store_location column
# =============================================================================

# see number of sales in each store

pie_plot(column_name = "store_location", explodeIndex = 0)
plt.title("Sales in Each Store")


# =============================================================================
# PART 7: Discovering product_category column
# =============================================================================

# see most common category

# set figure size
plt.figure(figsize = (15,6))

# call function i create it in cell 12
count_plot(x_axis = "product_category")  
plt.title("Most Common Category")




# =============================================================================
# PART 8: Discovering product_type column
# =============================================================================

# Assuming 'counts' is the DataFrame obtained from your groupby operation
counts = data.groupby(["product_category", "product_type"]).size().reset_index(name = "count")

# Get unique categories
categories = counts['product_category'].unique()

# Create subplots for each category in a 4x2 grid
fig, axes = plt.subplots(5, 2, figsize = (15, 20))

# Flatten the axes for easier iteration
axes = axes.flatten()

for i, category in enumerate(categories):
    # Filter data for each category
    subset = counts[counts['product_category'] == category]
    
    # Sort the data by 'count' column in descending order
    subset = subset.sort_values('count', ascending = False)
    
    # Create a bar plot for each category with sorted order
    sns.barplot(x = 'count', y = 'product_type', data = subset, ax = axes[i], order = subset['product_type'])
    axes[i].set_title(f'Product Types in {category}')
    axes[i].set_ylabel('')
    axes[i].set_xlabel('')
    axes[i].tick_params(axis = 'x', rotation = 45)
    axes[i].grid(True)
    
    # Adding bar labels
    for idx, bar in enumerate(axes[i].patches):
        axes[i].text(bar.get_width(), bar.get_y() + bar.get_height() / 2, subset.iloc[idx]['count'], ha = 'left', va = 'center')

# Hide extra subplots if there are fewer categories than subplots
for j in range(len(categories), len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()





























