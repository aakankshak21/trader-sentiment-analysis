import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Performance vs Market Sentiment")

df = pd.read_csv("data/final_trader_dataset.csv")

regime = st.selectbox("Select Sentiment Regime", df['sentiment_group'].unique())

filtered = df[df['sentiment_group'] == regime]

st.subheader("Summary Statistics")
st.write(filtered[['closed_pnl','trade_count','size_usd','long_ratio']].describe())

st.subheader("PnL Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered['closed_pnl'], bins=20, ax=ax)
st.pyplot(fig)