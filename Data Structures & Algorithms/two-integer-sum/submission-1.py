class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h_map:
                return[h_map[diff], i]
            else:
                h_map[nums[i]]=i
        