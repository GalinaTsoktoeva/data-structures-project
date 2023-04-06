import pytest
from src.stack import Stack

@pytest.fixture()
def some_stack():
    return Stack()