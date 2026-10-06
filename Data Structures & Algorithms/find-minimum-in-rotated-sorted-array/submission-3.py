class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # binary search 
        left = 0
        right = len(nums)-1

        # we're finding the smallest item in the sorted array (must reside in left side)
        while left < right:
            mid = (left+right)//2
            
            # we know the right side has the smaller numbers due to the pattern shown
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid 
        return nums[left]