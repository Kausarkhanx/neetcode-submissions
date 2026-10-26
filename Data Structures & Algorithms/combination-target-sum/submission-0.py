class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, current, total):

            # found a valid combination
            if total == target:
                result.append(current.copy())
                return None

            # too big, stop this path
            if total > target:
                return None

            # try all choices
            for i in range(start, len(nums)):

                # choose
                current.append(nums[i])

                # explore
                backtrack(i, current, total + nums[i])

                # undo
                current.pop()

            return None

        backtrack(0, [], 0)

        return result