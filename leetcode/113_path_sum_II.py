"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths
where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root is None: return None
            targetSum -= root.val
            path.append(root.val)
            if root.left is None and root.right is None:
                if targetSum == 0:
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans
