import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set() #Since it is a set, it can work with add function and not append
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row , col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if ((nr) in range(rows) and (nc) in range(cols)
                        and grid[nr][nc] == "1" and (nr, nc) not in visited ):
                        q.append((nr,nc))
                        visited.add((nr,nc))



        # As a child you must have when though about the questions must have looked first of starting
        # from top left position and then move on to look for places where other ones are. So, in finality
        # we will search the entire grid in search of 1's and 0's and islands. So, a simple double for loop

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)  #This is to check the neighbours of (R,C) and see truly how many in 1 island
                    islands = islands + 1
        return islands

        

        