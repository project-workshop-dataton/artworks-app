from gensim.models import KeyedVectors
# from ImageLoader import ImageLoader
import platform, os
import pandas as pd
# load = ImageLoader() #создание объекта load
if platform.system() == "Windows":
    path_to_word_vectors = os.environ['vector']
else:
    path_to_word_vectors = '~/Desktop/Projects/Data/GoogleNews/GoogleNews-vectors-negative300.bin.gz'
model = KeyedVectors.load_word2vec_format(path_to_word_vectors, binary=True, )

df = pd.read_csv('~/Desktop/Projects/Data/arts_data_model_and_front.csv')
arts_descriptions = df['feature_joined_text'].to_list()