#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

Includes a State class for Task 2

@author: A3 REPLACE WITH OUR STUDENT ID'S :(12345, 5678, and 89123)
@date:   11/10/2025
"""

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

def path_DFS(start,end): # Josh
    pass

def path_IDDFS(start,end): # Mason
    pass

def path_astar(start,end): # ?
    pass

def tester():
    print(path_BFS([0, 1, 0], [1, 0, 1]))  # Example 1
    print(path_BFS([0, 0, 0], [1, 1, 1]))  # Example 2
    print(path_BFS([1, 0, 1], [1, 0, 1]))  # Example 3 (same start and end)
    pass


if __name__ == "__main__":
    tester()
