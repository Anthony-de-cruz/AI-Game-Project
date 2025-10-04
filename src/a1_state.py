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
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)

    
    def clone(self):
        '''
        Returns
        -------
        List (copy)
        '''
        return [row[:] for row in self.grid]
    
    def moves(self):
        '''
        Returns
        -------
        A generator of all possible next states
        '''
        for i in range(len(self.grid)):
            for j in range (len(self.grid[i])):
                if self.grid[i][j] > 0: # An active cell
                    new_grid = self.clone() 
                    new_grid[i][j] -= 1
                    yield State(new_grid)
           
grid = [[1,1,0,2],
        [1,1,0,0],
        [0,1,1,1],
        [0,0,1,1]]

st = State(grid)

print(f'The Original state is : \n{st}')
print('\nThe next possible moves are : \n')
for next_state in st.moves():
    print(next_state)
    print()