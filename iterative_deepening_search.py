# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:35:39 2018

@author: nattawutvejkanchana
"""

from depth_limited_search import *

def iterative_deepening(problem):
    for depth in range(0,99999):
        result = depth_limited_search(problem,depth)
        if result != 0: #not a cutoff
            print("stop at depth: {0}".format(depth))
            return result
            
#test
#probA = Path_problem(graph_A,"S","B")
#iterative_deepening(probA)       

            