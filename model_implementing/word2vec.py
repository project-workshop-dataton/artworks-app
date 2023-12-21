import gensim
import numpy as np
import pandas as pd

def count_bag_of_words(model: gensim.models.keyedvectors.KeyedVectors, text: str) -> np.ndarray:
    words = text.split(' ')
    text_vector = np.zeros(model.vector_size)
    indexed_words_quantity = 0
    for word in words:
        if model.has_index_for(word):
            indexed_words_quantity += 1
            text_vector += model[word]
    if indexed_words_quantity != 0:
        text_vector /= indexed_words_quantity

    return text_vector

def find_most_similar_text(model: gensim.models.keyedvectors.KeyedVectors, query: str, texts: list[str], top_k: int) -> list[str]:
    '''

    Args:
        model (gensim.models.keyedvectors.KeyedVectors): Word vectors
        query (str): User query
        texts (list[str]): list of arts descriptions
        top_k (int): Hom many arts you want

    Returns:
        list[str]: List of most similar descriptions
    '''

    query_vector = count_bag_of_words(model=model, text=query)
    texts_vectors = pd.DataFrame({'text': texts, 
                                  'text_vector': list(map(lambda text: count_bag_of_words(model=model, text=text), texts))})
    texts_vectors['query_distance'] = list(model.cosine_similarities(query_vector, list(texts_vectors['text_vector'])))
    return texts_vectors.nlargest(n = top_k, columns='query_distance')['text'].to_list()
