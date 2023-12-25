import os
import time
import json
from typing import Union
#from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from ImageLoader import newrun
from Logic_init import model, df, arts_descriptions 
import model_implementing.word2vec as w2v
from mysql_connector import add_data,get_data,add_data_V2,get_data_V2
import nest_asyncio
# создание приложения
app = FastAPI()
import asyncio
nest_asyncio.apply()
import pymysql

def write_json(new_data, filename='data/metric.json'):
    if not os.path.isfile(filename):
        with open(filename, 'w+') as file:
            file.write("{}")
            file.close()
    with open(filename, 'r+') as file:
        file_data = list(json.load(file))
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()

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
    #print(df['feature_joined_text'][85287])
    most_similar_descriptions, cosine_distances = w2v.find_most_similar_text(model=model, query=q, texts=arts_descriptions, top_k=3)
    
    describtions_cosine_distances = dict(zip(most_similar_descriptions, cosine_distances))
    write_json({'query': q, 'output': describtions_cosine_distances})

    most_similar_arts = df[df['feature_joined_text'].isin(
        most_similar_descriptions)]

    # return 3 suggestions
    data = most_similar_arts[['title','artwork_id', 'name','medium', 'classification']].to_dict('records')
    temp=[]
    temp_names = {}
    for object in data:
        id=str(object['artwork_id'])
        if not os.path.isfile('./static/images/'+id+'.png'):
            temp.append(id)
            temp_names[str(id)]= object['name'] +" "+ object['title']
            print("Вызов")
        object['link'] = './images/'+id+'.png'
        #object['link'] = './images/dummy.png'
        #print(object)
    if len(temp) !=0:
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(newrun(temp,temp_names))
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
    add_data_V2(fb['q'],fb['id'],fb['feedback'])
# подключаем статические файлы сайта, включая веб-приложение
app.mount("/", StaticFiles(directory="static", html=True), name="static")
