import pandas as pd
import numpy as np
# !pip install CHAID[graph]
# !pip install graphviz
# !pip install treelib
# !pip install graphviz
# !apt-get install graphviz
from treelib import Tree as TreeLib
from CHAID import Tree, NominalColumn
import time

# Read the data from the Excel file
data = pd.read_excel('Group1&2 - DecisionTree & CHAID.xlsx')

# Use only the first 10 rows
data = data.head(100)

# Rename columns to match those used in the script (optional)
data.columns = ['SNo', 'SDG', 'Overview', 'Founded_Year', 'Country', 'State', 'City', 'Is_Funded', 'Total_Funding', 'Annual_Revenue', 'Latest_12_month_growth', 'Annual_Net_Profit', 'Total_Employee_Count']

# Drop the 'SNo' and 'Overview' columns as they are not used in the model
data = data.drop(columns=['SNo', 'Overview'])

# Convert categorical variables to category type
data['Is_Funded'] = data['Is_Funded'].astype('category')
data['SDG'] = data['SDG'].astype('category')
data['Country'] = data['Country'].astype('category')
data['State'] = data['State'].astype('category')
data['City'] = data['City'].astype('category')

# Convert 'Latest_12_month_growth' from percentage strings to numeric values
data['Latest_12_month_growth'] = data['Latest_12_month_growth'].str.rstrip('%').astype(float)

# Handle missing values (using median for numerical, mode for categorical)
data['Total_Funding'].fillna(data['Total_Funding'].median(), inplace=True)
data['Annual_Revenue'].fillna(data['Annual_Revenue'].median(), inplace=True)
data['Latest_12_month_growth'].fillna(data['Latest_12_month_growth'].median(), inplace=True)
data['Annual_Net_Profit'].fillna(data['Annual_Net_Profit'].median(), inplace=True)
data['Total_Employee_Count'].fillna(data['Total_Employee_Count'].median(), inplace=True)
data['State'].fillna(data['State'].mode()[0], inplace=True)
data['City'].fillna(data['City'].mode()[0], inplace=True)

# Prepare columns for CHAID
independent_variable_columns = ['SDG', 'Founded_Year', 'Country', 'State', 'City', 'Total_Funding', 'Annual_Revenue', 'Latest_12_month_growth', 'Annual_Net_Profit', 'Total_Employee_Count']
dep_variable = 'Is_Funded'

# Convert to NominalColumn
cols = [NominalColumn(data[col], name=col) for col in independent_variable_columns]

# Create the CHAID Tree
tree = Tree(cols, NominalColumn(data[dep_variable], name=dep_variable), {'min_child_node_size': 5})
ex_tree = Tree(cols, NominalColumn(data[dep_variable], name=dep_variable), {'min_child_node_size': 5, 'is_exhaustive':True})


tree.render("tree" + str(time.time()))
tree_lib = tree.to_tree()
tree_lib.save2file('tree')

ex_tree.render("ex_tree" + str(time.time()))
ex_tree_lib = ex_tree.to_tree()
ex_tree_lib.save2file('ex_tree')