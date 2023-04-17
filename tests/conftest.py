import pytest
from src.stack import Stack
from src.queue import Queue

@pytest.fixture()
def some_stack():
    return Stack()

@pytest.fixture()
def some_queue():
    return Queue()