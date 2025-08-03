# main.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.title("📊 ABC Inventory Forecast Dashboard")

# Đọc dữ liệu
df = pd.read_excel("ABC_Inventory_300_Rows.xlsx")

# Tiền xử lý
df.drop_duplicates(inplace=True)
df["Branch"] = df["Branch"].str.strip().str.lower()
df["Ingredient"] = df["Ingredient"].str.strip().str.lower()
df["Date"] = pd.to_datetime(df["Date"])

# Hiển thị dữ liệu
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# Biểu đồ 1: Số nguyên liệu khác nhau
st.subheader("🔎 Number of Unique Ingredients")
unique_count = df["Ingredient"].nunique()
st.write(f"There are **{unique_count}** unique ingredients being tracked.")

# Biểu đồ 2: Trung bình tiêu thụ
st.subheader("📊 Average Consumption per Ingredient")
avg_consumed = df.groupby("Ingredient")["Consumed_g"].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.barplot(data=avg_consumed, x="Ingredient", y="Consumed_g", palette="Blues", ax=ax1)
st.pyplot(fig1)

# Biểu đồ 3: Tỷ lệ tồn kho so với ban đầu
st.subheader("📉 Ratio of Ending to Starting Inventory")
df["Inventory_Ratio"] = df["Ending_Inventory_g"] / df["Starting_Inventory_g"]
fig2, ax2 = plt.subplots()
sns.histplot(df["Inventory_Ratio"], bins=20, kde=True, ax=ax2)
st.pyplot(fig2)

# Biểu đồ 4: Cảnh báo tồn kho thấp
st.subheader("🚨 Low-Stock Warnings")
df["Below_Threshold"] = df["Ending_Inventory_g"] < df["Threshold_g"]
low_stock = df[df["Below_Threshold"] == True]
low_counts = low_stock["Ingredient"].value_counts()
fig3, ax3 = plt.subplots()
sns.barplot(x=low_counts.index, y=low_counts.values, palette="Reds", ax=ax3)
ax3.set_ylabel("Number of Warnings")
st.pyplot(fig3)

# Biểu đồ 5: Ending Inventory theo thời gian cho "chicken"
st.subheader("📈 Ending Inventory over Time – Chicken")
df_chicken = df[df["Ingredient"] == "chicken"]
fig4, ax4 = plt.subplots()
sns.lineplot(data=df_chicken, x="Date", y="Ending_Inventory_g", hue="Branch", ax=ax4, marker='o')
plt.xticks(rotation=45)
st.pyplot(fig4)

# Dự báo tồn kho "chicken"
st.subheader("🔮 Forecasting Chicken Inventory (Linear Regression)")
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

st.metric("📏 Mean Squared Error", f"{mse:.2f}")
st.metric("📊 R-squared (R²)", f"{r2:.2f}")

# Dự báo 5 ngày tiếp theo
future_days = 5
future_x = np.arange(len(daily_chicken), len(daily_chicken) + future_days).reshape(-1, 1)
future_pred = model.predict(future_x)
future_dates = pd.date_range(start=daily_chicken["Date"].max() + pd.Timedelta(days=1), periods=future_days)

fig5, ax5 = plt.subplots()
plt.plot(daily_chicken["Date"], daily_chicken["Ending_Inventory_g"], label="Actual", marker="o")
plt.plot(future_dates, future_pred, label="Forecast", linestyle="--", marker="o")
plt.legend()
plt.xticks(rotation=45)
st.pyplot(fig5)
