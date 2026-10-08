class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict = {}
        longest = 0

        for right in range(len(s)):

            # add current character to frequency dictionary
            dict[s[right]] = dict.get(s[right], 0) + 1

            # if window needs too many replacements, shrink it
            while (right - left + 1) - max(dict.values()) > k:
                dict[s[left]] = dict[s[left]] - 1
                left = left+1

            # update longest valid window
            longest = max(longest, right - left + 1)

        return longest