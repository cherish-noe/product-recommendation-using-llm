import streamlit as st
import pandas as pd
from app.utils.ui_components import sidebar_menu

# Set Page Title
st.set_page_config(
    page_title="Add To Cart"
)
# Sidebar Menu
sidebar_menu()

def update_cart():
    updated_data = st.session_state.add_to_cart
    # print(updated_data)
    # edited_rows = updated_data['edited_rows']
    # edited_keys = list(edited_rows.keys())
    # print(edited_keys)

def main():
    st.header("Add to Cart")
    cols = ['product_name', 'aisle', 'department']
    file_path = "data/raw/sample_product_metadata.csv"
    df = pd.read_csv(file_path, usecols=cols)

    # Add 'add_to_cart' col
    df['add_to_cart'] = False
        
    edited_df = st.data_editor(
        df, 
        disabled=("product_name", "aisle", "department"),
        key="add_to_cart",
        on_change=update_cart
    )
    edited_rows = edited_df[edited_df['add_to_cart']==True]
    edited_names = edited_rows['product_name'].tolist()
    print(edited_names)

    st.session_state['add_to_cart_products'] = edited_names

    view_cart_submit = st.button("View Cart")
    if view_cart_submit:
        st.switch_page("pages/view_cart.py")

if __name__ == "__main__":
    main()
 








