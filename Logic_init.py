import os
import gdown
from gensim.models import KeyedVectors
import pandas as pd

os.makedirs(name='./data',exist_ok=True)
path_to_word_vectors = "./data/GoogleNews-vectors-negative300.bin.gz"
path_to_model = './data/arts_data_model_and_front.csv'

# проверяем, загружены ли файлы локально
if not os.path.exists(path_to_word_vectors):
    url = 'https://drive.google.com/uc?id=1TAkVgZNWVLvuEiUsEwn_oSbVLFrRfRVG'
    gdown.download(url, path_to_word_vectors, quiet=False)

if not os.path.exists(path_to_model):
    url = 'https://drive.google.com/uc?id=1cWYd9jYG9nGU0jDJDB3G6X6s-GyB2v_6'
    gdown.download(url, path_to_model, quiet=False)

# открываем базу данных объектов для поиска
df = pd.read_csv(path_to_model, dtype=str, keep_default_na=False)
arts_descriptions = df['feature_joined_text'].to_list()

# инициализируем модель
model = KeyedVectors.load_word2vec_format(path_to_word_vectors, binary=True)
