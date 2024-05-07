from bst.tree_node import TreeNode


def test_tree_node_trivial():
    root = TreeNode(value=5)
    assert root.value == 5
    assert root.left is None
    assert root.right is None


def test_tree_node_with_children():
    root = TreeNode(value=5)
    left_child = TreeNode(value=3)
    right_child = TreeNode(value=7)

    root.left = left_child
    root.right = right_child

    assert root.value == 5
    assert root.left.value == 3
    assert root.right.value == 7
