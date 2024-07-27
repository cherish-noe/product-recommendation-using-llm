import streamlit as st

st.text_input('Name', key='aa')

def set_name(ss):
    st.session_state.aa = ss

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])