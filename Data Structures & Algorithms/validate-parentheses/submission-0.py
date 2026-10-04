class Solution:
    def isValid(self, s: str) -> bool:

        # create a dictionary
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }

        stack = []
        for i in s:
            if i in pairs:
                # opener -> add it to the stack
                stack.append(i)
            else:
                # closer -> if nothing is open, there's nothing to close
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if pairs[top] != i:
                    return False

        # valid only if every opener was closed
        if len(stack) == 0:
            return True
        else:
            return False