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
    lsi_model = models.LsiModel.load("model/pat_lsi.model")
    print "TF/IDF MODEL & LSI MODEL TO INDEX MODEL BEGIN TRAIN"
    corpus_tfidf = tfidf_model[corpus]
    corpus_lsi   = lsi_model[corpus_tfidf]
    index = Similarity("index_lsi/sim.index",corpus_lsi,num_features=10, shardsize=327680) # build the index
    print "TRAIN DONE"
else:
    print("Please run to generate LSI data set")