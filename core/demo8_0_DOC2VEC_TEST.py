#coding:utf-8
import gensim
import logging

abstract9754858  ="Provided is a gas sensor package, including: a gas sensing element; and a substrate on which the gas sensing element is disposed, in which a through hole corresponding to the gas sensing element is formed."
abstract9755578 ="Current-mode control for radio-frequency (RF) power amplifiers. In some embodiments, an RF power amplifier control circuit can include a sensor configured to measure a base current of a power amplifier and generate a sensed current. The control circuit can further include a sensing node configured to receive a reference current and perform a current-mode operation with the sensed current to yield an error current. The control circuit can further include a control loop configured to generate a control signal based on the error current to adjust an operating parameter of the power amplifier."
abstract9754435 ="A device for the insertion of banknotes into containers in machines suitable for receiving and handling banknotes, comprises a container for the banknotes, adapted to be closed and removed from the machine once filled, and a loading path, diverting from a circulation path inside the machine and ending at said container, for the insertion of banknotes into the container. The device further comprises at least one scanner, placed along the loading path, for the optical detection of images of the banknotes entering into the container and a memory connected to the scanner for storing the images detected thereby."

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = gensim.models.doc2vec.Doc2Vec.load("D:/model/pat_doc2vec.model")
inferred_vector = list(abstract9754858.lower().split())
doc_inferred_vec=model.infer_vector(inferred_vector)
sims = model.docvecs.most_similar([doc_inferred_vec], topn=len(model.docvecs))
for i in range(0,100):
    print str(i) + " => "+str(sims[i][0])+ "," + str(sims[i][1])
print "DOC2VEC$"

file_object = open('result_abstract9754858/pat_doc2vec_100.csv', 'w')
for i in range(0,100):
    print str(sims[i][0])+ "," + str(sims[i][1])
    file_object.write(str(sims[i][0])+ "," + str(sims[i][1])+ "\n") 
file_object.close()
print "DOC2VECT WRITE DONE"