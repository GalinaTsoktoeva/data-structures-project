"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
def test_node(some_node):
    assert some_node.data == None
    assert some_node.next_node == None

def test_linked_list(some_linked_list):
    some_linked_list.insert_beginning({'a': 1})
    some_linked_list.insert_at_end({'b': 2})
    assert str(some_linked_list) == "{'a': 1} -> {'b': 2} -> None"

def test_to_list(some_linked_list):
    some_linked_list.insert_beginning({'a': 1})
    assert some_linked_list.to_list() == [{'a': 1}]

def test_get_data_by_id(some_linked_list):
    some_linked_list.get_data_by_id(2)
    assert some_linked_list.get_data_by_id(2) == None
    some_linked_list.insert_beginning({'id': 0})
    assert some_linked_list.get_data_by_id(0) == {'id': 0}