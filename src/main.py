import sys
import snap
import platform


def load_graph(path): 
	return snap.LoadEdgeList(snap.TUNGraph, path, 0,1,)


def main():
	print("Python version: " + platform.python_version())
	graph = load_graph("resources/blog_catalog.txt")
	node = graph.GetNI(1)

	print(node.GetId())
