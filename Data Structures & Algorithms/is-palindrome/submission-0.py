class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first remove any spaces
        s_trimmed = s.replace(" ", "")

        # now we need to remove any non alpha numeric characters
        new_string = ""
        for i in s_trimmed:
            if i.isalnum() == True:
                new_string = new_string + i.lower()
        return new_string == new_string[::-1]
