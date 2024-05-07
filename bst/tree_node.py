from __future__ import annotations
from dataclasses import dataclass, field
from idlelib.tree import TreeNode
from typing import Any


@dataclass
class TreeNode:
    value: Any
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)

    def __repr__(self) -> str:
        return f"{[self.left]}\t{[self.value]}\t{[self.right]}"

    def __lt__(self, other: TreeNode) -> bool:
        return self.value < other.value

    def __eq__(self, other: TreeNode) -> bool:
        return self.value == other.value

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


if __name__ == "__main__":
    tree = TreeNode(5)
    print(tree)
