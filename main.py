from typing import Union
from urllib import response

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from gensim.models import KeyedVectors

import model_implementing.word2vec as w2v

app = FastAPI()


@app.get("/api")
def search(q: Union[str, None] = None):
    '''
    Формат сообщения - массив объектов:
    - title
    - author
    - description
    - type
    - date
    '''

    path_to_word_vectors = '~/Desktop/Projects/Data/GoogleNews/GoogleNews-vectors-negative300.bin.gz'
    model = KeyedVectors.load_word2vec_format(path_to_word_vectors, binary=True)
    
    most_similar_descriptions = w2v.find_most_similar_text(model= model, query='impressionism',texts = ['man in black', 'starry night'], top_k = 1)
    print(most_similar_descriptions)

    # получение ИД
    # из файла достать 3 объекта
    # достать картинку из поисковика
    # вернуть в согласованном формате на фронт

    # return 3 suggestions

    dummy = {
        'id': '29296',
        'title': 'Picasso Dessins',
        'author': 'Pablo Picasso',
        'description': 'Monograph with reproductions and 1 lithograph (""Head of a Woman""; unbound frontispiece)',
        'type': 'Painting',
        'date': '1926',
        'link': 'images/29296.jpg'
    }

    data = [dummy, dummy, dummy]
    # data = []

    return data


app.mount("/", StaticFiles(directory="static", html=True), name="static")
