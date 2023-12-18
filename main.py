from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Logic_init import model,load, df, arts_descriptions
#from Logic_init import model, df, arts_descriptions
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

    # most_similar_descriptions = w2v.find_most_similar_text(model= model, query='impressionism',texts = ['man in black', 'starry night'], top_k = 1)
   

    most_similar_descriptions = w2v.find_most_similar_text(model= model, query=q,texts = arts_descriptions, top_k = 3)
    print(most_similar_descriptions)
    most_similar_arts = df[df['feature_joined_text'].isin(most_similar_descriptions)]

    # df[df['feature_joined_text'] in most_similar_descriptions]

    

    # получение ИД
    # из файла достать 3 объекта
    # достать картинку из поисковика
    # вернуть в согласованном формате на фронт

    # return 3 suggestions
    most_similar_arts['release_date'] = most_similar_arts['release_date'].astype(str)
    data = most_similar_arts[['artwork_id','title', 'name', 'medium', 'classification', 'release_date']].to_dict('records')
    final=[]
    for object in data:
        load.run(object['name']+object['title'],object['artwork_id'])  # строка поиска картинки по сути название картины + автор
        object['link'] = './images/'+str(object['artwork_id'])+'.png'
        final.append(object)
    # dummy = {
    #     'id': '29296',
    #     'title': 'Picasso Dessins',
    #     'author': 'Pablo Picasso',
    #     'description': 'Monograph with reproductions and 1 lithograph (""Head of a Woman""; unbound frontispiece)',
    #     'type': 'Painting',
    #     'date': '1926',
    #     'link': 'images/29296.jpg'
    # }

    # data = [dummy, dummy, dummy]
    print()
    print()
    print()
    print()
    print(data)
    # data = []
    return data


app.mount("/", StaticFiles(directory="static", html=True), name="static")
