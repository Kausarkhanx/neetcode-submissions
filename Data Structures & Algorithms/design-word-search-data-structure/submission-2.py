class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def addWord(self, word: str) -> None:
        current = self

        for char in word:
            if char not in current.children:
                current.children[char] = WordDictionary()

            current = current.children[char]

        current.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(index, current):

            if index == len(word):
                return current.end_of_word

            char = word[index]

            if char == ".":
                for child in current.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if char not in current.children:
                return False

            return dfs(index + 1, current.children[char])

        return dfs(0, self)