# coding:utf-8
import os
from gensim import corpora, models, similarities, utils
import logging
from gensim.similarities.docsim import Similarity
from gensim.corpora.sharded_corpus import ShardedCorpus
from pprint import pprint

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

abstract9754858 = "Provided is a gas sensor package, including: a gas sensing element; and a substrate on which the gas sensing element is disposed, in which a through hole corresponding to the gas sensing element is formed."
abstract9755578 = "Current-mode control for radio-frequency (RF) power amplifiers. In some embodiments, an RF power amplifier control circuit can include a sensor configured to measure a base current of a power amplifier and generate a sensed current. The control circuit can further include a sensing node configured to receive a reference current and perform a current-mode operation with the sensed current to yield an error current. The control circuit can further include a control loop configured to generate a control signal based on the error current to adjust an operating parameter of the power amplifier."
abstract9754435 = "A device for the insertion of banknotes into containers in machines suitable for receiving and handling banknotes, comprises a container for the banknotes, adapted to be closed and removed from the machine once filled, and a loading path, diverting from a circulation path inside the machine and ending at said container, for the insertion of banknotes into the container. The device further comprises at least one scanner, placed along the loading path, for the optical detection of images of the banknotes entering into the container and a memory connected to the scanner for storing the images detected thereby."

# sent = "A napkin holder formed of two pairs of magnetic securing devices attached in a laterally movable arrangement with respect to each other on the outer ends of a partially neck encircling lanyard. The magnetic securing devices are formed of plastic tabs movable laterally with respect to each other"

DICT_PATH = "dict/pat.dict"
CORPUS_PATH = "dict/pat.mm"
if (os.path.exists(DICT_PATH)):
    dictionary = corpora.Dictionary.load(DICT_PATH)
    corpus = corpora.MmCorpus(CORPUS_PATH)
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")
# sent = "A motor vehicle door hinge with a hinge axis includes a first hinge part and a second hinge part. The first hinge part has a first arm and a second arm axially spaced from the first arm with the hinge axis passing through the first arm and the second arm. The second hinge part includes a continuous strip of material having a first end"
if (os.path.exists("model/pat_tfidf.model")):
    tfidf_model = models.TfidfModel.load("model/pat_tfidf.model")
    lsi_model = models.LsiModel.load("model/pat_lsi.model")

#     corpus_lsi_simi_matrix = similarities.MatrixSimilarity(lsi_model[corpus_tfidf])
    print "LSI MODEL BEGIN LOAD"
#     print index
    compare_file = "abstract9755578/pat_lsi2vec.txt"
    if (os.path.exists(compare_file)):
        raise Exception("Please delete compare_file first") 
    lsiwriter = open(compare_file, "a")
    file_index = 0
    current = 0
    for file_index in range (0, 100):
        index_file = "index_lsi/sim.index." + str(file_index)
        if(os.path.exists(index_file)):
            index = Similarity.load(index_file)
            print index
            print " SIMS BEGIN COMPARE: Index" + str(file_index)
            inferred_vector = dictionary.doc2bow(abstract9755578.lower().split())
            print inferred_vector
            inferred_vector_tfidf = tfidf_model[inferred_vector]
            print inferred_vector_tfidf
            inferred_vector_lsi = lsi_model[inferred_vector_tfidf]
            print inferred_vector_lsi
            test_lsi_simi = index[inferred_vector_lsi]
            length = len(list(test_lsi_simi))
            print length
            for i in range (0, length):
                rank = list(test_lsi_simi)[i];
                line = i + current
                content = str(line) + "," + str(rank) 
                if(i%10000 == 0):
                    print "Document: " + str(line)
                    print "Content: " + content 
                lsiwriter.write(content + "\n")
                i = i + 1
            print("LSI END")
            current = current + length
        else:
            print "Compare end"
        file_index = file_index + 1
    lsiwriter.close()
    print "TEST DONE"
else:
    print("Please run to generate lsi data set")

