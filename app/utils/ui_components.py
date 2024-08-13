import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def sidebar_menu():
    st.sidebar.image("img/logo.png")
    # st.sidebar.text("")
    # st.sidebar.subheader("Product Recommendation using LLM", divider="grey")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.page_link("main.py", label=":blue[🏠] &nbsp; **HOME**")
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Cart
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.page_link("pages/add_to_cart.py", label=":grey[＋] &nbsp; Add To Cart") 
    st.sidebar.page_link("pages/view_cart.py", label=":grey[🛒] &nbsp; Cart Recommendations") 
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Search
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.page_link("pages/product_catalog.py", label=":grey[⌘] &nbsp; Product Catalog")
    st.sidebar.page_link("pages/search_similarity.py", label=":grey[≈≈] &nbsp; Similar Products")
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Setting
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.page_link("pages/setting.py", label=":violet[⚙️] &nbsp; API Configuration")

def custom_button(button_label, key):
    with stylable_container(
                key=key,
                css_styles="""
                    button {
                        background-color: #002855;
                        color: white;
                        font-weight: bold;
                        border-radius: 10px;
                    }
                """,
        ):
        submit = st.button(button_label)
    return submit

def load_css():
    css_code = """
    <style>
    .header_desc {
        font-size: 18px; 
        color: #b5b7ba;
    }
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)
