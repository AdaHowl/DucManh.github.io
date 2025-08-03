import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Title
st.title("📊 ABC Inventory Forecasting Dashboard")

# Load data
st.header("1. Load Dataset")
df = pd.read_excel("ABC_Inventory_300_Rows.xlsx")
st.dataframe(df.head())

# Data Cleaning
st.header("2. Data Preprocessing")
df = df.drop_duplicates()
df["Branch"] = df["Branch"].str.strip().str.lower()
df["Ingredient"] = df["Ingredient"].str.strip().str.lower()
df["Date"] = pd.to_datetime(df["Date"])
df["Is_Below_Threshold"] = df["Ending_Inventory_g"] < df["Threshold_g"]
df["Remaining_Ratio"] = df["Ending_Inventory_g"] / df["Starting_Inventory_g"]
st.success("Data cleaned and processed successfully.")

# Summary Stats
st.subheader("Summary Statistics")
st.write(df.describe())

# Visualization 1: Unique Ingredients
st.header("3. Data Visualization")
st.subheader("3.1 Number of Unique Ingredients")
unique_ingredients = df["Ingredient"].nunique()
st.write(f"Number of unique ingredients: **{unique_ingredients}**")

# Visualization 2: Average Consumption
st.subheader("3.2 Average Consumption per Ingredient")
avg_consumed = df.groupby("Ingredient")["Consumed_g"].mean().sort_values()
fig1, ax1 = plt.subplots()
sns.barplot(x=avg_consumed.values, y=avg_consumed.index, palette="Blues_d", ax=ax1)
st.pyplot(fig1)

# Visualization 3: Average Ending Inventory by Branch
st.subheader("3.3 Average Ending Inventory by Branch")
avg_ending = df.groupby("Branch")["Ending_Inventory_g"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
sns.barplot(x=avg_ending.index, y=avg_ending.values, palette="Greens", ax=ax2)
st.pyplot(fig2)

# Visualization 4: Low-Stock Warnings by Ingredient
st.subheader("3.4 Low-Stock Warnings by Ingredient")
low_stock_counts = df[df["Is_Below_Threshold"]]["Ingredient"].value_counts()
fig3, ax3 = plt.subplots()
sns.barplot(x=low_stock_counts.index, y=low_stock_counts.values, palette="Reds", ax=ax3)
st.pyplot(fig3)

# Visualization 5: Distribution of Remaining Ratio
st.subheader("3.5 Distribution of Ending Inventory Ratio")
fig4, ax4 = plt.subplots()
sns.histplot(df["Remaining_Ratio"], bins=10, kde=True, color="purple", ax=ax4)
st.pyplot(fig4)

# Visualization 6: Top 5 Ingredients by Total Consumption
st.subheader("3.6 Top 5 Ingredients by Total Consumption")
total_consumed = df.groupby("Ingredient")["Consumed_g"].sum().sort_values(ascending=False).head(5)
fig5, ax5 = plt.subplots()
sns.barplot(x=total_consumed.index, y=total_consumed.values, palette="coolwarm", ax=ax5)
st.pyplot(fig5)

# Forecasting Model
st.header("4. Forecasting Inventory - Linear Regression")
df_chicken = df[df["Ingredient"] == "chicken"].copy()
daily_chicken = df_chicken.groupby("Date")["Ending_Inventory_g"].sum().reset_index()
daily_chicken["Day_Number"] = np.arange(len(daily_chicken))

X = daily_chicken[["Day_Number"]]
y = daily_chicken["Ending_Inventory_g"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.metric("Mean Squared Error (MSE)", f"{mse:.2f}")
st.metric("R-squared (R²)", f"{r2:.2f}")

# Visualization: Prediction vs Actual
st.subheader("4.1 Prediction vs Actual - Chicken Inventory")
fig6, ax6 = plt.subplots()
ax6.plot(X_test, y_test.values, label="Actual", marker='o')
ax6.plot(X_test, y_pred, label="Predicted", linestyle='--', marker='o')
ax6.set_title("Inventory Forecast (Linear Regression)")
ax6.set_xlabel("Day Number")
ax6.set_ylabel("Ending Inventory (grams)")
ax6.legend()
ax6.grid(True)
st.pyplot(fig6)

st.success("✅ Forecasting complete. App ready to deploy!")
