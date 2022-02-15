class Array:
    def __init__(self, capacity) -> None:
        self.data = [-1]*capacity
        # 记录存了多少数据
        self.count = 0
        # 数组容量
        self.n = capacity

    def insert(self, location, value):
        if self.n == self.count:
            return False
        # 如果插入的位置不正确,且插入的位置，必须是连续的
        if location < 0 or location > self.count:
            return False

        # 循环
        for i in range(self.count, location, -1):
            self.data[i] = self.data[i - 1]

        self.data[location] = value
        self.count += 1
        return True

    def find(self, location):
        if location < 0:
            return -1
        if location >= self.count:
            return -1
        data = self.data[location]
        return data

    def delete(self, location):
        if location < 0:
            return False
        if location >= self.count:
            return False
        for i in range(location+1, self.count):
            self.data[i-1] = self.data[i]
        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()
