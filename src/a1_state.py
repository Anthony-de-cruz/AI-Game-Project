#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, 100357095)
@date:   12/10/2025

"""

import unittest

class State:
    
    def __init__(self,grid):
        '''
        Parameters
        ----------
        grid : 2D List of lists that the game is played on

        '''
        
        self.grid = grid
        
    def __str__(self):
        '''

        Returns
        -------
        A more readable representation of the grid

        '''
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)

    
    def clone(self):
        '''
        Returns
        -------
        A List (deep copy) of the grid
        '''
        return [row[:] for row in self.grid]
    
    def moves(self):
        '''
        Returns
        -------
        A generator of all possible next states in the game
        '''
        for i in range(len(self.grid)):
            for j in range (len(self.grid[i])):
                if self.grid[i][j] > 0: # An active cell
                    new_grid = self.clone() 
                    new_grid[i][j] -= 1
                    yield State(new_grid)
                    
    def numRegions(self):
        """
        Returns
        -------
        The number of active regions on the board
        """
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)] # 2D Array of False to mirror the board dimensions
        active_regions = 0
    
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] > 0 and not visited[i][j]:
                    active_regions += 1
                    stack = [(i, j)]
    
                    while stack:
                        row, col = stack.pop()
                        if not visited[row][col]:
                            visited[row][col] = True
                            # Check all possible surrounding cells using the max method
                            for neighbor_row in range(max(0, row - 1), min(rows, row + 2)):
                                for neighbor_col in range(max(0, col - 1), min(cols, col + 2)):
                                    # Use to ensure it's a neighbor where a -x = row distance (vert) and b - y is column distance (hor)
                                    if max(abs(row - neighbor_row), abs(col - neighbor_col)) == 1:
                                        if (
                                            self.grid[neighbor_row][neighbor_col] > 0
                                            and not visited[neighbor_row][neighbor_col]
                                        ):
                                            stack.append((neighbor_row, neighbor_col))
        return active_regions


    def numHingers(self):
        """
        Returns 
        --------
        the number of hinger cells currently on the board
        """
        hingers = 0
        current_regions = self.numRegions()  # Current number of active regions
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == 1:  # If an active cell
                    # Simulate removing this counter
                    new_grid = self.clone()  # Clone the grid
                    new_grid[i][j] = 0
                    new_state = State(new_grid)
                    
                    if new_state.numRegions() > current_regions:
                        hingers += 1
                        
        return hingers




class TestA1(unittest.TestCase):
    def test_numHingers(self):
        grid = [[1,1,0,2],
                [1,1,0,0],
                [0,0,1,1],
                [0,0,1,1]]
        self.assertEqual(State(grid).numHingers(), 2)

        grid = [[1,1,0,2],
                [1,2,0,0],
                [0,0,1,1],
                [0,0,1,1]]
        self.assertEqual(State(grid).numHingers(), 1)

        grid = [[1,1,0,2],
                [1,2,0,0],
                [0,0,2,1],
                [0,0,1,1]]
        self.assertEqual(State(grid).numHingers(), 0)

    def test_numRegions(self):
        grid = [[1,1,0,2],
                [1,1,0,0],
                [0,0,1,1],
                [0,0,1,1]]
        self.assertEqual(State(grid).numRegions(), 2)

        grid = [[1,1,0,2],
                [1,0,0,0],
                [0,0,1,1],
                [0,0,1,1]]
        self.assertEqual(State(grid).numRegions(), 3)

       
def tester():         
    unittest.main(exit=False)

    grid = [[1,1,1],
            [1,1,1],
            [1,1,1]]
    
    st = State(grid)
    print("The number of active regions is:", st.numRegions())
    print("The number of hingers cells currently on the board is :", st.numHingers() )
    print(f'The Original state is : \n{st}')
    print('\nThe next possible moves are : \n')
    for next_state in st.moves():
        print(next_state)
        print()

if __name__=='__main__':
    tester()
