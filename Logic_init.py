from gensim.models import KeyedVectors
from ImageLoader import ImageLoader
import platform, os
import pandas as pd
load = ImageLoader() #создание объекта load
import gdown
import os
path_to_word_vectors = "./data/GoogleNews-vectors-negative300.bin.gz"
path_to_model = './data/arts_data_model_and_front.csv'
if not os.path.exists(path_to_word_vectors):
    url = 'https://drive.google.com/uc?id=1TAkVgZNWVLvuEiUsEwn_oSbVLFrRfRVG'
    gdown.download(url, path_to_word_vectors, quiet=False)
if not os.path.exists(path_to_model):
    url = 'https://drive.google.com/uc?id=1cWYd9jYG9nGU0jDJDB3G6X6s-GyB2v_6'
    gdown.download(url, path_to_word_vectors, quiet=False)
df = pd.read_csv('./data/arts_data_model_and_front.csv')
model = KeyedVectors.load_word2vec_format(path_to_word_vectors, binary=True, )

arts_descriptions = df['feature_joined_text'].to_list()