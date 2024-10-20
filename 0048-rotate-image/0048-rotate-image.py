class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left): 

                top = left
                bottom = right

                temp_top_left = matrix[top][left + i]

                #Anticlockwise 1st step

                matrix[top][left + i] = matrix[bottom - i][left]

                #2nd Step

                matrix[bottom - i][left] = matrix[bottom][right - i]

                #3rd Step

                matrix[bottom][right - i] = matrix[top + i][right]

                #4th final assigment 

                matrix[top + i][right] = temp_top_left

            left = left + 1
            right = right - 1
        
                 
            




            
        
        