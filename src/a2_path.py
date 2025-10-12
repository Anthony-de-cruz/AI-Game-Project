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

# IDDFS = Split into DLS (Depth limited search) and IDDFS to recursively call DLS
def path_DLS(start : State, end : State, max_depth : int) -> list[State] | None:
    
    if (start == end or start.numHingers() or end.numHingers()):
        return None
    
    stack=[(start,[start])]
    while stack:
        vertex,path=stack.pop()
        #obtain remaining adjacent vertices
        adj = vertex.moves()
        if len(path) >= max_depth:
            continue
        for v in adj:
            if v.numHingers():
                continue
            elif v.grid == end.grid:
                return path+[v]
            else:
                stack.append((v,path+[v]))
    return None
    
    
def path_IDDFS(start : State,end: State, max_limit: int = 20) -> list[State] | None: # Mason
    for depth in range(max_limit + 1):
        result = path_DLS(start, end, depth)
        if result:
            return result
    return None

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

    thing = path_IDDFS(state1, state2, max_limit = 5)
    if(thing == None):
        print("NO PATH")
    else:    
        print(f"PATH FOUND at depth {len(thing)-1}")
        print("PATH")
        for move in thing:
            print("=======")
            print(move)

if __name__ == "__main__":
    tester()
