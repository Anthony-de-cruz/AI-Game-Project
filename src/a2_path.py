#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, TBC)
@date:   12/10/2025

"""

import time
import unittest
from collections import deque
from heapq import heappush, heappop
from typing import List, Tuple

from a1_state import State


# Safe path = a sequence of moves that never creates or passes through a hinger cell


def path_BFS(start: State, end: State) -> list[State] | None:
    """
    Navigates to the end state via the breadth first search algorithm.

    Parameters
    ----------
    start : The initial state.
    end : The goal state.

    Returns
    -------
    list[State] | None
        List of states from start to end. None if no path exists.
    """
    if start == end or start.numHingers() or end.numHingers():
        return None

    visited = set([start])
    queue = deque([(start, [start])])  # (current_state, path_of_moves)

    while queue:
        state, path = queue.popleft()

        for next_state in state.moves():
            if next_state not in visited:
                if state.numHingers():
                    continue
                if next_state.grid == end.grid:
                    return path + [next_state]
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None  # no path found


def path_DFS(start: State, end: State) -> list[State] | None:
    """
    Navigates to the end state via the depth first search algorithm.

    Parameters
    ----------
    start : The initial state.
    end : The goal state.

    Returns
    -------
    list[State] | None
        List of states from start to end. None if no path exists.
    """
    if start == end or start.numHingers() or end.numHingers():
        return None

    visited = set()
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)

        for v in vertex.moves():
            if v.numHingers() or v in visited:
                continue
            if v == end or v.grid == end.grid:
                return path + [v]

            stack.append((v, path + [v]))


# IDDFS = Split into DLS (Depth limited search) and IDDFS to recursively call DLS
def path_DLS(start: State, end: State, max_depth: int) -> list[State] | None:
    if start == end or start.numHingers() or end.numHingers():
        return None

    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        # obtain remaining adjacent vertices
        adj = vertex.moves()
        if len(path) >= max_depth:
            continue
        for v in adj:
            if v.numHingers():
                continue
            elif v.grid == end.grid:
                return path + [v]
            else:
                stack.append((v, path + [v]))
    return None


def path_IDDFS(start: State, end: State, max_limit: int = 20) -> list[State] | None:
    """
    Navigates to the end state via the iterative deepening depth first search algorithm.

    Parameters
    ----------
    start : The initial state.
    end : The goal state.
    max_limit : The maximum search depth.

    Returns
    -------
    list[State] | None
        List of states from start to end. None if no path exists.
    """
    for depth in range(max_limit + 1):
        result = path_DLS(start, end, depth)
        if result:
            return result
    return None


def calcualte_astar_heuristic(state: State, end: State) -> int:
    """
    Parameters
    ----------
    start : The initial state.
    end : The goal state.

    Returns
    -------
    int
        The calculated heuristic.
    """

    heuristic = 0
    for i in range(len(state.grid)):
        for j in range(len(state.grid[0])):
            heuristic += state.grid[i][j] != end.grid[i][j]
    return heuristic


def path_ASTAR(start: State, end: State) -> list[State] | None:
    """
    Navigates to the end state via the A* algorithm.

    The heuristic used is the sum of all hinger cells that are different.
    This is used to help determine if a cell needs to change.
    If a the number of different cells goes up, you're probably doing the wrong
    thing and should focus on the cells that are different.

    Parameters
    ----------
    start : The initial state.
    end : The goal state.

    Returns
    -------
    list[State] | None
        List of states from start to end. None if no path exists.
    """
    if start == end or start.numHingers() or end.numHingers():
        return None

    # The priority queue checks the second element if 1st is equal.
    counter = 0
    # (cost_to_end, counter, state, path, cost_from_start)
    priority_queue = [(0, counter, start, [start], 0)]
    visited = {}  # state : best cost_from_start
    visited[start] = 0

    while priority_queue:
        _, _, state, path, cost_from_start = heappop(priority_queue)

        if state in visited and visited[state] < cost_from_start:
            continue

        for next_state in state.moves():
            if next_state.numHingers():
                continue

            if next_state.grid == end.grid:
                return path + [next_state]

            new_cost_from_start = cost_from_start + 1  # Cost of 1 per move

            if next_state not in visited or new_cost_from_start < visited[next_state]:
                visited[next_state] = new_cost_from_start
                heuristic = calcualte_astar_heuristic(next_state, end)
                new_cost_to_end = new_cost_from_start + heuristic
                counter += 1
                heappush(
                    priority_queue,
                    (
                        new_cost_to_end,
                        counter,
                        next_state,
                        path + [next_state],
                        new_cost_from_start,
                    ),
                )

    return None


def compare(tests: List[Tuple[State, State]], repetitions) -> None:
    print("\nComparing BFS, DFS, IDDFS, and A* performance:\n")

    for test in tests:
        print()
        for index in range(len(test[0].grid)):
            for value in test[0].grid[index]:
                print(f"{value} ", end="")
            if index == int(len(test[0].grid) / 2):
                print("--> ", end="")
            else:
                print("    ", end="")

            for value in test[1].grid[index]:
                print(f"{value} ", end="")
            print()
        print()

        algos = {
            "BFS": path_BFS,
            "DFS": path_DFS,
            "IDDFS": path_IDDFS,
            "A*": path_ASTAR,
        }

        print(
            f"{'Algorithm':<10} {'Found?':<8} {'Path Len':<10} {'Time Avg (s)':<10}",
            end="",
        )
        for x in range(repetitions):
            print(f" {f'Time {x} (s)':<11}", end="")
        print()
        print("-" * (42 + repetitions * 12))

        for name, func in algos.items():
            times = []
            path = None
            for x in range(repetitions):
                t1 = time.time()
                path = func(test[0], test[1])
                t2 = time.time()
                times.append(t2 - t1)

            average = sum(times) / repetitions
            found = path is not None
            length = len(path) if path else 0
            print(f"{name:<10} {str(found):<8} {length:<10} {average:<12.6f}", end="")
            for x in range(repetitions):
                print(f" {times[x]:<11.6f}", end="")
            print()

        print("-" * (42 + repetitions * 12))


test_valid_1 = (
    State([[1, 1, 0], [1, 2, 0], [0, 1, 2]]),
    State([[1, 1, 0], [1, 2, 0], [0, 0, 2]]),
)

test_valid_2 = (
    State([[1, 1, 0], [1, 2, 0], [0, 0, 2]]),
    State([[0, 0, 0], [1, 2, 0], [0, 0, 2]]),
)

test_valid_3 = (
    State([[3, 1, 0], [1, 2, 0], [0, 0, 2]]),
    State([[0, 0, 0], [1, 2, 0], [0, 0, 2]]),
)

test_valid_4 = (
    State([[1, 1, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]),
    State([[1, 1, 0, 0], [1, 2, 0, 0], [0, 0, 2, 0], [0, 0, 1, 0]]),
)

test_valid_5 = (
    State([[1, 1, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]),
    State([[0, 0, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 0, 0]]),
)

test_invalid_1 = (
    State([[1, 1, 0], [1, 2, 0], [0, 0, 2]]),
    State([[1, 1, 0], [1, 1, 0], [0, 0, 2]]),
)

test_invalid_2 = (
    State([[1, 1, 0], [1, 2, 0], [0, 0, 2]]),
    State([[1, 1, 0], [1, 0, 0], [0, 0, 2]]),
)


class TestA2(unittest.TestCase):
    def test_path_BFS(self):
        self.assertNotEqual(path_BFS(test_valid_1[0], test_valid_1[1]), None)
        self.assertNotEqual(path_BFS(test_valid_2[0], test_valid_2[1]), None)
        self.assertNotEqual(path_BFS(test_valid_3[0], test_valid_3[1]), None)
        self.assertNotEqual(path_BFS(test_valid_4[0], test_valid_4[1]), None)
        self.assertNotEqual(path_BFS(test_valid_5[0], test_valid_5[1]), None)

        self.assertEqual(path_BFS(test_invalid_1[0], test_invalid_1[1]), None)
        self.assertEqual(path_BFS(test_invalid_2[0], test_invalid_2[1]), None)

    def test_path_DFS(self):
        self.assertNotEqual(path_DFS(test_valid_1[0], test_valid_1[1]), None)
        self.assertNotEqual(path_DFS(test_valid_2[0], test_valid_2[1]), None)
        self.assertNotEqual(path_DFS(test_valid_3[0], test_valid_3[1]), None)
        self.assertNotEqual(path_DFS(test_valid_4[0], test_valid_4[1]), None)
        self.assertNotEqual(path_DFS(test_valid_5[0], test_valid_5[1]), None)

        self.assertEqual(path_DFS(test_invalid_1[0], test_invalid_1[1]), None)
        self.assertEqual(path_DFS(test_invalid_2[0], test_invalid_2[1]), None)

    def test_path_IDDFS(self):
        self.assertNotEqual(path_IDDFS(test_valid_1[0], test_valid_1[1]), None)
        self.assertNotEqual(path_IDDFS(test_valid_2[0], test_valid_2[1]), None)
        self.assertNotEqual(path_IDDFS(test_valid_3[0], test_valid_3[1]), None)
        self.assertNotEqual(path_IDDFS(test_valid_4[0], test_valid_4[1]), None)
        self.assertNotEqual(path_IDDFS(test_valid_5[0], test_valid_5[1]), None)

        self.assertEqual(path_IDDFS(test_invalid_1[0], test_invalid_1[1]), None)
        self.assertEqual(path_IDDFS(test_invalid_2[0], test_invalid_2[1]), None)

    def test_path_ASTAR(self):
        self.assertNotEqual(path_ASTAR(test_valid_1[0], test_valid_1[1]), None)
        self.assertNotEqual(path_ASTAR(test_valid_2[0], test_valid_2[1]), None)
        self.assertNotEqual(path_ASTAR(test_valid_3[0], test_valid_3[1]), None)
        self.assertNotEqual(path_ASTAR(test_valid_4[0], test_valid_4[1]), None)
        self.assertNotEqual(path_ASTAR(test_valid_5[0], test_valid_5[1]), None)

        self.assertEqual(path_ASTAR(test_invalid_1[0], test_invalid_1[1]), None)
        self.assertEqual(path_ASTAR(test_invalid_2[0], test_invalid_2[1]), None)


def tester():
    print("Running unit test suite...")
    unittest.main(exit=False)

    tests = [
        (
            State([[2, 1, 1], [1, 2, 2], [1, 1, 1]]),
            State([[0, 1, 1], [1, 2, 1], [0, 1, 0]]),
        ),
        (
            State([[2, 1, 1], [1, 1, 1], [2, 2, 1]]),
            State([[0, 1, 0], [0, 1, 1], [1, 1, 0]]),
        ),
        (
            State([[4, 1, 1], [1, 1, 1], [1, 1, 1]]),
            State([[0, 1, 0], [1, 1, 0], [1, 1, 0]]),
        ),
        (
            State([[4, 1, 1], [1, 1, 1], [1, 1, 1]]),
            State([[0, 1, 0], [1, 1, 0], [1, 1, 0]]),
        ),
        (
            State([[1, 1, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]),
            State([[1, 1, 0, 0], [1, 2, 0, 0], [0, 0, 2, 0], [0, 0, 1, 0]]),
        ),
        (
            State([[1, 1, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]),
            State([[0, 0, 0, 1], [1, 2, 0, 0], [0, 0, 2, 1], [0, 0, 0, 0]]),
        ),
        (
            State(
                [
                    [1, 1, 0, 1, 1],
                    [1, 2, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                ]
            ),
            State(
                [
                    [0, 0, 0, 1, 0],
                    [1, 2, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                ]
            ),
        ),
        (
            State(
                [
                    [1, 1, 0, 1, 1],
                    [2, 2, 0, 0, 0],
                    [2, 0, 2, 1, 0],
                    [1, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                ]
            ),
            State(
                [
                    [1, 0, 0, 1, 0],
                    [2, 2, 0, 0, 0],
                    [2, 0, 2, 1, 0],
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                ]
            ),
        ),
    ]

    print("\nPerforming algorithmic analysis...")
    compare(tests, 3)


if __name__ == "__main__":
    tester()
