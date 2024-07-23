import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
from openai import OpenAI
client = OpenAI()

import chromadb
#Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="data/chroma_storage")
collection = chroma_client.get_collection(name="product_embeddings")


st.title("Similar Products") # Rename the title
search_form = st.form("search_form")
product_name = search_form.text_input('Search product:', 'Milk tea')
submitted = search_form.form_submit_button(label="Submit")


def similar_recommendation(product_name, top_n=3):
    # Get embedding for the input description
    response = client.embeddings.create(input=product_name, model='text-embedding-3-small')
    input_embedding = response.data[0].embedding

    # Query ChromaDB for similar embeddings
    results = collection.query(query_embeddings=input_embedding, n_results=top_n)

    # Extract and return recommended products
    recommendations = []
    metadatas = results['metadatas']

    product_names = [item['product_name'] for sublist in metadatas for item in sublist]

    for product_name in product_names:
        recommendations.append({'product_name': product_name})

    return recommendations




if submitted:
    a = similar_recommendation(product_name)
    st.write(a)





