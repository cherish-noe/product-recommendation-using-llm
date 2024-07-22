import pandas as pd
import streamlit as st

df = pd.read_csv("../data/raw/product_metadata.csv")
df_10 = df.head(10)

st.table(df_10)

