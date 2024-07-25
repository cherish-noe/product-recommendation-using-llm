import streamlit as st
from app.utils.resources import init_resources
from app.recommender.llm_recommender import get_similar_products

# Initialize the resources
init_resources()

def main():

    st.title("Similar Products")
    search_form = st.form("search_form")
    product_name = search_form.text_input('Search product:', 'Milk tea')
    search_submit = search_form.form_submit_button(label="Submit")

    if search_submit:
        results = get_similar_products(product_name, st.session_state.llm, st.session_state.chroma_client, 5)
        st.write(results)

if __name__ == "__main__":
    main()
