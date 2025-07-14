class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #I must create a new data structure of Set named seen
        seen = set()
        particle1 = 0
        particle2 = 0
        n = (len(grid))
        max_length = n * n

        #Now, i must iterate through the grid
        for row in grid:
            for x in row:
                if x in seen:
                    particle1 = x
                seen.add(x)
            
        for i in range(1, (max_length)+1):
            if i not in seen:
                particle2 = i
                break

                
        return [particle1, particle2]
            

        

        