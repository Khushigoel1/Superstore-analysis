import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("superstore.csv",encoding="latin1")
print(df["Profit"].sum())#total profit 
print(df["Sales"].sum())#total sales

# Scatter plot (Sales vs Profit)
plt.figure(figsize=(8,6))
plt.scatter(df["Sales"],df["Profit"],color="pink")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# Top 10 products by sales
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10)
print(top_products)

# Sales by Region (grouped)
plt.bar(df["Region"],df["Sales"],color="green")
plt.title("sales in different regions")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

#category vs sales grouped bar chart
df.groupby("Category")["Sales"].sum().plot(kind="bar",color="blue")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()