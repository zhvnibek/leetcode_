#  https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solution/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def paths(self, root: TreeNode, path: list, path_len: int = 0):
        if root is None:
            return
        if len(path) > path_len:
            path[path_len] = root.val
            path = path[:path_len+1]
        else:
            path.append(root.val)
        if root.left is None and root.right is None:
            yield path
        else:
            yield from self.paths(root=root.left, path=path, path_len=path_len+1)
            yield from self.paths(root=root.right, path=path, path_len=path_len+1)

    def read_binary(self, path: list) -> int:
        deg = len(path) - 1
        res = 0
        for b in path:
            res += b << deg
            deg -= 1
        print(res)
        return res

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return sum([self.read_binary(path=path) for path in self.paths(root=root, path=[])])


if __name__ == '__main__':
    tree = TreeNode(0,
                    TreeNode(1,
                             TreeNode(0)
                             ),
                    TreeNode(0,
                             TreeNode(0, TreeNode(0, None, TreeNode(1, None, TreeNode(1)))),
                             TreeNode(0)
                             )
                    )

    print(Solution().sumRootToLeaf(root=tree))
