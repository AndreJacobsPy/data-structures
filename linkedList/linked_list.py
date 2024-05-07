from __future__ import annotations
from dataclasses import dataclass
from linkedList.node import Node


@dataclass
class LinkedList:
    head: Node | None = None
    tail: Node | None = None

    def add(self, value: int) -> None:
        """Adding a node to the linked list (O(1))"""
        node = Node(None, None, value)
        if self.head is None:  # base case O(1)
            self.head = node
            self.tail = self.head

        elif self.head is self.tail:  # O(1)
            self.head.next = node
            self.tail = node

            # update new node's pointer
            self.tail.previous = self.head

        elif self.head is not self.tail:  # O(1)
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

        else:
            raise Exception("The linked list is broken...")

    def delete(self, value: int) -> Node:
        """Finding a node in the linked list and deleting it (O(n))"""
        # base case
        if self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node

        node = self.head
        while node.value != value and node.next is None:
            node = node.next

        if node is None:
            raise ValueError("The node is not found...")

        if node == self.head:
            self.head = node.next

        elif node == self.tail:
            self.tail = node.previous

        elif (left := node.previous) and (right := node.next):
            left.next = node.next
            right.previous = left

        elif node == self.head == self.tail:
            self.head = None
            self.tail = None

        return node

    def find(self, value: int) -> Node:
        """Finding a node in the linked list with the given value (O(n))"""
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value is not in list...")
