"""
Given a binary tree,
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Assume perfect binary tree and try to solve this in constant extra space.
"""


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        def helper(root):
            if root.left is None: return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            helper(root.left)
            helper(root.right)
        helper(root)
        return root