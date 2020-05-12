

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root

    def height(self, node: TreeNode):
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)
            return l_height + 1 if l_height > r_height else r_height + 1

    def contains_one(self, node: TreeNode) -> bool:
        if node is None:
            return False
        if node.val == 1:
            return True
        return self.contains_one(node.left) or self.contains_one(node.right)

    def print_bft(self, root: TreeNode) -> None:
        def print_level(node: TreeNode, level: int) -> None:
            if node is None:
                print('null->', end='')
                return
            if level == 1:
                print(str(node.val) + '->', end='')
            elif level > 1:
                print_level(node.left, level - 1)
                print_level(node.right, level - 1)

        h = self.height(root)
        for i in range(1, h + 1):
            print_level(root, i)
        print('\n')

    def print_inorder(self, root: TreeNode) -> None:
        pass

    def print_preorder(self, root: TreeNode) -> None:
        pass

    def print_postorder(self, root: TreeNode) -> None:
        pass

if __name__ == '__main__':
    s = Solution()
    a = r = TreeNode(1)
    b = r.left = TreeNode(0)
    c = r.right = TreeNode(1)
    d = r.left.left = TreeNode(0)
    e = r.left.right = TreeNode(0)
    f = r.right.left = TreeNode(0)
    g = r.right.right = TreeNode(1)
    s.print_bft(r)
    # h = s.height(r)
    # print(h)
    ans = s.pruneTree(r)
    s.print_bft(ans)

