class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find the #
            length = int(s[i:j])         # number before it = word length
            words.append(s[j + 1 : j + 1 + length])   # grab the word
            i = j + 1 + length           # jump to next number
        return words