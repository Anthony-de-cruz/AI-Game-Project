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
        self.size = size
        self.name = name
        self.modes = ["minimax", "alphabeta"]
        
    def __str__(self):
        return self.name
    
    def move(self, state: State, mode = "minimax") -> State| None:
        if mode == 'minimax':
            return self.minimax(state)
        else:
            return None
        
    
    def minimax(self,state: State) -> State| None:
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
    
        return v
    
    def minimum_value(self,state) -> int:
        if self.win(state):
            return self.utility(state)
        
        v = float("inf")
        for move in state.moves():
            v = min(v, self.maximum_val(move))
    
        return v
            
    
    def win(self, state: State) -> bool:
        return state.numHingers() > 0 or not any(state.moves())
    
    def utility(self, state: State) -> int:
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
    move = agent.move(state1, mode="minimax")
    print(move)
    move1 = agent.move(move, mode="minimax")
    print(move1)
    move2 = agent.move(move1, mode="minimax")
    print(move2)
    move3 = agent.move(move2, mode="minimax")
    print(move3)
    move4 = agent.move(move3, mode="minimax")
    print(move4)
        

if __name__ == "__main__":
    tester()