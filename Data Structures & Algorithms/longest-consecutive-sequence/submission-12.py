class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        biggest = 0

        for num in num_set:
            # only start counting at the beginning of a run
            if num - 1 not in num_set:
                sum = 1
                current = num

                # count upwards while the next number exists
                while current + 1 in num_set:
                    current = current + 1
                    sum = sum + 1

                if sum > biggest:
                    biggest = sum

        return biggest