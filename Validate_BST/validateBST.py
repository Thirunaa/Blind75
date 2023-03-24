# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.li = []
        self.prev = float("-inf")
        self.flag = True
        self.inorder(root)
               
        return self.flag

    def inorder(self,root):
        if root==None or not self.flag:
            return

        self.inorder(root.left)
        
        if root.val<=self.prev:
            self.flag = False
        self.prev = root.val

        self.inorder(root.right)