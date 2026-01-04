class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 遍历递归一棵二叉树
def traverse(root):
    if root is None:
        return
    
    traverse(root.left)
    traverse(root.right)

# 3种层次遍历的方法
from collections import deque 
def levelOrderTraverse(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)

    while q:
        cur = q.popleft()
        print(cur.val)

        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)


def level2(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)
    depth = 1

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"depth={depth}, val={cur.val}")

            # 加入队列
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)

        depth += 1

    return

class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

    
def level3(root):
    if root is None:
        return
    
    q = deque()
    q.append(State(root, 1))

    while q:
        cur = q.popleft()
        print(f"depth={cur.depth}, val={cur.val}")

        if cur.left is not None:
            q.append(cur.node.left, cur.depth + 1)
        if cur.right is not None:
            q.append(cur.node.right, cur.depth + 1)



