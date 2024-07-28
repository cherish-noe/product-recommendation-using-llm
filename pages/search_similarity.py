import time
import streamlit as st
from app.utils.resources import init_resources
from app.utils.ui_components import sidebar_menu, load_css
from app.recommender.llm_recommender import get_similar_products

# Set Page Title
st.set_page_config(
    page_title="Similar Products"
)
# Initialize the resources
init_resources()
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

def main():
    # ffad69
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>Similar Products</h1>
    <div style='text-align: left; color: #7f7f7f; font-size: 17px;'>
    To get recommedations about what to buy next, add items to your cart.
    </div>
                <hr>
    """, unsafe_allow_html=True)

    st.subheader("Search Product:")
    search_form = st.form("search_form")
    product_name = search_form.text_input('Search product:', 'Milk tea')
    search_submit = search_form.form_submit_button(label="Submit")

    if search_submit:
        st.subheader("Products like this:")
        with st.spinner('Wait for it...'):
            time.sleep(5)
            results = get_similar_products(product_name, st.session_state.llm, st.session_state.chroma_client, 5)
            st.write(results)

if __name__ == "__main__":
    main()