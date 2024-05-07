from linkedList.node import Node
from pytest import fixture


@fixture
def first_node():
    node = Node(None, None, 5)
    yield node


def test_first_node(first_node):
    assert first_node.value == 5
    assert first_node.next is None
    assert first_node.previous is None


@fixture
def more_nodes():
    first_node = Node(None, None, 5)
    second_node = Node(first_node, None, 10)
    third_node = Node(second_node, None, 15)
    first_node.next = second_node
    second_node.next = third_node

    yield first_node


def test_more_nodes_iterate(more_nodes):
    node = more_nodes
    values = [node.value]
    while node.next:
        node = node.next
        values.append(node.value)

    assert values == [5, 10, 15, ]
