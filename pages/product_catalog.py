import pandas as pd
import streamlit as st
from app.utils.ui_components import sidebar_menu, load_css

# Set Page Title
st.set_page_config(
    page_title="Product Catalog",
    layout="wide"
)
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

def main():
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>Product Catalog</h1>
    <div style='text-align: left; color: #7f7f7f; font-size: 17px;'>
    Here is the list of the products available in the store.
    </div>
    <hr>
    """, unsafe_allow_html=True)

    @st.cache_data
    def read_data():
        cols_to_read = ['product_name', 'aisle', 'department']
        df = pd.read_csv("app/data/processed/product_metadata.csv", usecols=cols_to_read)
        df = df.iloc[:5000]
        return df
    
    df = read_data()
    
    with st.container():
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "product_name": "Product Name",
                "aisle": "Aisle",
                "department": "Department"
            },
            hide_index=True
        )

if __name__ == "__main__":
    main()

