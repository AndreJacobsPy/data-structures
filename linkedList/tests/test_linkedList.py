from linkedList.linked_list import LinkedList
from linkedList.node import Node


def test_trivial_list():
    linked_list = LinkedList()
    linked_list.add(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next is None
    assert linked_list.head is linked_list.tail


def test_linked_list_size_2():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)

    assert (second_node := linked_list.head.next).value == 2
    assert second_node.next is None
    assert second_node.previous is linked_list.head
    assert linked_list.head is not linked_list.tail


def test_linked_list_size_3():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert (third_node := linked_list.head.next.next).value == 3
    assert third_node.next is None
    assert third_node.previous is (second_node := linked_list.head.next)
    assert second_node.next is third_node
    assert second_node.previous is linked_list.head
    assert linked_list.head is not linked_list.tail


def test_linked_list_size_50():
    linked_list = LinkedList()
    for i in range(50):
        linked_list.add(i + 1)

    node = linked_list.head
    values = [node.value]
    while node.next:
        node = node.next
        values.append(node.value)

    assert list(range(1, 51)) == values


def test_trivial_find():
    linked_list = LinkedList()
    linked_list.add(1)

    assert linked_list.find(1) == Node(None, None, 1)


def test_find_50():
    linked_list = LinkedList()
    for i in range(50):
        linked_list.add(i + 1)

    values = [linked_list.find(i).value for i in range(1, 51)]
    assert values == list(range(1, 51))


def test_trivial_delete():
    linked_list = LinkedList()
    linked_list.add(1)
    node = linked_list.head
    node_removed = linked_list.delete(1)

    assert node is node_removed
    assert linked_list.head is None
    assert linked_list.tail is None


def test_delete_50():
    linked_list = LinkedList()
    for i in range(50):
        linked_list.add(i + 1)

    deleted_nodes = [linked_list.delete(i + 1).value for i in range(50)]

    assert linked_list.head is None
    assert linked_list.tail is None
    assert deleted_nodes == list(range(1, 51))
