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
                    
    def numRegions(self):
        '''
        Returns
        -------
        Number of active regions on the board
        '''
        row = len(self.grid)
        col = len(self.grid[0])
        
        visited = []
        active_regions = 0
        
        # Loop over all cells
        for i in range(row):
            for j in range(col):
                if self.grid[i][j] > 0 and (i,j) not in visited: # if active and not visited yet
                    active_regions += 1
                    stack = [(i,j)]
                    
                    #dfs
                    while stack:
                        a,b = stack.pop()
                        if (a,b) not in visited:
                            visited.append((a,b))
                            # Find neighours of (a,b)
                            for x in range(row):
                                for y in range(col):
                                    if (x,y) not in visited and self.grid[x][y] > 0: # if active and not visited
                                        # max(∣a−x∣,∣b−y∣)=1 check for neighbouring cells
                                        if max(abs(a-x), abs(b-y)) == 1:
                                            stack.append((x,y))
        return active_regions
                            
                    
                
        
           
grid = [[1,1,0,2],
        [1,1,0,0],
        [0,1,1,1],
        [0,0,1,1]]

st = State(grid)
print("The number of active regions is:", st.numRegions())
print(f'The Original state is : \n{st}')
print('\nThe next possible moves are : \n')
for next_state in st.moves():
    print(next_state)
    print()