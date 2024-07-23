import streamlit as st
import pandas as pd

cols = ['product_name', 'aisle', 'department']
file_path = "../data/raw/sample_product_metadata.csv"
df = pd.read_csv(file_path, usecols=cols)

# Add 'add_to_cart' col
df['add_to_cart'] = False

def update_cart():
    updated_data = st.session_state.add_to_cart
    st.write(updated_data)

edited_df = st.data_editor(
    df, 
    disabled=("product_name", "aisle", "department"),
    key="add_to_cart",
    on_change=update_cart
)




