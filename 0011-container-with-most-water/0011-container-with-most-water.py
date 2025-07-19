class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        result_Area = 0

        while l < r:
            area = abs(l - r) * (min(height[l], height[r]))
            result_Area = max(result_Area, area)

            if height[l] < height[r]:
                l = l + 1
            elif height[r] < height[l]:
                r = r - 1
            else:
                l = l + 1
            
            

        return result_Area
        