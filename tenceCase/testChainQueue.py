"""
链式队列不需要指定大小，可以无限的增大，链式队列，入队一定是成功的。
"""


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """
        判断是否是第一个节点，如果是，需要初始化定义
        :param item:
        :return:
        """
        if self.tail is None:
            new_node = self.Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next

    def dequeue(self):
        """
        出队操作
        :return:
        """
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None


def test_queue():
    a = Queue()
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    deque_item = a.dequeue()
    assert deque_item == "10"
    assert a.head.data == "20"
    assert a.head.next.data == "30"


if __name__ == "__main__":
    test_queue()