#!/bin/bash

for f in *.txt
do
    ./take_results.py $f >> result.$f
done