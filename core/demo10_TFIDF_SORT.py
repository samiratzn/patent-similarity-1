#coding=utf-8  
#-*- coding: UTF-8
import os
# sort_folder = "abstract9755578"
#sort_folder = "abstract9754435"
sort_folder = "abstract9754858"
pat_only_number_file = file("corpus/pat_only_number.txt", "r")  
i = 0 
pat_only_number_file.readline()
pat_only_number_map = {0:"0"};
for line in pat_only_number_file.readlines():
    i = i + 1
    pat_only_number_map[i] = line.strip()
# print(pat_only_number_map)
print("LOAD PAT NUMBER")
pat_only_number_file.close()
pat_tfidf2vec_file = file(sort_folder+"/pat_tfidf2vec.txt", "r")  
pat_tfidf2vec_map = {0:0.0};
i = 0
for line in pat_tfidf2vec_file.readlines():
    i = i + 1
    pat_tfidf2vec_map[i] = float(line.split(",")[1])
pat_tfidf2vec_file.close()
# print(pat_tfidf2vec_map)
print("LOAD PAT TF/IDF NUMBER")
sort_pat_tfidf2vec_map = sorted(pat_tfidf2vec_map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
# print(sort_pat_tfidf2vec_map)
print sort_pat_tfidf2vec_map[0]
print("LOAD PAT TF/IDF SORT NUMBER")
foldresult = "result_"+sort_folder
if (not os.path.exists(foldresult)):
    print foldresult + " not exist"
pat_tfidf2vec_result = file(foldresult + "/pat_tfidf2vec_result_100.csv", "w")
for index in range(0, len(sort_pat_tfidf2vec_map)) :
    line = sort_pat_tfidf2vec_map[index][0]
    rank = sort_pat_tfidf2vec_map[index][1]
    number = pat_only_number_map.get(int(line)-1)
#     print "" + str(index) + "," + str(number) + "," + str(rank)
    if(index < 100):
        pat_tfidf2vec_result.write("" + str(index) + "," + str(number) + "," + str(rank) + "\n")
    if(index == 100):
        pat_tfidf2vec_result.close()
        print "TF/IDF DONE：" + foldresult
        raise  Exception("Done TOP 100")
print "TF/IDF$"
