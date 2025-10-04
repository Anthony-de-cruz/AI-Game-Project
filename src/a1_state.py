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
    size = 5
    
    def __init__(self,grid):
        '''
        Parameters
        ----------
        grid : 2D List of lists

        '''
        
        # Check for error with assert
        assert(len(grid) == State.size)
        self.grid = grid
        
    def __str__(self):
        return self.grid