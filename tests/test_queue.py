"""Здесь надо написать тесты с использованием unittest для модуля queue."""
def test_queue(some_queue):
    assert some_queue.head == None
    assert some_queue.tail == None

def test_enqueue(some_queue):
    some_queue.enqueue("data1")
    some_queue.enqueue("data2")
    some_queue.enqueue("data3")
    assert some_queue.head.data == "data1"
    assert some_queue.tail.data == "data3"

def test_dequeue(some_queue):
    some_queue.enqueue("data1")
    some_queue.enqueue("data2")
    some_queue.enqueue("data3")
    assert some_queue.dequeue() == 'data1'
    assert some_queue.dequeue() == 'data2'
    assert some_queue.dequeue() == 'data3'
    assert some_queue.dequeue() is None
def test_str(some_queue):
    assert str(some_queue) == ""
    some_queue.enqueue("data1")
    assert str(some_queue) == "data1\n"

