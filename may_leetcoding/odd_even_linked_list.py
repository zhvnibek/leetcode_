

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        cur = self
        _s = f'{cur.val}-->'
        while cur.next is not None:
            cur = cur.next
            _s += f'{cur.val}-->'
        return _s + 'END'


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = even_head = head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

if __name__ == '__main__':
    node = ListNode(val=1,
                    next=ListNode(val=2,
                                  next=ListNode(val=3,
                                                next=ListNode(val=4,
                                                              next=ListNode(val=5,
                                                                            next=ListNode(val=6,
                                                                                          next=None))))))
    print(Solution().oddEvenList(head=node))
