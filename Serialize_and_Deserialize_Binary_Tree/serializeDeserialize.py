# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("null")


        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        i = 0
        q = deque()
        root = TreeNode(int(data[0]))
        q.append(root)
        i+=1
        while q:
            node = q.popleft()
            #left
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i+=1

            #right
            if data[i] != "null":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i+=1

        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))