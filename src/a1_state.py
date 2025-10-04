#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

Includes a State class for Task 1

@author: A3 REPLACE WITH OUR STUDENT ID'S :(12345, 5678, and 89123)
@date:   04/10/2025
"""

class State:
    
    def __init__(self,grid):
        '''
        Parameters
        ----------
        grid : 2D List of lists

        '''
        
        self.grid = grid
        
    def __str__(self):
        return f'{self.grid}'
    
    def clone(self):
        '''
        Returns
        -------
        List (copy)
        '''
        grid_copy = [row[:] for row in self.grid]
        return grid_copy
    
    def moves(self):
        '''
        Returns
        -------
        A generator of all possible next states
        '''
        
        
grid = [[1,1,0,2],
        [1,1,0,0],
        [0,1,1,1],
        [0,0,1,1]]

st = State(grid)
print(st) 