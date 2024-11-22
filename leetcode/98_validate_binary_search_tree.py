# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class SolutionInorder(object):
    def inorder(self, node, output) -> None:
        if node is None:
            return

        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        output = []

        self.inorder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True
