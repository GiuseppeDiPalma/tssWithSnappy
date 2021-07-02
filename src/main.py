from optparse import OptionParser
from typing import *
import random as rnd
from icecream import ic
from time import time

from .wrapper import *

DECIMALNUMBER = 4

def main():
    rnd.seed(1234)

    parser = OptionParser("\n\t python %prog -d [dataset_name]")

    parser.add_option("-d", dest="dataset",
                   help="Filename of dataset", metavar="string")


    (options, args) = parser.parse_args()

    if not options.dataset:
        parser.error("You must pass a dataset!")

    edge_p_functions = [
        p_edge_uniform, p_edge_neighborhood_biased, p_edge_neighborhood_biased_reverse
        ]

    degree_coefficients = [(1,2),(1,3),(2,3)]
    constants = [2,4,6]
    print(f"Dataset name = {options.dataset}")

    for edge_function in edge_p_functions:
        # Degree based
        for coefficients in degree_coefficients:
            print("for coefficients in degree_coefficients:")

            startL = time()
            graph = load_graph(options.dataset)
            print(f"load_graph - Elapsed time: {round(time()-startL, DECIMALNUMBER)}")

            startS = time()
            subgraph(graph, edge_function)
            print(f"subgraph - Elapsed time: {round(time()-startS, DECIMALNUMBER)}")

            print(f"Graph size: |N| = {graph.GetNodes()} - |E| = {graph.GetEdges()}")
            print(f"Degree based with coefficients |a|={coefficients[0]} - |b|={coefficients[1]}")

            startT = time()
            threshold_array = initialize_threshold(graph, tf_degree_based, coefficients[0], coefficients[1])
            print(f"initialize_threshold - Elapsed time: {round(time()-startT, DECIMALNUMBER)}")

            ic.disable()

            startTSS = time()
            S = TSS(graph, threshold_array)
            print(f"TSS - Elapsed time: {time()-startTSS}")

            ic.enable()
            #print(f"Solution TSS = {S}")
            #print(f"Solution Size = {len(S)}")
            #ic(S)

        # Constants
        for value in constants:
            print("for value in constants:")

            startL = time()
            graph = load_graph(options.dataset)
            print(f"load_graph - Elapsed time: {round(time()-startL, DECIMALNUMBER)}")

            startS = time()
            subgraph(graph, edge_function)
            print(f"subgraph - Elapsed time: {round(time()-startS, DECIMALNUMBER)}")

            print(f"Graph size: |N| = {graph.GetNodes()} - |E| = {graph.GetEdges()} - Constant value: {value} \n")

            startT = time()
            threshold_array = initialize_threshold(graph, tf_constant, value)
            print(f"initialize_threshold - Elapsed time: {round(time()-startT, DECIMALNUMBER)}")

            ic.disable()

            startTSS = time()
            S = TSS(graph, threshold_array)
            print(f"TSS - Elapsed time: {time()-startTSS}")

            ic.enable()
            #print(f"Solution TSS = {S}")
            #print(f"Solution Size = {len(S)}")
            #ic(S)  