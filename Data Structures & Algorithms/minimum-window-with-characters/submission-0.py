class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # stores how many of each character we NEED from t
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        # stores how many of each character are in our current window
        window = {}
        left = 0

        have = 0 # how many required characters currently have enough frequency
        need_count = len(need) # how many different required characters we need in total

        # store best answer
        result = ""
        min_length = float("inf")

        # expand window using right
        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1 # add current character to window

            # if this character is needed
            # and we now have exactly enough of it
            if char in need and window[char] == need[char]:
                have = have + 1

            # if we currently have everything we need
            # try shrinking window from the left
            while have == need_count:

                # current window length
                curr_length = right - left + 1

                # update shortest answer
                if curr_length < min_length:
                    min_length = curr_length
                    result = s[left:right + 1]

                # remove left character from window
                left_char = s[left]
                window[left_char] -= 1

                # if removing it means we no longer have enough
                # of a required character
                if left_char in need and window[left_char] < need[left_char]:
                    have = have - 1

                # shrink window
                left = left + 1

        return result