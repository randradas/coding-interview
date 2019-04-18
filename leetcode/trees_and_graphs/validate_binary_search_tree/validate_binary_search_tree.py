# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, less_than=float('inf'), larger_than=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        elif root.val >= less_than or root.val <= larger_than:
            return False
        else:
            return self.isValidBST(root.left, less_than=min(root.val, less_than), larger_than=larger_than) and \
                   self.isValidBST(root.right, less_than=less_than, larger_than=max(root.val, larger_than))