#!/bin/bash

FILES="resources/dataset/*"
count=1

for f in $FILES
do
    if [ "$FILES" != "normalized.txt" ]; then
        if [[ $FILES != *".pdf"* ]]; then
            echo "sto elaborando ---> $f"
            python3.7 targetsetselection.py -d $f >> resources/benchmarks/benchmark_$count.txt
            count=$((count+1))
        fi
    fi
done