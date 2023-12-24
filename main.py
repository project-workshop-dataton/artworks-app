import os
from typing import Union
#from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from ImageLoader import newrun
from Logic_init import model, df, arts_descriptions 
import model_implementing.word2vec as w2v
from pprint import pprint
import asyncio

# создание приложения
app = FastAPI()

from pprint import pprint

#from bs4 import BeautifulSoup
import asyncio
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor

from requests_html import AsyncHTMLSession, HTML



# обработчик поискового запроса
@app.get("/api")
async def search(q: Union[str, None] = None):
    '''
    Формат сообщения - массив объектов:
    - artwork_id - ид объекта в базе
    - pub_title - название
    - name - имя автора
    - medium - описание объекта
    - classification - тип прозведения исскуства
    - pub_year - год создания
    - link - ссылка на иллюстрация
    '''

    most_similar_descriptions = w2v.find_most_similar_text(
        model=model, query=q, texts=arts_descriptions, top_k=3)  # type: ignore

    most_similar_arts = df[df['feature_joined_text'].isin(
        most_similar_descriptions)]

    # return 3 suggestions
    data = most_similar_arts[['artwork_id', 'name','medium', 'classification']].to_dict('records')
    temp=[]
    for object in data:
        id=str(object['artwork_id'])
        if not os.path.isfile('./static/images/'+id+'.png'):
            temp.append(id)
            print("Вызов")
        #object['link'] = '.images/'+id+'.png'
        object['link'] = './images/dummy.png'
        #print(object)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(newrun(temp))
    loop.run_until_complete(future)

        # строка поиска картинки по сути название картины + автор
        # load.newrun(object['title'], object['artwork_id'])
        # object['link'] = './images/'+str(object['artwork_id'])+'.png'
        # final.append(object)
    # Объект заглушка для мок-тестирования
    # dummy = {'artwork_id': '46333',
    #          'classification': 'Photograph',
    #          'link': './images/dummy.png',
    #          'medium': 'Chromogenic color print. Chromogenic color print. Chromogenic color print. Chromogenic color print.Chromogenic color print.',
    #          'name': 'Stuart Klipper',
    #          'pub_title': 'FOG AND ICE BLINK',
    #          'pub_year': '1981'}
    # pprint(data)


    return data


# сбор обратной связи по качеству ответа
@app.post("/api/feedback")
async def feedback(request: Request):
    fb = await request.json()
    print(fb)


# подключаем статические файла сайта, включая веб-приложение
app.mount("/", StaticFiles(directory="static", html=True), name="static")
