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
        p_edge_neighborhood_biased, p_edge_uniform, p_edge_neighborhood_biased_reverse
        ]

    degree_coefficients = [(1,2),(1,3),(2,3)]
    constants = [2,4,6]
    #load_mtx_graph(options.dataset)

    print(f"Dataset name = {options.dataset}")

    for edge_function in edge_p_functions:
        print(f"\n---------- Edge function: {edge_function.__name__}----------\n")
    
        print(f"--- Degree based threshold with coefficient ---\n")
        # Degree based
        for coefficients in degree_coefficients:
            print(f"Coefficients: |a|={coefficients[0]} - |b|={coefficients[1]}")
            startL = time()
            graph = load_graph(options.dataset)
            print(f"load_graph: {round(time()-startL, DECIMALNUMBER)}")

            startS = time()
            subgraph(graph, edge_function)
            print(f"subgraph: {round(time()-startS, DECIMALNUMBER)}")

            print(f"Graph size: |N| = {graph.GetNodes()} - |E| = {graph.GetEdges()}")

            startT = time()
            threshold_array = initialize_threshold(graph, tf_degree_based, coefficients[0], coefficients[1])
            print(f"Initialize_threshold: {round(time()-startT, DECIMALNUMBER)}")

            ic.disable()

            startTSS = time()
            S = TSS(graph, threshold_array)
            print(f"TSS: {time()-startTSS}")
            print(f"|S| = {len(S)}")
            print("\n--------------\n")

            ic.enable()
            #print(f"Solution TSS = {S}")
            #print(f"Solution Size = {len(S)}")
            #ic(S)
        
        
        # Constants
        print(f"---Constant threshold ---")
        for value in constants:
            print(f"Threshold: {value}")
            startL = time()
            graph = load_graph(options.dataset)
            print(f"load_graph: {round(time()-startL, DECIMALNUMBER)}")

            startS = time()
            subgraph(graph, edge_function)
            print(f"subgraph: {round(time()-startS, DECIMALNUMBER)}")

            print(f"Graph size: |N| = {graph.GetNodes()} - |E| = {graph.GetEdges()} \n")

            startT = time()
            threshold_array = initialize_threshold(graph, tf_constant, value)
            print(f"Initialize_threshold: {round(time()-startT, DECIMALNUMBER)}")

            ic.disable()

            startTSS = time()
            S = TSS(graph, threshold_array)
            print(f"TSS: {time()-startTSS}")
            print(f"|S| = {len(S)}")
            print("\n--------------\n")

            ic.enable()
            #print(f"Solution TSS = {S}")
            #print(f"Solution Size = {len(S)}")
            #ic(S)  