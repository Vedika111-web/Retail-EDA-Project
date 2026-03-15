# Exploratory Data Analysis (EDA)
# Project 1 - Retail Sales and McDonalds Menu Analysis
# Tools: Python, Pandas, Matplotlib

# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt


# =========================================
# DATASET 1 : RETAIL SALES DATA ANALYSIS
# =========================================

# load dataset
data = pd.read_csv("retail_sales_dataset.csv")

# Dataset preview
print(data.head())

# Dataset Information
print("\nDataset Information:")
print(data.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe()) 

print("\nMissing Values:")
print(data.isnull().sum())

# Gender distribution
print("\nGender Distribution:")
print(data["Gender"].value_counts())

# Product category distribution
print("\nProduct Category Distribution:")
print(data["Product Category"].value_counts())

# Bar chart for product categories
data["Product Category"].value_counts().plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Purchases")

plt.show()

# Age distribution
data["Age"].plot(kind="hist", bins=10)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# Revenue by Product Category
category_revenue = data.groupby("Product Category")["Total Amount"].sum()

category_revenue.plot(kind="bar")

plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")

plt.show()

# Sales Trend Over Time
data["Date"] = pd.to_datetime(data["Date"])

sales_trend = data.groupby("Date")["Total Amount"].sum()

sales_trend.plot()

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.show()

# --------------------------------
# Insights from Retail Sales EDA
# --------------------------------

# 1. The dataset contains 1000 transactions and 9 columns.
# 2. No missing values were found in the dataset.
# 3. Clothing category recorded the highest number of purchases.
# 4. Electronics and Beauty categories also contributed significantly to sales.
# 5. Most customers fall between the age group of 30–50 years.
# 6. Sales vary across different dates, indicating changing purchasing patterns.



# =========================================
# DATASET 2 : MCDONALDS MENU DATA ANALYSIS
# =========================================
menu = pd.read_csv("menu.csv")

# Dataset preview
print("\nFirst Rows of Menu Dataset:")
print(menu.head())

# Dataset information
print("\nMenu Dataset Info:")
print(menu.info())

# Descriptive statistics
print("\nMenu Descriptive Statistics:")
print(menu.describe())

# Average calories by category
calories_category = menu.groupby("Category")["Calories"].mean()

calories_category.plot(kind="bar")

plt.title("Average Calories by Menu Category")
plt.xlabel("Category")
plt.ylabel("Average Calories")

plt.show()

# Calories Distribution
menu["Calories"].plot(kind="hist", bins=10)

plt.title("Calories Distribution of Menu Items")
plt.xlabel("Calories")
plt.ylabel("Frequency")

plt.show()

# Missing values check
print("\nMissing Values in Menu Dataset:")
print(menu.isnull().sum())

# --------------------------------
# Insights from McDonalds Menu Dataset
# --------------------------------

# 1. The dataset contains nutritional information of McDonald's menu items.
# 2. Categories like Chicken & Fish and Breakfast have higher average calories.
# 3. Beverages and salads generally contain fewer calories.
# 4. Calorie values vary significantly across different menu categories.