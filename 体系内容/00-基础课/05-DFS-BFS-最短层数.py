# 2种dfs输出最短路径
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFS01:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 1

        while q:
            sz = len(q)

            for i in range(sz):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return depth

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            
            depth += 1

        return 99999
    

class DFS:
    def __init__(self):
        # 记录最小深度
        self.minDepthValue = float('inf')
        # 当前遍历到的层数
        self.curDepth = 0

    def minDepth(self, root):
        if root is None:
            return 0
        self.traverse(self, root)
        return self.minDepthValue
    

    def traverse(self, root):
        if root is None:
            return
        
        self.curDepth += 1

        # 叶子节点，更新最小深度
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.curDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.curDepth -= 1

