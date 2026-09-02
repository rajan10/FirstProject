import pandas as pd
import os
products = {
    "Product":["Laptop","Mouse","Keyboard","Monitor","Printer"],
    "Category":["Electronics","Accessories","Accessories","Electronics","Electronics"],
    "Price":[60000,500,1200,15000,10000],
    "Stock":[15,200,120,25,18]
}
df=pd.DataFrame(products)
print("-"*50)
print("Question 1: Show products above 10,000")
above_10k = df[df["Price"] > 10000]
print(above_10k)
print("-"*50)
print("Question 2: Sort by price")
df_sorted = df.sort_values("Price", ascending=False)
print(df_sorted)
print("-"*50)
print("Question 3: Count products by category")
category_counts = df["Category"].value_counts()
print(category_counts)
print("-"*50)
print("Question 4: Find average price by category")
avg_price_by_category = df.groupby("Category")["Price"].mean()
print(avg_price_by_category)
print("-"*50)
print("Question 5: Add GST (18%)")
df["GST"] = df["Price"] * 0.18
print(df)
print("-"*50)
print("Question 6: Calculate Final Price")
df["Final Price"] = df["Price"] + df["GST"]
print(df)
print("-"*50)
print("Question 7: Save to CSV")
df.to_csv("products.csv", index=False)
print("File saved at:", os.path.abspath("products.csv"))

print("-"*50)
df_read = pd.read_csv("products.csv")
print("Data read from CSV:")
print(df_read)