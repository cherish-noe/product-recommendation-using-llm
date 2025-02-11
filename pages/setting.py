import os
import streamlit as st
from app.utils.resources import init_resources
from app.utils.ui_components import sidebar_menu, load_css, custom_button


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
    # st.header("API Configuration")
    st.markdown("""
    <h1 style='text-align: left; color: #f8f4f1;'>API Configuration</h1>
    <div class='header_desc'>
    <p style= 'text-align: left;'>Pleae provide your OpenAI API key to continue using the app:</p>
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        openai_api_key = st.text_input(label="OpenAI API key", key='api_key')

    agree = st.checkbox('I acknowledge that adding the value will overwrite the existing key.')
    if agree:
        submit = st.button('&nbsp;&nbsp;Submit&nbsp;&nbsp;', key='set-api-key')
        if submit:
            with open('.env', 'w') as file:
                file.write(f"OPENAI_API_KEY={openai_api_key}\n")
            st.success('Success!', icon='✅')
    else:
        submit = st.button('&nbsp;&nbsp;Submit&nbsp;&nbsp;', key='set-api-key', disabled=True)


if __name__ == "__main__":
    main()

