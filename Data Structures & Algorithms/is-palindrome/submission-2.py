class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first remove any spaces
        s_trimmed = s.replace(" ", "")

        # now we need to remove any non alpha numeric characters to actually do the problem
        new_string = ""
        for i in s_trimmed:
            if i.isalnum() == True:
                new_string = new_string + i.lower() # convert to lower case to match strings
        return new_string == new_string[::-1]
