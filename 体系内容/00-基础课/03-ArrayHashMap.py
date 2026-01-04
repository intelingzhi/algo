import random

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
class MyArrayHashMap:
    def __init__(self):
        # 存储key以及key的索引
        self.map = {}
        # 存储key-val Node
        self.arr = []

    def get(self, key):
        if key in self.map:
            index = self.map[key]
            return self.arr[index].val
        else:
            return None

    def put(self, key, val):
        if key in self.map:
            index = self.map[key]
            self.arr[index].val = val
        else:
            self.arr.append(Node(key, val))
            self.map[key] = len(self.arr) - 1

    def remove(self, key):
        if key in self.map:
            index = self.map[key]
            node = self.arr[index]

            e = self.arr[-1]
            self.arr[index] = e
            self.arr[-1] = node

            self.map[e.key] = index

            self.arr.pop()
            self.map.pop(node.key)

    def randomKey(self):
        n = len(self.arr)
        r_index = random.randint(0, n - 1)
        return self.arr[r_index].val

    def containKey(self, key):
        pass

    def size(self):
        return len(self.arr)


if __name__ == '__main__':
    map = MyArrayHashMap()
    map.put(1,1)
    map.put(2,2)
    map.put(3,3)
    map.put(4,4)
    map.put(5,5)
    print(map.get(1))
    print(map.randomKey())

    map.remove(2)
    print(map.randomKey())