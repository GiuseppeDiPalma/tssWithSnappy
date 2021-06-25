from typing import Any
import random as rnd
import sys
import snap
import platform
from icecream import ic
from time import time


def t(v):
    return 2

def initialize_threshold(graph,threshold):
    threshold_array = [min(threshold,graph.GetNI(i).GetDeg()) for i in range(1,graph.GetNodes()+1,1)]
    return threshold_array

def load_graph(path):
    graph = snap.LoadEdgeList(snap.TUNGraph, path, 0, 1, "\t")
    return graph


def get_probability_edge(edge):
    return 0.5


def subgraph(graph):
    for e in graph.Edges():
        if rnd.random() > get_probability_edge(e):
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
                for i in range(0,degree):
                    if threshold_array[v.GetNbrNId(i)-1] > 0:
                        threshold_array[v.GetNbrNId(i)-1] -= 1
                graph.DelNode(id)
        else:
            if v_minor_id != None:
                S.add(v_minor_id)
                v_minor = graph.GetNI(v_minor_id)
                degree = v_minor.GetDeg()
                for i in range(0,degree):
                    if threshold_array[v_minor.GetNbrNId(i)-1] > 0:
                        threshold_array[v_minor.GetNbrNId(i)-1] -= 1
                graph.DelNode(v_minor_id) 
            else:
                graph.DelNode(max_vertex_id)
    return S
    

def main():
    rnd.seed(1234)
    
    for i in range(1,11,1):        
        graph = load_graph("resources/blog_catalog_3.txt")
        print(f"Graph loaded at iteration {i}")
        print(f"Graph size: |N| = {graph.GetNodes()} - |E| = {graph.GetEdges()}\n")
        threshold_array = initialize_threshold(graph,i)
        
        ic.disable()
        start = time()
        S = TSS(graph,threshold_array)
        ic.enable()
        print(f"Elapsed time: {time()-start} - Threshold: {i} - |S| = {len(S)}\n")
        ic(S)
    
