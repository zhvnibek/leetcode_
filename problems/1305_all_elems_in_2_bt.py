from typing import List
from itertools import chain
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         def inorder(root: TreeNode):
#             if root:
#                 yield from inorder(root.left)
#                 yield root.val
#                 yield from inorder(root.right)
#
#         res = []
#         g1 = deque(inorder(root1))
#         g2 = deque(inorder(root2))
#         while g1 and g2:
#             res.append(g1.popleft() if g1[0] < g2[0] else g2.popleft())
#
#         return res + list(g1) + list(g2)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root: TreeNode):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)

        def merger(g1, g2):
            a = next(g1, None)
            b = next(g2, None)
            if a is None and b is not None:
                yield b
                yield from g2
            elif b is None and a is not None:
                yield a
                yield from g1
            elif a < b:
                yield a
                yield from merger(g1=g1, g2=chain([b], g2))
            else:
                yield b
                yield from merger(g1=chain([a], g1), g2=g2)

        return list(merger(g1=inorder(root=root1), g2=inorder(root=root2)))


if __name__ == '__main__':
    t = TreeNode(2, TreeNode(1), TreeNode(4))
    s = TreeNode(1, TreeNode(0), TreeNode(3))
    print(Solution().getAllElements(root1=t, root2=s))
