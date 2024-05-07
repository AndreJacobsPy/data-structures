from __future__ import annotations
from dataclasses import dataclass
from linkedList.linked_list import LinkedList


@dataclass
class Stack:
    items = LinkedList()

    def __repr__(self) -> str:
        node = self.items.head
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next

        return str(values)

    def push(self, item: Any) -> None:
        self.items.add(item)

    def pop(self) -> Node:
        node = self.items.tail
        self.items.tail = node.previous

        if self.items.tail is None:
            self.items.head = None
            return node

        self.items.tail.next = None
        return node
