import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


st.title("📊 ABC Inventory Forecasting Dashboard")

# Upload file Excel nếu cần
df = pd.read_excel("ABC_Inventory_300_Rows.xlsx")
st.subheader("Preview Dataset")
st.dataframe(df.head())

df = df.drop_duplicates()
df["Branch"] = df["Branch"].str.strip().str.lower()
df["Ingredient"] = df["Ingredient"].str.strip().str.lower()
df["Date"] = pd.to_datetime(df["Date"])

st.subheader("📈 Tồn kho nguyên liệu 'Chicken' theo thời gian")
df_chicken = df[df["Ingredient"] == "chicken"]
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_chicken, x="Date", y="Ending_Inventory_g", hue="Branch", marker="o")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)


st.subheader("📉 Dự báo tồn kho cho 'chicken'")
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

st.metric("📏 Mean Squared Error (MSE)", f"{mse:.2f}")
st.metric("📊 R-squared (R²)", f"{r2:.2f}")


st.subheader("🔮 Dự báo tồn kho 5 ngày tới")
future_days = 5
future_x = np.arange(len(daily_chicken), len(daily_chicken) + future_days).reshape(-1, 1)
future_pred = model.predict(future_x)
future_dates = pd.date_range(start=daily_chicken["Date"].max() + pd.Timedelta(days=1), periods=future_days)

plt.figure(figsize=(10, 5))
plt.plot(daily_chicken["Date"], daily_chicken["Ending_Inventory_g"], label="Thực tế", marker="o")
plt.plot(future_dates, future_pred, label="Dự đoán", linestyle="--", marker="o")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
