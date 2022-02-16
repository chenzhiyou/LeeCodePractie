class Queue:
    def __init__(self, capacity) -> None:
        self.n = capacity
        self.items = [-1]*capacity
        self.head = 0
        self.tail = 0

    # 入队
    def enqueue(self, item):
        if self.tail == self.n:
            return False
        self.items[self.tail] = item
        self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            return False
        value = self.items[self.head]
        self.head += 1
        return value


def test_queue():
    a = Queue(10)
    a.enqueue("10")
    a.enqueue("20")
    deque_time = a.dequeue()
    assert deque_time == "10"
    a.enqueue("30")
    assert a.items[a.head] == "20"
    assert a.items[a.tail - 1] == "30"


if __name__ == "__main__":
    test_queue()
