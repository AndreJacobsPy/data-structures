from stack.stack import Stack


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.pop().value == 2
    assert stack.pop().value == 1
