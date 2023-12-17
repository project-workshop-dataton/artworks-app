from typing import Union
from urllib import response

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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
