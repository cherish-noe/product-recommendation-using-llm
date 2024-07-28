import pandas as pd
import streamlit as st
from app.utils.ui_components import sidebar_menu, load_css

# Set Page Title
st.set_page_config(
    page_title="Product Catalog"
)
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

def main():
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>Product Catalog</h1>
    <div style='text-align: left; color: #7f7f7f; font-size: 17px;'>
    To get recommedations about what to buy next, add items to your cart.
    </div>
    <hr>
    """, unsafe_allow_html=True)

    cols_to_read = ['product_name', 'aisle', 'department']
    df = pd.read_csv("data/raw/product_metadata.csv", usecols=cols_to_read)
    df_10 = df.head(20)

    st.dataframe(
        df_10,
        column_config={
            "product_name": "Product Name",
            "aisle": "Aisle",
            "department": "Department"
        },
        hide_index=True
    )

if __name__ == "__main__":
    main()

