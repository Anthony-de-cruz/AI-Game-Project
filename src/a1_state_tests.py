#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, TBC)
@date:   12/10/2025

"""

import unittest

from a1_state import State

class TestA1(unittest.TestCase):
    def test_numHingers(self):
        """"""

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
        """"""

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

if __name__ == '__main__':
    unittest.main()
