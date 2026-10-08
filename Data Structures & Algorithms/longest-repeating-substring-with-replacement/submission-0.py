class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        longest = 0

        for right in range(len(s)):

            # add current character to frequency dictionary
            count[s[right]] = count.get(s[right], 0) + 1

            # if window needs too many replacements, shrink it
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # update longest valid window
            longest = max(longest, right - left + 1)

        return longest