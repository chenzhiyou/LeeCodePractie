class Queue:
    """
    优化队列
    """
    def __init__(self, capacity) -> None:
        self.n = capacity
        self.items = [-1]*capacity
        self.head = 0
        self.tail = 0

    """
    每次判断队列是否是空时：需要判断队尾是否=n且队头是否=0
    否则需要将队列整体前移，使得队头永远=0
    """
    def enqueue(self, item):
        if self.tail == self.n:
            if self.head == 0:
                return False
            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]
        self.tail -= self.head
        self.head = 0

    def dequeue(self):
        if self.head == self.tail:
            return None
        value = self.items[self.head]
        return value


def test_queue():
    a = Queue(4)
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    result = a.enqueue("40")
    assert not result
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[0] == "20"
    assert a.items[2] == "30"


if __name__ == "__main__":
    test_queue()
