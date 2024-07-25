import streamlit as st
from app.utils.resources import init_resources
from app.recommender.llm_recommender import get_cart_recommendations

# Initialize the resources
init_resources()

def main():
    result = get_cart_recommendations(
        st.session_state.add_to_cart_products,
        st.session_state.llm,
        st.session_state.chroma_client,
        5)
    st.write(result)

if __name__ == "__main__":
    main()