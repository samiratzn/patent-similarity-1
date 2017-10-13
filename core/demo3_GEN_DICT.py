#!/usr/bin/env Python
# coding=utf-8
import logging
from gensim import corpora
CORPUS_PATH = "corpus/pat_only_abstract.txt";
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f = open(CORPUS_PATH)
f.readline()
dictionary = corpora.Dictionary(line.lower().split() for line in f)
dictionary.save("dict/pat.dict")
f.close()
# remove stop words and words that appear only once
# stoplist = set('a the'.split())
# stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#             if stopword in dictionary.token2id]
# once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
# dictionary.filter_tokens(stop_ids)# + once_ids)  # remove stop words and words that appear only once
# dictionary.compactify()  # remove gaps in id sequence after words that were removed
# pprint(dictionary.token2id)
# 
# corpus = []
# f1 = open(CORPUS_PATH)
# f1.readline()
# for text in f1:
#     simtext = text.lower().split();
#     corpus.append(dictionary.doc2bow(simtext))
# f1.close()
# # print(corpus[0])
# # print(corpus[1])
# # print(corpus[2])
# 
# corpora.MmCorpus.serialize("dict/pat.mm", corpus)  # store to disk, for later use
print "DICT DONE$"