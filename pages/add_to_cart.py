import streamlit as st
import pandas as pd

df = pd.read_csv("../data/raw/sample_product_metadata.csv")

edited_df = st.data_editor(df)
