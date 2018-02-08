# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:47:07 2018

@author: nattawutvejkanchana
"""
from uniform_cost_search import *
from iterative_deepening_search import *
from astar_search import *

def load_graph(filename):
    ret_graph = dict()
    f = open(filename)
    for line in f:
        l = line.strip().split(",")
        v1 = l[0]
        v2 = l[1]
        cost = int(l[2])
        
        #v1 -> v2
        if ret_graph.get(v1) == None:
            ret_graph[v1] = [(v2,cost)]
        else:
            edge_list = ret_graph.get(v1)
            edge_list.append((v2,cost))
            ret_graph[v1] = edge_list
            
        #v2 -> v1
        if ret_graph.get(v2) == None:
            ret_graph[v2] = [(v1,cost)]
        else:
            edge_list = ret_graph.get(v2)
            edge_list.append((v1,cost))
            ret_graph[v2] = edge_list
    
    return ret_graph

def load_heuristic(filename):
    ret_h = dict()
    f = open(filename)
    for line in f:
        l = line.strip().split(",")
        ret_h[l[0]] = int(l[1])
    return ret_h


romania_g = load_graph("romania_input.txt")
romania_h = load_heuristic("romania_heuristic_input.txt")

prob_rom = Path_problem(romania_g,"A","B")
uniform_cost_search(prob_rom)

iterative_deepening(prob_rom)

prob_rom_heuristic = Path_problem(romania_g,"A","B",romania_h)
astar_search(prob_rom_heuristic)