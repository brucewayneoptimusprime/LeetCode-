class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            for i in range(left,right):
                result.append(matrix[top][i])
                #covering the top layer
            top = top + 1

            #covering coming down
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right = right - 1

            if not (left < right and top < bottom):
                break
                
            #covering right to left
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom = bottom - 1
                
            #Covering going up
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left = left + 1
        return result

            
               



                

        