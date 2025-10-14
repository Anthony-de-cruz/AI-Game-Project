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

from collections import deque

def path_BFS(start, end):
    start = tuple(start)
    end = tuple(end)
    n = len(start)

    # helper to generate neighbors by flipping one bit
    def neighbors(state):
        for i in range(n):
            new_state = list(state)
            new_state[i] = 1 - new_state[i]
            yield tuple(new_state), i

    visited = set([start])
    queue = deque([(start, [])])  # (current_state, path_of_moves)

    while queue:
        state, path = queue.popleft()
        if state == end:
            return path  # found path as list of bit indices flipped

        for next_state, move in neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))

    return None  # no path found

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
    print(path_BFS([0, 1, 0], [1, 0, 1]))  # Example 1
    print(path_BFS([0, 0, 0], [1, 1, 1]))  # Example 2
    print(path_BFS([1, 0, 1], [1, 0, 1]))  # Example 3 (same start and end)

    state1 = State([[1,1,1],
                    [1,1,2],
                    [2,2,2]])

    state2 = State([[0,0,0],
                    [1,1,1],
                    [1,1,1]])

    print(state2.numHingers())

    thing = path_IDDFS(state1, state2,max_limit = 8)
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
