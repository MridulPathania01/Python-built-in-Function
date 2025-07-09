# Question :- Need to find nearest left node of target in same level else return null

# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPrevNodeAtSameLevel(self, root: Optional[TreeNode], target: int) -> str:
        levels = []
        def dfs(node, level):
            if not node:
                return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        for level in levels:
            for i in range(len(level)):
                if level[i] == target:
                    if i == 0:
                        return "Null"
                    else:
                        return str(level[i - 1])
        return None