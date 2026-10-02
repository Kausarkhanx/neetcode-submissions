from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for i in strs:

            key = "".join(sorted(i))

            # the key is key which we pass in the [] and the value is the append
            anagram_dict[key].append(i)
        
        return list(anagram_dict.values())
        
