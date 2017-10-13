#coding:utf-8
import os
from gensim import corpora, models
import logging
from gensim.similarities.docsim import Similarity

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

DICT_PATH = "dict/pat.dict"
CORPUS_PATH = "dict/pat.mm"
if (os.path.exists(DICT_PATH)):
    dictionary = corpora.Dictionary.load(DICT_PATH)
    corpus = corpora.MmCorpus(CORPUS_PATH)
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")
if (os.path.exists("model/pat_tfidf.model")):
    tfidf_model = models.TfidfModel.load("model/pat_tfidf.model")
    corpus_tfidf = tfidf_model[corpus]
    index = Similarity( "index/sim.index",corpus_tfidf,num_features=len(dictionary), shardsize=327680) # build the index
else:
    print("Please run to generate tfidf data set")