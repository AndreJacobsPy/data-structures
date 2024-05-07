from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    previous: Node | None
    next: Node | None
    value: int

    def __eq__(self, other: Node) -> bool:
        return self.value == other.value
