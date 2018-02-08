# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:38:35 2018

@author: nattawutvejkanchana
"""

from graph import *

def astar_search(problem):
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