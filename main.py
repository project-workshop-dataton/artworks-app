from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Logic_init import model
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
    most_similar_descriptions = w2v.find_most_similar_text(model= model, query='impressionism',texts = ['man in black', 'starry night'], top_k = 1)
    print(most_similar_descriptions)
    #load.run("the manhattan transcripts project new york new york episode one the park bernard tschumi")  # строка поиска картинки по сути название картины + автор
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
