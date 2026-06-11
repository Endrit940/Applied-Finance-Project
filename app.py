import streamlit as st
from stock_data import get_stock_data

st.title("Applied Finance")

ticker = st.text_input("Ticker", "AAPL")

if st.button("Laden"):
    data = get_stock_data(ticker)

    st.line_chart(data["Close"])

    st.dataframe(data.tail())