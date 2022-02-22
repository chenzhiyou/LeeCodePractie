"""
单链表的实现
"""


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_tail(self, value):
        """
        先要判断是不是空链表，如果是空链表，先在头插入一个元素，如果不是空的，需要找到尾结点，然后再进行插入
        :param value: 要插入的元素
        :return:
        """
        if self.head is None:
            self.insert_to_head(value)
            return
        q = self.head
        """
        去寻找尾结点
        尾结点的特点：尾结点的下一个节点是None
        """
        while q.next is not None:
            q = q.next
        new_node = self.Node(value)
        q.next = new_node

    def insert_to_head(self, value):
        """
        插入到链表的头,需要先判断链表是不是空链表，如果是空的，让要插入的元素是第一个元素，如果不是，让新元素的
        下一个节点指向链表的头节点后，将新元素置为头节点
        :param value: 要插入的值
        :return:
        """
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_all(self):
        """
        打印链表
        :return:
        """
        if self.head is None:
            return
        q = self.head
        while q is not None:
            print(q.data)
            q = q.next

    def delete_by_value(self, value):
        """
        从链表中删除指定指
        :param value: 需要删除的数据
        :return:
        """
        if self.head is None:
            return False
        q = self.head
        p = None
        while q is not None and q.data != value:
            p = q
            q = q.next
        """
        当链表中没有value的时候，q为None
        """
        if q is None:
            return False
        """
        当head的值为value的时候，P会为None
        """
        if p is None:
            self.head = self.head.next
            return True
        else:
            p.next = q.next
            return True

    def find_by_value(self, value):
        """
        查询元素并返回
        :param value:要查找的元素
        :return:
        """
        if self.head is None:
            return None
        q = self.head
        while q is not None and q.data != value:
            q = q.next
        if q is None:
            return None
        else:
            return q

    def insert_after(self, node, value):
        """
        像指定元素后面插入元素
        :param node: 指定的元素
        :param value: 要插入的值
        :return:
        """
        if node is None:
            return
        q = self.find_by_value(node.data)
        new_node = self.Node(value)
        if q is None:
            """
            要判断一下 指定的节点是否存在
            """
            return False
        else:
            new_node.next = q.next
            q.next = new_node

    def insert_before(self, node, value):
        """
        在当前元素前插入元素
        :param node: 要在某个元素前插入节点
        :param value: 要插入的元素的值
        :return:
        """
        if self.head is None:
            self.insert_to_head(value)
        q = self.head
        p = None
        new_node = self.Node(value)
        while q is not None and q != node:
            p = q
            q = q.next
        if q is None:
            return None
        if p is None:
            new_node.next = self.head
        else:
            new_node.next = node
            p.next = new_node

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None


def test_link():
    link = SingleLinkedList()
    data = [1, 2, 5, 3, 1]
    for i in data:
        link.insert_tail(i)
    link.insert_to_head(99)
    print("*********************")
    link.print_all()
    link.delete_by_value(2)
    assert not link.delete_by_value(999)
    assert link.delete_by_value(99)
    print("*********************")
    link.print_all()
    assert link.find_by_value(2) is None
    new_node = link.find_by_value(3)
    print("*********************")
    print(new_node.data)
    link.insert_after(new_node, 10)
    print("*********************")
    print(link.find_by_value(3).next.data)
    assert link.find_by_value(3).next.data == 10
    link.insert_before(new_node, 30)
    assert link.find_by_value(5).next.data == 30
    print("*********************")
    link.print_all()


if __name__ == '__main__':
    test_link()
