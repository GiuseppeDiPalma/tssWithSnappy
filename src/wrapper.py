import math
import random as rnd
from time import time
import snap
from icecream import ic
from scipy.io import mmread
from bitarray import bitarray

def get_bitest_for_each_node(graph):
    list_b = []
    list_b.append(bitarray()) # Blank element 
    num_nodes = graph.GetNodes()
    for node in graph.Nodes():
        bitset = bitarray(num_nodes+1)
        bitset.setall(0)
        degree = node.GetDeg()
        for i in range(0, degree):
            bitset[node.GetNbrNId(i)] = True
        list_b.append(bitset)
    return list_b

def tf_constant(i):
    return i

# t(v) = a * d(v) / b
def tf_degree_based(v, a, b):
    return math.ceil(a * v.GetDeg() / b)


def p_edge_neighborhood_biased(graph, e,bitset_list):
    src_id = e.GetSrcNId()
    dst_id = e.GetDstNId()
    src_node = graph.GetNI(src_id)
    dst_node = graph.GetNI(dst_id)
    src_degree = src_node.GetDeg()
    dst_degree = dst_node.GetDeg()

    common_neighbors = (bitset_list[src_id] & bitset_list[dst_id]).count()
    num_neighbors = (src_degree + dst_degree - common_neighbors - 1) * 1 / 100
    
    overlap = common_neighbors / (num_neighbors + 1)
    
    return overlap if overlap < 1 else 1


def p_edge_neighborhood_biased_reverse(graph, e,bitset_list):
    return 1 - p_edge_neighborhood_biased(graph, e,bitset_list)


def p_edge_uniform(graph, e,bitset_list):
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
    return graph

def load_mtx_graph(path):
    graph = snap.LoadEdgeList(snap.TUNGraph, mmread(path), 0, 1, ' ')
    print(graph)
    return graph


def subgraph(graph, p_function,bitset_list):
    list_edge = []
    for e in graph.Edges():
        if rnd.random() > p_function(graph, e,bitset_list):
            list_edge.append((e.GetSrcNId(), e.GetDstNId()))
    for e in list_edge:
        graph.DelEdge(e[0], e[1])

def TSS(graph, threshold_array):
    S = set()
    V_0 = set()
    num = 0
    while graph.GetNodes() > 0:
        num += 1
        v_minor_id = None
        max_vertex_id = -1
        max_value = -1
    
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