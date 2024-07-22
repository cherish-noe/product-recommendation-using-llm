import streamlit as st

search_form = st.form("search_form")
product_search = search_form.text_input('Search product:', 'Milk tea')
submit = search_form.form_submit_button("Submit")



