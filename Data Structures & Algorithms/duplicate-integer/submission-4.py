class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)
        return len(nums)!=len(new_set)
        