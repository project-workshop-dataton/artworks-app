from gensim.models import KeyedVectors
# from ImageLoader import ImageLoader
import platform, os
import pandas as pd
# load = ImageLoader() #создание объекта load
import gdown
import os
path_to_word_vectors ="./data/GoogleNews-vectors-negative300.bin.gz"
if not os.path.exists(path_to_word_vectors):
    url = 'https://drive.google.com/uc?id=1TAkVgZNWVLvuEiUsEwn_oSbVLFrRfRVG'
    gdown.download(url, path_to_word_vectors, quiet=False)
model = KeyedVectors.load_word2vec_format(path_to_word_vectors, binary=True, )
df = pd.read_csv('~/Desktop/Projects/Data/arts_data_model_and_front.csv')
arts_descriptions = df['feature_joined_text'].to_list()