#!/bin/python3

import sys

def gridChallenge(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    grid[0] = sorted(grid[0])
    for i in range(1,n):
        grid[i] = sorted(grid[i])
        for j in range(m):
            if grid[i-1][j] > grid[i][j]:
                return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(grid_t)
        result = gridChallenge(grid)
        print(result)
