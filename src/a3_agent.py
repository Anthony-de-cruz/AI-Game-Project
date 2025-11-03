#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, 100357095)
@date:   19/10/2025
"""

import time

from a1_state import State

import matplotlib.pyplot as plt


class Agent:
 
    def __init__(self, size, name = "A23"):
        '''

        Parameters
        ----------
        size : Size of the grid
        name : The name of the agent or group

        Returns
        -------
        None.

        '''
        self.size = size
        self.name = name
        self.modes = ["minimax", "alphabeta"]
        
    def __str__(self):
        '''

        Returns
        -------
        Name of the agent

        '''
        return self.name
    
    def move(self, state: State, mode = "minimax") -> State| None:
        '''

        Parameters
        ----------
        state : State of the current game board
        mode : The game playing strategy used by the agent

        Returns
        -------
        The next best state or none

        '''
        if mode == 'minimax':
            return self.minimax(state)
        elif mode == 'alphabeta':
            return self.alphabeta_search(state)
        else:
            raise ValueError(f"Unknown mode '{mode}'. Use 'minimax' or 'alphabeta'.")
        
    
    def minimax(self,state: State) -> State| None:
        '''

        Parameters
        ----------
        state : State of the current game board

        Returns
        -------
        best_move : State | None
            The move that maximizes the player's chances of winning, based on the minimax evaluation.

        '''
        best_score = float("-inf")
        best_move = None
        
        current_regions = state.numRegions()
        possible_moves = list(state.moves())
        for move in possible_moves:
            if move.numRegions() > current_regions:
                return move
            value = self.minimum_value(move)
            if value > best_score:
                best_score = value
                best_move = move
        return best_move
    
    def maximum_val(self,state) -> int:
        possible_moves = list(state.moves())
        if not possible_moves:
            return -1 # max has no moves so max loses
        
        current_regions = state.numRegions()

        v = float("-inf")
        
        for move in state.moves():
            if move.numRegions() > current_regions:
                return 1 # max finds a winning move
            
            v = max(v, self.minimum_value(move))
    
        return int(v)
    
    def minimum_value(self,state) -> int:
        possible_moves = list(state.moves())
        if not possible_moves:
            return 1    # max has no moves so max loses
        
        current_regions = state.numRegions()

        v = float("inf")
        
        for move in state.moves():
            if move.numRegions() > current_regions:
                return -1 # max finds a winning move
            
            v = min(v, self.maximum_val(move))
        return int(v)

    def alphabeta_search(self, state: State) -> State | None:
        '''
        Implements alpha-beta pruning to choose the best move.
        '''
        best_score = float("-inf")
        best_move = None
        alpha = float("-inf")
        beta = float("inf")
        
        current_regions = state.numRegions()
        possible_moves = list(state.moves())

        if not possible_moves:
            return None # No possible moves
        for move in possible_moves:
            # Check for a a win
            if move.numRegions() > current_regions:
                return move
            value = self.min_value_ab(move, alpha, beta)
            if value > best_score:
                best_score = value
                best_move = move
            alpha = max(alpha, best_score)
        return best_move
    
    def max_value_ab(self, state: State, alpha: float, beta: float) -> int:
        possible_moves = list(state.moves())
        if not possible_moves:
            return -1
        
        current_regions = state.numRegions()
        v = float("-inf")
        for move in state.moves():
            if move.numRegions() > current_regions:
                return 1
            v = max(v, self.min_value_ab(move, alpha, beta))
            if v >= beta:
                return v  # prune
            alpha = max(alpha, v)
        return int(v)
    
    def min_value_ab(self, state: State, alpha: float, beta: float) -> int:
        possible_moves = list(state.moves())
        if not possible_moves:
            return 1
        
        current_regions = state.numRegions()
        v = float("inf")
        for move in state.moves():
            if move.numRegions() > current_regions:
                return -1
            v = min(v, self.max_value_ab(move, alpha, beta))
            if v <= alpha:
                return v  # prune
            beta = min(beta, v)
        return int(v)
    
    
    

def compare(agent: Agent, tests: list[State]) -> None:
    
    times: dict[str, list[float]] = {"minimax": [], "alphabeta": []}

    for algo in times:
        print(f"Testing: {algo}...")
        for start in tests:
            t1 = time.time()
            
            # --- Simulated game loop ---
            current_state = start
            while True:
                current_regions = current_state.numRegions()
                next_move = agent.move(current_state, mode=algo)

                # Condition 1: Game over (Loss)
                # The agent had no moves and returned None
                if next_move is None:
                    break 
                
                # Condition 2: Game over (Win)
                # The agent took a hinger
                if next_move.numRegions() > current_regions:
                    break

                # continue the game
                current_state = next_move
            # --- End of loop ---

            t2 = time.time()
            times[algo].append(t2 - t1)
        print(times[algo])

    averages = {k: sum(v) / len(v) for k, v in times.items()}

    # --- Print results ---
    print("\nAverage completion times:")
    for algo, avg in averages.items():
        print(f"  {algo:<10} = {avg:.6f} s")

    # --- Line Plot: Performance per test ---
    plt.figure(figsize=(8, 5))
    num_tests = len(next(iter(times.values())))
    test_labels = [f"Test {i+1}" for i in range(num_tests)]

    for algo, results in times.items():
        plt.plot(test_labels, results, marker="o", label=algo)

    plt.title("Algorithm Performance per Test", fontsize=14, fontweight="bold", pad=10)
    plt.xlabel("Test Case", fontsize=12)
    plt.ylabel("Completion Time (s)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("minimax_vs_alphabeta_tests.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.clf()

    # --- Bar Chart: Average completion times ---
    plt.figure(figsize=(7, 5))
    algos = list(averages.keys())
    avg_times = list(averages.values())
    colors = ["#4E79A7", "#F28E2B"]

    bars = plt.bar(algos, avg_times, color=colors, edgecolor="black", alpha=0.85)

    # Add text labels above bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + (yval * 0.05),
            f"{yval:.3f}s",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    plt.title("Average Runtime Comparison", fontsize=14, fontweight="bold", pad=15)
    plt.ylabel("Average Time (s)", fontsize=12)
    plt.xlabel("Algorithm", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("minimax_vs_alphabeta_avg.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.clf()


def tester():
    state1 = State([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    agent = Agent((3, 3))
    
    compare(
        agent,
        [
            State([[0, 1, 1], [0, 1, 1], [1, 1, 1]]),
            State([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            State([[1, 1, 1], [1, 2, 1], [1, 1, 1]]),
            State([[0, 2, 2], [0, 2, 1], [0, 2, 1]]),
            State([[0, 2, 2], [0, 2, 1], [0, 1, 0]]),
            State([[0, 1, 2], [0, 2, 0], [0, 2, 1]]),
        ],
    )
    
    

    print("Initial State: ")
    print(state1)

    print("\nBest move (minimax):")
    move = agent.move(state1, mode="minimax")
    while move:
        print(move)
        print("\n")
        move = agent.move(move, mode="minimax")

    print("\nBest move (alphabeta):")
    move = agent.move(state1, mode="alphabeta")
    while move:
        print(move)
        print("\n")
        move = agent.move(move, mode="alphabeta")


if __name__ == "__main__":
    tester()
