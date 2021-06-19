import sys
from typing import Any
import snap
import platform
import random as rnd


def t(v):
    return 2


def load_graph(path):
    graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1, "\t")
    threshold_array = [t(v) for v in graph.Nodes()]
    return graph, threshold_array


def get_probability_edge(edge):
    return 0.5


def get_subgraph(graph):
    for e in graph.Edges():
        if rnd.random() > get_probability_edge(e):
            graph.DelEdge(e.GetSrcNId(), e.GetDstNId())
    return graph


def TSS(graph, threshold_array):
    S = set()
    V_0 = set()
    while graph.GetNodes() > 0:
        v_minor_id = None
        max_vertex_id = -1
        max_value = -1
        for v in graph.Nodes():
            id = v.GetId()
            degree = v.GetDeg()
            if threshold_array[id] == 0:
                V_0.add(id)
            elif threshold_array[id] > degree:
                v_minor_id = id
            else:
                c = threshold_array[id] / degree * (degree+1)
                if c > max_value:
                    max_vertex_id = id
                    max_value = c
        ######## Compute thresholds ############
        if len(V_0) > 0:
            while len(V_0) > 0:
                id = V_0.pop()
                v = graph.GetNI(id)
                degree = v.GetDeg()
                for i in range(0,degree):
                    threshold_array[v.GetNbrNId(i)] -= 1
                graph.DelNode(v.GetId()) 
        elif v_minor_id != None:
            S.add(v_minor_id)
            v_minor = graph.GetNI(v_minor_id)
            degree = v_minor.GetDeg()
            for i in range(0,degree):
                threshold_array[v_minor.GetNbrNId(i)] -= 1
            graph.DelNode(v_minor.GetId()) 
        else:
            graph.DelNode(max_vertex_id)
    return S
    

def main():
    rnd.seed(1234)
    print("Python version: " + platform.python_version())
    # graph, threshold_array = load_graph("resources/blog_catalog.txt")
    graph = snap.GenRndGnm(snap.TUNGraph, 500, 1024)
    threshold_array = [t(v) for v in graph.Nodes()]
    subgraph = get_subgraph(graph)
    S = TSS(subgraph,threshold_array)
    
    for node in S:
        print(node)
    
