from linked_list import *

t_ex = LinkedList()
def test_insert_beginning():
    t_ex.insert_beginning('1')
    assert t_ex.head.data == '1'
    t_ex.insert_beginning('2')
    assert t_ex.head.data == '2'

def test_insert_at_end():
    t_ex.insert_at_end('3')
    assert t_ex.head.data == '2'