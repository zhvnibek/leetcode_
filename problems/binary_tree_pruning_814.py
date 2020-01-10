

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        pass

    def height(self, node: TreeNode):
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)
            return l_height + 1 if l_height > r_height else r_height + 1

    def print_bft(self, root: TreeNode) -> None:
        def print_level(node: TreeNode, l: int) -> None:
            if node is None:
                return
            if l == 1:
                print(node.val)
            elif l > 1:
                print_level(node.left, l - 1)
                print_level(node.right, l - 1)

        h = self.height(root)
        for i in range(1, h + 1):
            print_level(root, i)

    def print_inorder(self, root: TreeNode) -> None:
        pass

    def print_preorder(self, root: TreeNode) -> None:
        pass

    def print_postorder(self, root: TreeNode) -> None:
        pass

if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.right.left = TreeNode(6)
    r.right.right = TreeNode(7)
    s.print_bft(r)
    # h = s.height(r)
    # print(h)
    # ans = s.pruneTree(r)
    # print(ans)
