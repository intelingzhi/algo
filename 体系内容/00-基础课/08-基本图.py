from abc import ABC, abstractmethod
from typing import List, Tuple

class Graph(ABC):
    @abstractmethod
    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        pass

    @abstractmethod
    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        pass

    @abstractmethod
    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        pass

    @abstractmethod
    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        pass

    @abstractmethod
    def neighbors(self, v: int) -> List[Tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        pass

    @abstractmethod
    def size(self) -> int:
        # 返回节点总数
        pass



#===========================================
# 有向加权图（邻接表实现）
class WeightedDigraph:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        # 我们这里简单起见，建图时要传入节点总数，这其实可以优化
        # 比如把 graph 设置为 Map<Integer, List<Edge>>，就可以动态添加新节点了
        self.graph = [[] for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度 O(1)
    def addEdge(self, from_: int, to: int, weight: int):
        self.graph[from_].append(self.Edge(to, weight))

    # 删，删除一条有向边，复杂度 O(V)
    def removeEdge(self, from_: int, to: int):
        self.graph[from_] = [e for e in self.graph[from_] if e.to != to]

    # 查，判断两个节点是否相邻，复杂度 O(V)
    def hasEdge(self, from_: int, to: int) -> bool:
        for e in self.graph[from_]:
            if e.to == to:
                return True
        return False

    # 查，返回一条边的权重，复杂度 O(V)
    def weight(self, from_: int, to: int) -> int:
        for e in self.graph[from_]:
            if e.to == to:
                return e.weight
        raise ValueError("No such edge")
    
    # 查，返回某个节点的所有邻居节点，复杂度 O(1)
    def neighbors(self, v: int):
        return self.graph[v]
    

#=========================================
# 有向加权图（邻接矩阵实现）
class WeightedDigraph:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to, weight):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        # 邻接矩阵，matrix[from][to] 存储从节点 from 到节点 to 的边的权重
        # 0 表示没有连接
        self.matrix = [[0] * n for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度 O(1)
    def addEdge(self, from_node, to, weight):
        self.matrix[from_node][to] = weight

    # 删，删除一条有向边，复杂度 O(1)
    def removeEdge(self, from_node, to):
        self.matrix[from_node][to] = 0

    # 查，判断两个节点是否相邻，复杂度 O(1)
    def hasEdge(self, from_node, to):
        return self.matrix[from_node][to] != 0

    # 查，返回一条边的权重，复杂度 O(1)
    def weight(self, from_node, to):
        return self.matrix[from_node][to]

    # 查，返回某个节点的所有邻居节点，复杂度 O(V)
    def neighbors(self, v):
        res = []
        for i in range(len(self.matrix[v])):
            if self.matrix[v][i] != 0:
                res.append(self.Edge(i, self.matrix[v][i]))
        return res
    

#=========================================
# 有向无权图（邻接表/邻接矩阵实现）
# 复用上面的实现即可，把权重参数都设为 1

#=========================================
# 无向加权图（邻接表/邻接矩阵实现）
# 无向加权图就等同于双向的有向加权图，所以直接复用上面用邻接表/领接矩阵实现的 WeightedDigraph 类就行了，只是在增加边的时候，要同时添加两条边：

    # 增，添加一条带权重的无向边
def addEdge(self, frm, to, weight):
    self.graph.addEdge(frm, to, weight)
    self.graph.addEdge(to, frm, weight)

    # 删，删除一条无向边
def removeEdge(self, frm, to):
    self.graph.removeEdge(frm, to)
    self.graph.removeEdge(to, frm)

