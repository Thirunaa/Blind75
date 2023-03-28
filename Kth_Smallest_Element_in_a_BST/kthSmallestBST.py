# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = 0
        self.k = k
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root or self.k <= 0:
            return

        self.inorder(root.left)
        self.k-=1
        if self.k == 0:
            self.result = root.val
        self.inorder(root.right)