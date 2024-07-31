import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import chromadb


def init_resources():
    load_dotenv()

    if "llm" not in st.session_state:
        llm = OpenAI() #api_key=os.environ.get('OPENAI_API_KEY')
        st.session_state['llm'] = llm

    if "chorma_client" not in st.session_state:
        chroma_client = chromadb.PersistentClient(path="app/data/chroma_storage")
        st.session_state['chroma_client'] = chroma_client
