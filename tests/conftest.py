import pytest
from src.stack import Stack
from src.queue import Queue
from src.linked_list import LinkedList, Node

@pytest.fixture()
def some_stack():
    return Stack()

@pytest.fixture()
def some_queue():
    return Queue()

@pytest.fixture()
def some_node():
    return Node()

@pytest.fixture()
def some_linked_list():
    return LinkedList()