from bst.tree import BST


def test_tree_trivial():
    bst = BST()
    bst.insert(5)

    assert bst.root.value == 5


def test_tree_basic():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)

    assert bst.root.value == 5
    assert bst.root.left.value == 3
    assert bst.root.right.value == 7
