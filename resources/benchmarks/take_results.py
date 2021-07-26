#!/usr/bin/env python3.7
import sys
import statistics as sts

def read_result(fileName):
    stringa = sys.argv[2]
    resultList=[] 
    with open(fileName, 'r') as f:
        for line in f:
            if "Dataset name" in line:
                print(line)
            if stringa in line:
                print(line)
            if "|S|" in line:
                print(f"Size: {line}")
                print("------------------------")
    return resultList

#arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
#for element in arr_txt:
    #values = read_result(element)

read_result(sys.argv[1])