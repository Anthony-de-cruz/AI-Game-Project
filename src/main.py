#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, TBC, TBC)
@date:   03/10/2025

"""

import matplotlib.pyplot as plt


def main() -> None:
    print("Hello, world!")

    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Test Plot")
    plt.show()
    plt.savefig("plot.png")

if __name__ == "__main__":
    main()
