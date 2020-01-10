# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __len__(self):
        n = 1
        cur_node = self
        while cur_node.next is not None:
            n += 1
            cur_node = cur_node.next
        return n

    def __str__(self):
        _str = ''
        cur_node = self
        while cur_node is not None:
            _str += f"{cur_node.val}" + "->"
            cur_node = cur_node.next
        return _str + 'NULL'


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head
        n = 1  # len
        cur_node = head
        while cur_node.next is not None:
            n += 1
            cur_node = cur_node.next
        if k == 0 or k % n == 0:
            return head  # no rotation
        a = head
        b = head
        for _ in range(k % n):
            a = a.next
        while a.next is not None:
            a = a.next
            b = b.next
        head, a.next, b.next = b.next, head, None
        return head


if __name__ == '__main__':
    s = Solution()
    h = ListNode(0)
    h.next = ListNode(1)
    h.next.next = ListNode(2)
    h.next.next.next = ListNode(3)

    k = 2
    print(s.rotateRight(h, k))
