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
    lda_model = models.LdaModel.load("model/pat_lda.model")
    print "TF/IDF MODEL & LDA MODEL TO INDEX MODEL BEGIN TRAIN"
    corpus_tfidf = tfidf_model[corpus]
    corpus_lda   = lda_model[corpus_tfidf]
    index = Similarity("index_lda/sim.index",corpus_lda,num_features=10, shardsize=327680) # build the index
    print "TRAIN DONE"
else:
    print("Please run to generate LDA data set")