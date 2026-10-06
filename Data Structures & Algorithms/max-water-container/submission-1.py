class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # consider 2 pointer approach

        left = 0
        right = len(heights)-1
        best_area = 0

        while left<right:
            width = right-left
            height = min(heights[right], heights[left])
            curr_area = width*height
            best_area = max(best_area, curr_area)

            if heights[left]<heights[right]:
                left = left+1
            else:
                right = right-1
                
        return best_area
        
        