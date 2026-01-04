class MyLinkedHashMap:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()  # kv对

    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key].val
    
    def put(self, key, val):
        if key not in self.map:
            node = self.Node(key, val)
            self.add_last_node(node)
            self.map[key] = node
            return
        
        # 若key存在
        self.map[key].val = val

    def remove(self, key):
        if key not in self.map:
            return
        
        node = self.map[key]
        del self.map[key]  # 从字典中删除
        self.remove_node(node)

    def contains_key(self, key):
        return key in self.map
    
    def keys(self):
        key_list = []
        p = self.head.next
        while p != self.tail:
            key_list.append(p.key)
            p = p.next

        return key_list
    
    def add_last_node(self, x):

        # 要修改3个node的信息
        # 第一个node：插入前的倒数第一个有效node
        last_final_node = self.tail.prev
        # 第二个node：插入前的tail
        # 第三个node：当前插入的node

        # 修改x的左右
        x.next = self.tail
        x.prev = last_final_node

        # 修改last的右
        last_final_node.next = x
        # 修改tail的左
        self.tail.prev = x

    
    def remove_node(self, x):
        # 取x的左右
        prev = x.prev
        next = x.next
        # 将上一个的右拼接
        prev.next = next
        # 将下一个的左拼接
        next.prev = prev

        # 删除
        x.next = x.prev = None


if __name__ == '__main__':
    map = MyLinkedHashMap()
    map.put("a", 1)
    map.put("b", 2)
    map.put("c", 3)
    map.put("d", 4)
    map.put("e", 5)

    print(map.keys())  # ['a', 'b', 'c', 'd', 'e']
    map.remove("c")
    print(map.keys())  # ['a', 'b', 'd', 'e']

    