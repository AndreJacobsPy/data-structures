from queue.queue import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)

    assert queue.items.head.value == 5
    assert queue.items.tail.value == 6


def test_dequeue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)

    queue.dequeue()
    assert queue.items.head.value == 6
    assert queue.items.tail.value == 6

    queue.dequeue()
    assert queue.items.head is None
    assert queue.items.tail is None
