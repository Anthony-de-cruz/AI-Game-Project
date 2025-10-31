#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, TBC)
@date:   19/10/2025
"""

from a1_state import State

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
        
        for move in state.moves():
            value = self.minimum_value(move)
            if value > best_score:
                best_score = value
                best_move = move
        return best_move
    
    def maximum_val(self,state) -> int:
        if self.win(state):
            return self.utility(state)
        
        v = float("-inf")
        
        for move in state.moves():
            v = max(v, self.minimum_value(move))
    
        return int(v)
    
    def minimum_value(self,state) -> int:
        if self.win(state):
            return self.utility(state)
        
        v = float("inf")
        for move in state.moves():
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
        
        for move in state.moves():
            value = self.min_value_ab(move, alpha, beta)
            if value > best_score:
                best_score = value
                best_move = move
            alpha = max(alpha, best_score)
        return best_move
    
    def max_value_ab(self, state: State, alpha: float, beta: float) -> int:
        if self.win(state):
            return self.utility(state)
        
        v = float("-inf")
        for move in state.moves():
            v = max(v, self.min_value_ab(move, alpha, beta))
            if v >= beta:
                return v  # prune
            alpha = max(alpha, v)
        return int(v)
    
    def min_value_ab(self, state: State, alpha: float, beta: float) -> int:
        if self.win(state):
            return self.utility(state)
        
        v = float("inf")
        for move in state.moves():
            v = min(v, self.max_value_ab(move, alpha, beta))
            if v <= alpha:
                return int(v)  # prune
            beta = min(beta, v)
        return int(v)
            
    
    def win(self, state: State) -> bool:
        '''

        Parameters
        ----------
        state : State of the current board 

        Returns
        -------
        True or False depending on whether the player has one

        '''
        return state.numHingers() > 0 or not any(state.moves())
    
    def utility(self, state: State) -> int:
        '''
        
        Evaluates the Utility of a terminal game state
        Parameters
        ----------
        state : State of the current board

        Returns
        -------
        int
            +1 if the curent player has won the game
            -1 if the cirrent player has lost the game

        '''
        if state.numHingers() > 0:
            return -1
        else:
            return 1
        
def tester():
    state1 = State([[1,1,1],
                    [1,1,1],
                    [1,1,1]])
    agent = Agent((3,3))
        
    print("Initial State: ")
    print(state1)
        
    print("\nBest move (minimax):")
    move = agent.move(state1, mode="alphabeta")
    while move:
        print(move)
        move = agent.move(move, mode="alphabeta")


if __name__ == "__main__":
    tester()
