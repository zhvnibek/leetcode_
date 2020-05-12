from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     x_lvl = -1
#     y_lvl = -2
#     x_prt = y_prt = None
#
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         def dfs(node: TreeNode, parent: Optional[TreeNode], x: int, y: int, lvl: int):
#             if node is None:
#                 return
#             if node.val == x:
#                 self.x_prt = parent
#                 self.x_lvl = lvl
#             elif node.val == y:
#                 self.y_prt = parent
#                 self.y_lvl = lvl
#             else:
#                 dfs(node=node.left, parent=node, x=x, y=y, lvl=lvl+1)
#                 dfs(node=node.right, parent=node, x=x, y=y, lvl=lvl+1)
#
#         dfs(node=root, parent=None, x=x, y=y, lvl=0)
#         return self.x_lvl == self.y_lvl and self.x_prt != self.y_prt

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_lvl = Solution.find_level(node=root, s=x)
        y_lvl = Solution.find_level(node=root, s=y)
        if x_lvl < 0 or y_lvl < 0:
            return False
        siblings = Solution.are_siblings(node=root, x=x, y=y)
        print(f'{x} is on level {x_lvl}\n{y} is on level {y_lvl}\nSiblings: {siblings}')
        return x_lvl == y_lvl and not siblings

    @staticmethod
    def are_siblings(node: TreeNode, x: int, y: int) -> bool:
        def _are_children_of(node: TreeNode, x: int, y: int):
            if node.left is None or node.right is None:
                return False
            return \
                node.left.val == x and node.right.val == y or \
                node.left.val == y and node.right.val == x

        return \
            _are_children_of(node=node, x=x, y=y) or \
            node.right is not None and Solution.are_siblings(node=node.right, x=x, y=y) or \
            node.left is not None and Solution.are_siblings(node=node.left, x=x, y=y)

    @staticmethod
    def find_level(node: TreeNode, s: int, cur_lvl: int = 0) -> int:
        if node is None:
            return -1
        if node.val == s:
            return cur_lvl

        lvl = Solution.find_level(node=node.left, s=s, cur_lvl=cur_lvl+1)
        if lvl > 0:
            return lvl
        return Solution.find_level(node=node.right, s=s, cur_lvl=cur_lvl + 1)

    def level_order(self, node: TreeNode):
        if node is None:
            return

        to_visit = [node]
        while to_visit:
            cur = to_visit.pop(0)
            print(cur.val   )

            if cur.left is not None:
                to_visit.append(cur.left)
            if cur.right is not None:
                to_visit.append(cur.right)


if __name__ == '__main__':
    """
               1
              2 3
            4 5 6 7   2^k --> 2^(k+1)-1
     """
    tree = TreeNode(1,
                    # TreeNode(2,
                    #          TreeNode(4),
                    #          TreeNode(5)
                    #          ),
                    TreeNode(2,
                             TreeNode(3,
                                      TreeNode(4),

                                      ),
                             TreeNode(5,
                                      None,
                                      TreeNode(6))
                             )
                    )
    first, second = 2, 3
    # print(Solution().level_order(node=tree))
    print(Solution().isCousins(root=tree, x=6, y=4))
