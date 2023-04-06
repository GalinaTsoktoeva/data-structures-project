"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
def test_stack(some_stack):

    assert some_stack.top == None

def test_stack_push(some_stack):
    some_stack.push(4)
    assert some_stack.top.data == 4


def test_stack_pop(some_stack):
    assert some_stack.pop() == None
    some_stack.push(1)
    some_stack.push(2)
    del_data = some_stack.pop()
    assert del_data == 2


