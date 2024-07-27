import time
import streamlit as st
from app.utils.resources import init_resources
from app.utils.ui_components import sidebar_menu
from app.recommender.llm_recommender import get_cart_recommendations

# Set Page Title
st.set_page_config(
    page_title="Cart Recommendations"
)
# Initialize the resources
init_resources()
# Sidebar Menu
sidebar_menu()

def display_text():
    st.write("Ohh ohh! :blue[No product] is added to the cart yet. 😅")
    st.write("Please visit to the following page and add the products to the cart.")
    st.page_link("pages/add_to_cart.py", label="👉 &nbsp; Click here.")


def main():
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>Cart Recommendations</h1>
    <div style='text-align: left; color: #7f7f7f; font-size: 17px;'>
    To get recommedations about what to buy next, add items to your cart.
    </div>
    <hr>
    """, unsafe_allow_html=True)
    # st.divider()
    if 'add_to_cart_products' not in st.session_state:
        display_text()
        
    else:
        if st.session_state.add_to_cart_products == []:
            display_text()
        else:
            st.subheader("Products in the cart:")
            st.write(st.session_state.add_to_cart_products)
            st.subheader("What to buy next:")
            with st.spinner('Wait for it...'):
                time.sleep(5)
                result = get_cart_recommendations(
                    st.session_state.add_to_cart_products,
                    st.session_state.llm,
                    st.session_state.chroma_client,
                    5)
                print(type(result))
                print(result)
                st.write(result)

if __name__ == "__main__":
    main()