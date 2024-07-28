import streamlit as st
from app.utils.resources import init_resources
from app.utils.ui_components import sidebar_menu, load_css
from app.recommender.llm_recommender import get_similar_products

# Set Page Title
st.set_page_config(
    page_title="Home Page",
    layout="wide"
)
# Initialize the resources
init_resources()
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

def main():
    st.title("Welcome to :rainbow[...]")
    st.html(
    """
    <p style='font-size:29px; color: #dae3e5;'>Product Recommendations using
    <span style='font-size:40px; color: #64b5f6;  font-weight: bold;'>LLM</span>
    </p><hr>"""
    )
    col1, col2, col3 = st.columns([0.35, 0.05, 0.6])
    with col1:
        st.subheader(":grey[About the Project]")
        st.markdown("""
        This :blue-background[&nbsp;POC&nbsp;] project leverages **LLMs** to provide product recommendations.
        It analyzes the items added to your cart and suggests additional products you might be intersted in.
        """)
        st.markdown("""
        Plus, when you search for a product, it displays and recommends products similar to your search query.
        """)
        st.subheader(":grey[Technologies Used]")
        st.markdown("""
        - **Vector Database**
        """)
    with col2:
        st.write("")
    with col3:
        st.subheader(":grey[How to Use This App]")
        st.markdown("Follow the steps below to get the best out of LLM recommendations.")
        st.markdown("""
        1. 🏠 **Home Page** (Current Page):  
        Here, you'll find information about the project, and how to use the app.
        """)
        st.markdown("""
        2. **Add To Cart**:  
        Start by exploring the products and adding your desired items to the cart. Once you've made your selection, click 'View Cart' button to review and get recommendations.
        """)
        st.markdown("""
        3. **Cart Recommendations**:  
        This page lists all the items you've added to your cart and provides recommendations on what you should consider buying next.
        """)
    



if __name__ == "__main__":
    main()
