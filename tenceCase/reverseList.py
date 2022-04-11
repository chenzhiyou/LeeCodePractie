class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverse_list(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            curr.next = prev
            prev = curr
            curr = curr.next
        return prev


if __name__ == "__main__":
    list = Solution()
    data = [1, 2, 3, 4, 5]
    reverse_head = list.reverse_list(data)
    print(reverse_head)
