import os
import streamlit as st
from app.utils.resources import init_resources
from app.utils.ui_components import sidebar_menu, load_css


# Set Page Title
st.set_page_config(
    page_title="Setting"
)
# Initialize resources
init_resources()
# Sidebar Menu
sidebar_menu()
# CSS
load_css()

def main():
    st.subheader("API Configuration")
    st.markdown("""
    <div class='header_desc'>
    Pleae provide your OpenAI API key to continue using the app:
    </div>
    <br>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        openai_api_key = st.text_input(label="OpenAI API key")
    
    submit = st.button('Submit', key='set-api-key')
    if submit:
        with open('.env', 'w') as file:
            file.write(f"OPENAI_API_KEY={openai_api_key}\n")


if __name__ == "__main__":
    main()

