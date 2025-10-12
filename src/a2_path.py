#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

Includes a State class for Task 2

@author: A3 REPLACE WITH OUR STUDENT ID'S :(12345, 5678, and 89123)
@date:   11/10/2025
"""

from a1_state import State

# Safe path = a sequence of moves that never creates or passes through a hinger cell
def path_BFS(start,end): # Anthony?
    pass

def path_DFS(start: State,end: State) -> list[State] | None:

    if (start == end or
        start.numHingers() or
        end.numHingers()):
        return None

    stack=[(start,[start])]
    while stack:
        vertex,path=stack.pop()
        #obtain remaining adjacent vertices
        adj = vertex.moves()
        for v in adj:  #next vertex to explore
            if v.numHingers():
                continue
            elif v.grid == end.grid:
                return path+[v]
            else:
                stack.append((v,path+[v]))

    return None

def path_IDDFS(start,end): # Mason
    pass

def path_astar(start,end): # ?
    pass

def tester():
    state1 = State([[1,1,0,1],
                    [1,2,0,0],
                    [0,0,2,1],
                    [0,0,1,1]])

    state2 = State([[1,1,0,0],
                    [1,2,0,0],
                    [0,0,2,0],
                    [0,0,1,0]])

    print(state2.numHingers())

    thing = path_DFS(state1, state2)
    if(thing == None):
        print("NO PATH")
        return;

    print("PATH")
    for move in thing:
        print("=======")
        print(move)

if __name__ == "__main__":
    tester()
