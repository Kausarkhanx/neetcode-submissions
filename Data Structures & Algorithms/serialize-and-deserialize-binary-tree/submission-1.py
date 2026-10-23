class Codec:

    def serialize(self, root):
        values = []

        def dfs(node):
            if node == None:
                values.append("null")
                return None

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)


    def deserialize(self, data):
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if values[i] == "null":
                i=i+1
                return None

            node = TreeNode(int(values[i]))
            i=i+1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()