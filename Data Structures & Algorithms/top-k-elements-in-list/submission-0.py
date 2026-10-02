from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter_dictionary = Counter(nums)

        # k gives u the most common numbers. for example, if k is 5 we get the 5 most common numbers
        most_common_element = counter_dictionary.most_common(k)

        return [num for num, count in most_common_element]
        