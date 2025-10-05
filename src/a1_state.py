#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

Includes a State class for Task 1

@author: A3 REPLACE WITH OUR STUDENT ID'S :(12345, 5678, and 89123)
@date:   04/10/2025

TODO (Optional):
    - check if a cell is active
    - check if a cell is a hinger
    - more utility methods
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
                    # DFS from this cell
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        if not visited[row][col]:
                            visited[row][col] = True
                            # Check all 8 neighbors of current cell
                            for row_offset in [-1, 0, 1]:
                                for col_offset in [-1, 0, 1]:
                                    if row_offset == 0 and col_offset == 0:
                                        continue
                                    neighbor_row = row + row_offset
                                    neighbor_col = col + col_offset
                                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                                        if self.grid[neighbor_row][neighbor_col] > 0 and not visited[neighbor_row][neighbor_col]:
                                            stack.append((neighbor_row, neighbor_col))
                    active_regions += 1  
    
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



    

        
def tester():         
    grid = [[1,1,0,2],
            [1,1,0,0],
            [0,0,1,1],
            [0,0,1,1]]
    
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