import math , os
from optparse import OptionParser
from typing import Any
import random as rnd
import snap
from icecream import ic
from time import time

DECIMALNUMBER = 4

def tf_constant(i):
    return i

# t(v) = a * d(v) / b
def tf_degree_based(v, a, b):
    return math.ceil(a * v.GetDeg() / b)


def p_edge_neighborhood_biased(graph, e):
    src_node = graph.GetNI(e.GetSrcNId())
    dst_node = graph.GetNI(e.GetDstNId())
    common_neighbors = 0
    src_degree = src_node.GetDeg()
    dst_degree = dst_node.GetDeg()
    for i in range(0, src_degree):
        node_1_id = src_node.GetNbrNId(i)
        for j in range(0, dst_degree):
            node_2_id = dst_node.GetNbrNId(j)
            if node_1_id == node_2_id:
                common_neighbors += 1
    num_neighbors = (src_degree + dst_degree - 2) * 20 / 100
    overlap = common_neighbors / (num_neighbors + 1)
    return overlap if overlap < 1 else 1


def p_edge_neighborhood_biased_reverse(graph, e):
    return 1 - p_edge_neighborhood_biased(graph, e)


def p_edge_uniform(graph, e):
    return rnd.random()


def initialize_threshold(graph, threshold_function, a, b=-1):
    threshold_array = []
    if b == -1:
        threshold_array = [min(threshold_function(a), graph.GetNI(
            i).GetDeg()) for i in range(1, graph.GetNodes()+1, 1)]
    else:
        for i in range(1, graph.GetNodes()+1, 1):
            if i == 106:
                print("")
            threshold_array.append(min(threshold_function(
                graph.GetNI(i), a, b), graph.GetNI(i).GetDeg()))
        # threshold_array = [min(threshold_function(graph.GetNI(i),a,b),graph.GetNI(i).GetDeg()) for i in range(1,graph.GetNodes()+1,1)]
    return threshold_array


def load_graph(path):
    graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1, '\t')
    #graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1, "\t")
    return graph


def subgraph(graph, p_function):
    for e in graph.Edges():
        if rnd.random() > p_function(graph, e):
            graph.DelEdge(e.GetSrcNId(), e.GetDstNId())

def TSS(graph, threshold_array):
    S = set()
    V_0 = set()
    num = 0
    while graph.GetNodes() > 0:
        num += 1
        v_minor_id = None
        max_vertex_id = -1
        max_value = -1
        ic(num)
        for v in graph.Nodes():
            id = v.GetId()
            degree = v.GetDeg()

            if threshold_array[id-1] == 0:
                V_0.add(id)
            else:
                if threshold_array[id-1] > degree:
                    v_minor_id = id
                else:
                    c = threshold_array[id-1] / (degree * (degree+1))
                    if c > max_value:
                        max_vertex_id = id
                        max_value = c
        ######## Compute thresholds ############
        if len(V_0) > 0:
            while len(V_0) > 0:
                id = V_0.pop()
                v = graph.GetNI(id)
                degree = v.GetDeg()
                for i in range(0, degree):
                    if threshold_array[v.GetNbrNId(i)-1] > 0:
                        threshold_array[v.GetNbrNId(i)-1] -= 1
                graph.DelNode(id)
        else:
            if v_minor_id != None:
                S.add(v_minor_id)
                v_minor = graph.GetNI(v_minor_id)
                degree = v_minor.GetDeg()
                for i in range(0, degree):
                    if threshold_array[v_minor.GetNbrNId(i)-1] > 0:
                        threshold_array[v_minor.GetNbrNId(i)-1] -= 1
                graph.DelNode(v_minor_id)
            else:
                graph.DelNode(max_vertex_id)
    return S

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