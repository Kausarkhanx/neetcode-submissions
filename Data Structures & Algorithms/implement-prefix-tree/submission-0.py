class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def insert(self, word: str) -> None:
        current = self

        for i in word:
            if i not in current.children:
                current.children[i] = PrefixTree()
            current = current.children[i]
        current.end_of_word = True
        

    def search(self, word: str) -> bool:
        current = self
        
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        return current.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        current = self

        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        return True

        
        