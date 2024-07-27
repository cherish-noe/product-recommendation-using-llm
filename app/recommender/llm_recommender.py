import json

def get_similar_products(product_name, llm_client, chroma_client, top_n=5):
    """
    Recommend similar products based on item name and descriptions.

    Args:
        product_name (str): Name of the product.
    
    Returns:
        list: List of similar recommended products.
    """
    # Get embedding for the input product
    response = llm_client.embeddings.create(input=product_name, model='text-embedding-3-small')
    input_embedding = response.data[0].embedding

    # Query ChromaDB for similar embeddings
    collection = chroma_client.get_collection(name="product_embeddings")
    results = collection.query(query_embeddings=input_embedding, n_results=top_n)

    # Extract and return recommeded products
    recommendations = []
    metadatas = results['metadatas']

    product_names = [item['product_name'] for sublist in metadatas for item in sublist]

    for product_name in product_names:
        recommendations.append({'product_name': product_name})

    return recommendations

def get_user_prompt(add_to_cart_products, top_n):
    products = ', '.join(add_to_cart_products)
    prompt = f"A user added the following products: {add_to_cart_products} to her shopping cart. \
        What next {top_n} items would she be likely to purchase next?"
    # prompt += "Express your response as a python list."
    prompt += " Express your response as a JSON object with a key of 'next_items' and \
        a value representing your array of recommended items."
    
    return prompt

def get_general_recommendations(add_to_cart_products, llm_client, chroma_client, top_n=5):
    """
    Recommend items based on the items added to the cart.

    Args:
        cart_items (list): List of the items currently in the cart.

    Returns:
        list: List of recommended items.
    """
    system_prompt = "You are an AI assistant functioning as a recommendation system for an ecommerce website. \
        Be specific and limit your answers to the requested format. Keep your answers short and concise."

    user_prompt = get_user_prompt(add_to_cart_products, top_n)

    response = llm_client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={ "type": "json_object" },
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        max_tokens=128
    )

    return response.choices[0].message.content


def get_cart_recommendations(add_to_cart_products, llm_client, chroma_client, top_n=10):

    general_products = get_general_recommendations(add_to_cart_products, llm_client, chroma_client, top_n=5)
    product_dict = json.loads(general_products)
    product_list = product_dict["next_items"]
    print(len(product_list))
    print(product_list)
    print(type(product_list))
    if len(product_list) > 0:
        n_result = round(top_n/len(product_list))
        print(n_result)
        recommendations = []
        for product in product_list:
            # Get embedding for the input product
            response = llm_client.embeddings.create(input=product, model='text-embedding-3-small')
            input_embedding = response.data[0].embedding

            # Query ChromaDB for similar embeddings
            collection = chroma_client.get_collection(name="product_embeddings")
            results = collection.query(query_embeddings=input_embedding, n_results=n_result)

            metadatas = results['metadatas']

            product_names = [item['product_name'] for sublist in metadatas for item in sublist]

            for product_name in product_names:
                recommendations.append([product_name])

        return recommendations
    else:
        return None


