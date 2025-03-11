# # 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Explanation:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import deque
        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            li = []
            for i in range (n):
                node = q.popleft()
                li.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(li[-1])
        return ans


        