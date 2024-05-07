from __future__ import annotations
from bst.tree_node import TreeNode


class BST:
    """A basic binary search tree, this is not great because tree can become unbalanced."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int | float | str) -> None:
        node = self.root
        if node is None:  # base case (no root)
            self.root = TreeNode(value)
            return

        else:  # if we need to move down the tree
            while node:
                if value < node.value:  # move down left branch
                    if node.left is None:
                        node.left = TreeNode(value)
                        return
                    else:
                        node = node.left

                if value > node.value:  # move down right branch
                    if node.right is None:
                        node.right = TreeNode(value)
                        return
                    else:
                        node = node.right

    def delete(self, value: int | float | str) -> None:
        raise NotImplementedError
