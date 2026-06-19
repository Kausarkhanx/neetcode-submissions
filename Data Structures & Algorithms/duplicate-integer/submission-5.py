class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = set(nums)
        return len(nums)!=len(new_list)
        