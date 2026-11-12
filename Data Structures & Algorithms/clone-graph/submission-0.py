class Solution:
    def cloneGraph(self, node):

        # empty graph
        if node is None:
            return None

        # stores: original node -> copied node
        copies = {}

        def dfs(node):

            # if we already copied this node,
            # just return the copy
            if node in copies:
                return copies[node]

            # make a new copy of this node
            copy = Node(node.val)

            # save it so we don't copy it again
            copies[node] = copy

            # copy all of its neighbours
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))

            # return the copied node
            return copy

        # start cloning from the first node
        return dfs(node)


        