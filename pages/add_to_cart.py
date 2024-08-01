import streamlit as st
import pandas as pd
from app.utils.ui_components import sidebar_menu, load_css, custom_button

# Set Page Title
st.set_page_config(
    page_title="Add To Cart",
    layout="wide"
)
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

# def update_cart():
#     updated_data = st.session_state.add_to_cart
#     # print(updated_data)
#     # edited_rows = updated_data['edited_rows']
#     # edited_keys = list(edited_rows.keys())
#     # print(edited_keys)

def main():
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>Add to Cart</h1>
    <p style='text-align: left; color: #7f7f7f; font-size: 17px;'>
    To get recommedations about what to buy next, add items to your cart.
    </p>
    <hr>
    """, unsafe_allow_html=True)

    @st.cache_data
    def read_data():
        cols = ['product_name', 'aisle', 'department']
        file_path = "app/data/processed/product_metadata.csv"
        df = pd.read_csv(file_path, usecols=cols)
        df = df.iloc[:5000]
        return df

    df = read_data()

    # Add 'add_to_cart' col
    df['add_to_cart'] = False
        
    st.session_state['edited_df'] = st.data_editor(
        df, 
        height=350,
        use_container_width=True,
        hide_index=True,
        column_config={
        "product_name": "Product Name",
        "aisle": "Aisle",
        "department": "Department",
        "add_to_cart": "Add to Cart"
        },
        disabled=("product_name", "aisle", "department"),
        key="add_to_cart"
        # on_change=update_cart
    )
    
    edited_rows = st.session_state.edited_df[st.session_state.edited_df['add_to_cart']==True]
    edited_names = edited_rows['product_name'].tolist()
    print(f"names:{edited_names}")

    st.session_state['add_to_cart_products'] = edited_names

    col1, col2, col3 = st.columns([0.7, 0.18, 0.2])

    with col1:
        st.text("")

    with col2:
        st.text("")

    with col3:
        view_cart_submit = custom_button(button_label="View cart &nbsp; 🛒", key="view_cart_submit")
        if view_cart_submit:
            st.switch_page("pages/view_cart.py")

if __name__ == "__main__":
    main()
 








