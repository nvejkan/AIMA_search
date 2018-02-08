# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:18:33 2018

@author: nattawutvejkanchana
"""

from graph import *

def uniform_cost_search(problem):
    node = Node(problem.get_init_state(),0)
    frontier = [node]
    explored = dict()
    while(True):
        if len(frontier) == 0:
            print("Failure")
            return False
            
        node = frontier.pop(0)
        
        if problem.get_goal_state() == node.state:
            return solution(node)
        
        #check to add node to explored
        explored[node.state] = node.cost
        for action in problem.get_actions(node.state):
            child = problem.child_node(node,action)
            if (not child.state in explored.keys() \
                or (child.state in explored.keys() and child.cost < explored.get(child.state))):
                    frontier.append(child)
                    frontier.sort()
                    
def depth_limited_search(problem,limit):
    return recursive_dls(Node(problem.get_init_state(),0),problem, limit)

def recursive_dls(node,problem,limit):
    #return : solution, 0==cutoff, -1==Failure
    if problem.get_goal_state() == node.state:
        return solution(node)
    elif limit == 0:
        return 0 #cutoff
    else:
        cutoff_occurred = False
        for action in problem.get_actions(node.state):
            child = problem.child_node(node,action)
            result = recursive_dls(child,problem,limit-1)
            if result == 0:
                cutoff_occurred = True
            elif result != -1:
                return result
        if cutoff_occurred:
            return 0
        else:
            return -1

#test
#probA = Path_problem(graph_A,"S","B")
#depth_limited_search(probA,1)
#depth_limited_search(probA,2)
#depth_limited_search(probA,3)
#depth_limited_search(probA,4)
#depth_limited_search(probA,5)