#coding:utf-8
import logging

abstract9754858  ="Provided is a gas sensor package, including: a gas sensing element; and a substrate on which the gas sensing element is disposed, in which a through hole corresponding to the gas sensing element is formed."
abstract9755578 ="Current-mode control for radio-frequency (RF) power amplifiers. In some embodiments, an RF power amplifier control circuit can include a sensor configured to measure a base current of a power amplifier and generate a sensed current. The control circuit can further include a sensing node configured to receive a reference current and perform a current-mode operation with the sensed current to yield an error current. The control circuit can further include a control loop configured to generate a control signal based on the error current to adjust an operating parameter of the power amplifier."
abstract9754435 ="A device for the insertion of banknotes into containers in machines suitable for receiving and handling banknotes, comprises a container for the banknotes, adapted to be closed and removed from the machine once filled, and a loading path, diverting from a circulation path inside the machine and ending at said container, for the insertion of banknotes into the container. The device further comprises at least one scanner, placed along the loading path, for the optical detection of images of the banknotes entering into the container and a memory connected to the scanner for storing the images detected thereby."

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

pat_only_number_file = file("corpus/pat_only_number.txt", "r")  
# pat_only_number_file.readline()
i = 0 
pat_only_number_map = {0:"0"};
for line in pat_only_number_file.readlines():
    i = i + 1
    pat_only_number_map[i] = line.strip()
print "LOAD PAT NUMBER DONE"
pat_only_number_file.close()
print pat_only_number_map[0]
print pat_only_number_map[1]
pat_doc2vec_file = file("abstract9754858/pat_doc2vec.txt", "r")  
pat_doc2vec_map = {0:0};
pat_doc2vec_rank_map = {0:0.0};
i = 0
for line in pat_doc2vec_file.readlines():
    pat_doc2vec_map[i] = line.split(",")[0]
    pat_doc2vec_rank_map[i] = line.split(",")[1]
    i = i + 1
pat_doc2vec_file.close()
print pat_doc2vec_map[0]
print pat_doc2vec_rank_map[0]
pat_doc2vec_result = file("result_abstract9754858/pat_doc2vec_result.txt", "w")
for index in range(0, len(pat_doc2vec_map)) :
    line = pat_doc2vec_map[index]
    rank = pat_doc2vec_rank_map[index]
    number = pat_only_number_map[int(line)+1]
    print "" + str(line) + "," + str(number) + "," + str(rank)
    pat_doc2vec_result.write("" + str(line) + "," + str(number) + "," + (str(rank)).strip()+ "\n")
pat_doc2vec_result.close()
print "RANK DONE"
