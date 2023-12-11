from ..queue import Queue
import pytest
from ..node import Node

def test_enqueue():
    queue = Queue()
    queue.enqueue(10)

    assert queue.start == queue.last
    assert 10 == queue.start.data
    assert 10 == queue.last.data
    assert 1 == queue.size

    queue.enqueue(20)

    assert 20 == queue.last.data
    assert 10 == queue.start.data
    assert 2 == queue.size

def test_dequeue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert 10 == queue.dequeue()
    assert 20 == queue.dequeue()
    assert None == queue.dequeue()

def test_clear():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.clear()

    assert None == queue.start
    assert 0 == queue.size
