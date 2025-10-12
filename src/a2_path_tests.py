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
from a2_path import path_DFS

test_valid_1 = (
    State([[1,1,0,1],
           [1,2,0,0],
           [0,0,2,1],
           [0,0,1,1]]),
    State([[1,1,0,0],
           [1,2,0,0],
           [0,0,2,0],
           [0,0,1,0]]))

test_valid_2 = (
    State([[1,1,0,1],
           [1,2,0,0],
           [0,0,2,1],
           [0,0,1,1]]),
    State([[0,0,0,1],
           [1,2,0,0],
           [0,0,2,1],
           [0,0,0,0]]))

test_invalid_1 = (
    State([[1,1,0,1],
           [1,2,0,0],
           [0,0,2,1],
           [0,0,1,1]]),
    State([[1,1,0,1],
           [1,2,0,0],
           [0,0,0,1],
           [0,0,1,1]]))

test_invalid_2 = (
    State([[1,1,0,1],
           [1,2,0,0],
           [0,0,2,1],
           [0,0,1,1]]),
    State([[1,1,0,1],
           [1,0,0,0],
           [0,0,2,1],
           [0,0,1,1]]))

class TestA2(unittest.TestCase):
    def test_path_DFS(self):
        """"""

        self.assertNotEqual(path_DFS(test_valid_1[0], test_valid_1[1]), None)
        self.assertNotEqual(path_DFS(test_valid_2[0], test_valid_2[1]), None)

        self.assertEqual(path_DFS(test_invalid_1[0], test_invalid_1[1]), None)
        self.assertEqual(path_DFS(test_invalid_2[0], test_invalid_2[1]), None)

if __name__ == '__main__':
        unittest.main()
