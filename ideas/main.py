import json
import numpy as np
import tensorflow as tf
import time
from jsonHelpers import cleanUpDataset
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
import nltk
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize 
nltk.download('punkt')

start_time = time.time()
cleanUpDataset("data", "Electronics_5.json", 500)
print("%s data read time seconds" % (time.time() - start_time))

reviewDict = {}

with open("./cleanData/Electronics_5.json") as jsonfile:
    reviewDict = json.load(jsonfile)

data = []

for review in reviewDict['reviews']:
    reviewItem = sent_tokenize(review['reviewText'])
    for word in reviewItem:
        data.append(word_tokenize(word))

model = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5, sg = 1) 

print("Similarity", model.similarity('gps', 'bedframe')) 