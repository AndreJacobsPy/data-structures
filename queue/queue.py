from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from linkedList.linked_list import LinkedList
from linkedList.node import Node


@dataclass
class Queue:
    items = LinkedList()

    def __repr__(self) -> str:
        node = self.items.head
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next

        return str(values)

    def enqueue(self, item: Any) -> None:
        self.items.add(item)

    def dequeue(self) -> Node:
        if self.items.head is None:
            raise ValueError("Queue is empty")

        if (node := self.items.head) == self.items.tail:
            self.items.head = None
            self.items.tail = None
            return node

        else:
            node = self.items.head
            self.items.head = node.next

        return node
