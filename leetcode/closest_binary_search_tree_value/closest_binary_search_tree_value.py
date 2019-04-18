# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        def find_closest_value(root, target):
            if not root:
                return float('inf')

            left_closest_value = find_closest_value(root.left, target)
            right_closest_value = find_closest_value(root.right, target)

            # Chose children closest value
            if abs(left_closest_value - target) <= abs(right_closest_value - target):
                min_closest_value = left_closest_value
            else:
                min_closest_value = right_closest_value

            # Compare children closest value with current node value to calculate current closest value
            if abs(root.val - target) <= abs(min_closest_value - target):
                current_closest_value = root.val
            else:
                current_closest_value = min_closest_value

            return current_closest_value

        return find_closest_value(root, target)