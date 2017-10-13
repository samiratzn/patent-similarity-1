#!/usr/bin/python  
# coding = UFT-8
pat_only_number_file = file("corpus/pat_only_number.txt", "r")  
pat_only_number_file.readline()
i = 0 
pat_only_number_map = {0:"0"};
for line in pat_only_number_file.readlines():
    pat_only_number_map[i] = line.strip()
    i = i + 1
print(pat_only_number_map)
pat_only_number_file.close()
pat_doc2vec_file = file("test/pat_doc2vec.txt", "r")  
pat_doc2vec_map = {0:0.0};
i = 0
for line in pat_doc2vec_file.readlines():
    pat_doc2vec_map[i] = float(line.split(",")[1])
    i = i + 1
pat_doc2vec_file.close()
print(pat_doc2vec_map)
sort_pat_doc2vec_map = sorted(pat_doc2vec_map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
print(sort_pat_doc2vec_map)
pat_doc2vec_result = file("result/pat_doc2vec_result.txt", "w")
for index in range(0, len(sort_pat_doc2vec_map)) :
    line = sort_pat_doc2vec_map[index][0]
    rank = sort_pat_doc2vec_map[index][1]
    number = pat_only_number_map.get(line)
    print "" + str(line) + "," + str(number) + "," + str(rank)
    if(index < 100):
        pat_doc2vec_result.write("" + str(line) + "," + str(number) + "," + str(rank) + "\n")
    if(index == 100):
        pat_doc2vec_result.close()
print "doc$"
