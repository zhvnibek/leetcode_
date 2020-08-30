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
    def insertionSortList(self, head: ListNode) -> ListNode:
        i = 0
        cur = head
        while cur is not None:
            key = ListNode(cur.val)
            print(f'Key: {key.val}')
            shift = head
            while shift is not None and shift.val < key.val:
                shift = shift.next
                print(f'shift: {shift}')
            # shift.next = key
            # key.next = shift.next.next

            cur = cur.next

        return head


if __name__ == '__main__':
    s = Solution()
    _list = [-1, 5, 3, 4, 0]
    a = ListNode(-1)
    a.next = b = ListNode(5)
    b.next = c = ListNode(3)
    c.next = d = ListNode(4)
    d.next = e = ListNode(0)
    _sorted = s.insertionSortList(a)
    print(_sorted)
