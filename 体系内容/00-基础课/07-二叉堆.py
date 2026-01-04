# 简化版优先级队列

class SimpleMinPQ:
    # 容量为 cap 的优先级队列
    def __init__(self, cap):
        self.heap = [0] * cap
        self.size = 0

    def parent(self, node):
        return (node - 1) // 2
    
    def left(self, node):
        return node * 2 + 1
    
    def right(self, node):
        return node * 2 + 2
    
    # 交换两个数（只需要交换数组的值即可）
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        return self.heap[0]

    def push(self, x):
        # 新元素追加到末尾
        self.heap[self.size] = x
        # 上浮
        self.swim(self.size)
        self.size += 1

    # 推出堆顶元素，时间复杂度 O(logn)
    def pop(self):
        result = self.heap[0]
        # 把堆顶元素放到堆顶
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1

        # 下沉
        self.sink(0)
        return result
    

    def swim(self, node):
        pNode = self.parent(node)
        while node > 0 and self.heap[pNode] > self.heap[node]:
            self.swap(pNode, node)
            node = pNode

    def sink(self, node):
        # 确保找左右节点不超出范围
        while self.left(node) < self.size or self.right(node) < self.size:
            min_node = node
            leftIndex = self.left(node)
            rightIndex = self.right(node)

            if leftIndex < self.size:
                if self.heap[leftIndex] < self.heap[min_node]:
                    min_node = leftIndex

            if rightIndex < self.size:
                if self.heap[rightIndex] < self.heap[min_node]:
                    min_node = rightIndex

            if min_node == node:
                break
            else:
                self.swap(node, min_node)
                node = min_node


class MyPriorityQueue:
    def __init__(self, capacity, comparator = None):
        # 堆数组
        self.heap = [None] * capacity

        # 堆中元素的数目
        self.size = 0

        # 元素比较
        if comparator is not None:
            self.comparator = comparator  
        else:
            self.comparator = lambda x, y: (x > y) - (x < y)

    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def parent(self, node):
        return (node - 1) // 2
    
    def left(self, node):
        return node * 2 + 1
    
    def right(self, node):
        return node * 2 + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        
        return self.heap[0]
    
    def push(self, x):
        if self.size == len(self.heap):
            self.resize(2 * len(self.heap))

        self.heap[self.size] = x
        self.swim(self.size)
        self.size += 1


    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        
        res = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap[self.size - 1] = None
        self.size -= 1

        self.sink(0)

        return res

    def swim(self, i_node):
        
        while i_node > 0:
            i_pnode = self.parent(i_node)
            if self.comparator(self.heap[i_pnode], self.heap[i_node]) > 0:
                self.swap(i_pnode, i_node)
                i_node = i_pnode
            # 头小于左右
            else:
                break

    def sink(self, h_node):
        # 不检查右边，因为左小于右
        while self.left(h_node) < self.size:
            min_node = h_node

            l_hnode = self.left(h_node)
            r_hnode = self.right(h_node)
            if l_hnode < self.size and self.comparator(self.heap[l_hnode], self.heap[min_node]) < 0:
                min_node = l_hnode
            if r_hnode < self.size and self.comparator(self.heap[r_hnode], self.heap[min_node]) < 0:
                min_node = r_hnode

            if min_node == h_node:
                break

            self.swap(h_node, min_node)
            h_node = min_node


        # 调整堆的大小
    def resize(self, capacity):
        assert capacity >= self.size
        new_heap = [None] * capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap


# pq = SimpleMinPQ(10)
# pq.push(3)
# pq.push(2)
# pq.push(1)
# pq.push(5)
# pq.push(4)

# print(pq.pop()) # 1
# print(pq.pop()) # 2
# print(pq.pop()) # 3
# print(pq.pop()) # 4
# print(pq.pop()) # 5



# 小顶堆
pq = MyPriorityQueue(3, comparator=lambda x, y: (x > y) - (x < y))
pq.push(3)
pq.push(1)
pq.push(4)
pq.push(1)
pq.push(5)
pq.push(9)

# 1 1 3 4 5 9
while not pq.is_empty():
    print(pq.pop())