#coding:utf-8
import os
from gensim import corpora
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
DICT_PATH = "dict/pat.dict"
CORPUS_PATH = "corpus/pat_only_abstract.txt";
if (os.path.exists(DICT_PATH)):
    dictionary = corpora.Dictionary.load(DICT_PATH)
    print("Used files generated")
else:
    print("Please GEN DICT FIRST")

corpus = []
f1 = open(CORPUS_PATH)
f1.readline()
i = 0
for text in f1:
    simtext = text.lower().split();
    a = dictionary.doc2bow(simtext)
    corpus.append(a)
    i = i + 1
    if(i%100000==0):
        print str(i) + ":完成100000批次：" + str(a) 
corpora.MmCorpus.serialize("dict/pat.mm", corpus)
f1.close()
    # print(corpus[0])
    # print(corpus[1])
    # print(corpus[2])
    
  # store to disk, for later use