import streamlit as st

def sidebar_menu():
    st.sidebar.page_link("pages/add_to_cart.py", label=":blue[＋] &nbsp; **ADD TO CART**")
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Recommend
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.page_link("pages/view_cart.py", label=":grey[🛒] &nbsp; Cart Recommendations") 
    st.sidebar.page_link("main.py", label=":grey[≈≈] &nbsp; Similar Products")
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Product
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    
    st.sidebar.page_link("pages/product_catalog.py", label=":grey[⌘] &nbsp; Product Catalog")
    st.sidebar.markdown("""
                        <div style='font-size: 18px; color: #6c757d; margin-top: 7px; margin-bottom:-25px;'>
                            &nbsp; Setting
                        </div>
                        """,
                        unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.page_link("pages/setting.py", label=":violet[⚙️] &nbsp; API Configuration")

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
