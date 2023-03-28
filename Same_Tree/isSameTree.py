# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, root, subRoot):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right))

        return False