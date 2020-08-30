# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root: TreeNode):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)if root is not None else []

    def kthSmallest_2(self, root: TreeNode, k: int) -> int:
        return self.inorder(root)[k-1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

if __name__ == '__main__':
    t_root = TreeNode(5,
                      TreeNode(3,
                               TreeNode(2,
                                        TreeNode(1)),
                               TreeNode(4)
                               ),
                      TreeNode(6)
                      )
    t = 4
    print(Solution().kthSmallest(root=t_root, k=t))
