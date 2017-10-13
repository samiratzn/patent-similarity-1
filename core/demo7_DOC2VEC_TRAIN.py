#coding:utf-8
import multiprocessing
import gensim
import smart_open
import logging
# from nltk.parse.featurechart import sent
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
cores = multiprocessing.cpu_count()
train_file ="corpus/pat_only_abstract.txt"
# lee_test_file = 'csv_pat_abstract_test.txt'
 
def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="utf-8") as f:
        f.readline()
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])
 
train_corpus = list(read_corpus(train_file))
# test_corpus = list(read_corpus(lee_test_file))

model = gensim.models.doc2vec.Doc2Vec(size=1000, min_count=2, iter=100,workers=cores)
model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.iter)
model.save("model/pat_doc2vec.model")
print "DOC2VEC$"