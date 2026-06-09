class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i in range(len(nums)):
            h_map[nums[i]]=i # key = value (index)
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h_map and h_map[diff]!=i:
                return[i, h_map[diff]]
        


        