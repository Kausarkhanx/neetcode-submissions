class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 2 pointer approach
        left = 0
        right = len(s)-1

        # here we're returning true or false ultimately -> so no need to add a 3rd initialiser

        while left < right:
            # put conditions or stuff to calculate
            # here we need to check for conditions 

            # we check if the item is an alpha-num -> if not -> then we move on

            if not s[left].isalnum():
                left = left + 1
            elif not s[right].isalnum():
                right = right - 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left = left + 1
                right = right -1
        
        return True


        