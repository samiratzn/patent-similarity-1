#coding:utf-8
import os
from gensim import corpora, models
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
DICT_PATH = "dict/pat.dict"
CORPUS_PATH = "dict/pat.mm"
if (os.path.exists(DICT_PATH)):
    dictionary = corpora.Dictionary.load(DICT_PATH)
    corpus = corpora.MmCorpus(CORPUS_PATH)
    print("Used files generated")
else:
    print("Please GEN DICT FIRST")

#PrintDictionary(dictionary)
print "TF/IDF/BEGIN"
tfidf_model = models.TfidfModel(corpus) 
tfidf_m = tfidf_model[corpus]
tfidf_model.save("model/pat_tfidf.model")
print "TF/IDF/END"

print "LSI/BEGIN"
lsi_model = models.LsiModel(tfidf_m, id2word=dictionary, num_topics=10)
lsi_model.save("model/pat_lsi.model")
print "LSI/END"

# ## LDA模型 **************************************************
print "LDA/BEGIN"
lda_model = models.LdaModel(tfidf_m, id2word=dictionary, num_topics=10)
lda_model.save("model/pat_lda.model")
print "LDA/END"