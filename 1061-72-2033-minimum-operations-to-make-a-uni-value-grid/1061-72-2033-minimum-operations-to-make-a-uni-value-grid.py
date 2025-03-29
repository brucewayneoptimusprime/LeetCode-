class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [item for row in grid for item in row]

        remainder = flattened[0] % x

        for nums in flattened:
            if nums % x != remainder:
                return -1
        
        flattened_new =[]
        for num in flattened:
            new_num = (num - remainder) // x
            flattened_new.append(new_num)
        flattened = flattened_new

        flattened.sort()
        median = flattened[len(flattened) // 2]

        operations = 0

        for num in flattened:
            difference = abs(num - median)
            operations = operations + difference
        return operations
        

        
        