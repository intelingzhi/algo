# 环形数组
class CycleArray:
    def __init__(self, size = 1):
        self.size = size
        self.arr = [None] * size

        # 左开右闭
        self.start = 0
        self.end = 0

        self.count = 0


    def is_full(self):
        return self.count == self.size

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0


    #######################################################
    def resize(self, newSize):
        new_arr = [None] * newSize
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start + i) % self.size]

        self.arr = new_arr
        self.start = 0
        self.end = self.count
        self.size = newSize

    # 在头部添加元素
    def add_first(self, arr, val):
        if self.is_full():
            self.resize(self.size * 2)

        # 把start左移动1位，再赋值
        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1


    def remove_first(self):
        # 先赋值，再右移
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1


    # 尾部添加元素
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)

        # 先赋值，再右移
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    # 尾部删除元素
    def remove_last(self):
        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1

    # 获取数组头部元素，时间复杂度 O(1)
    def get_first(self):
        return self.arr[self.start]

    # 获取数组尾部元素，时间复杂度 O(1)
    def get_last(self):
        # end 是开区间，指向的是下一个元素的位置，所以要减 1
        return self.arr[(self.end - 1 + self.size) % self.size]