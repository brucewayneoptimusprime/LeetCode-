import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))


            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if((nr in range(row)) and (nc in range(cols)) and grid[nr][nc] == "1" 
                    and ((nr,nc) not in visited)):
                        q.append((nr,nc))
                        visited.add((nr,nc))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands = islands + 1
        return islands



























        































        