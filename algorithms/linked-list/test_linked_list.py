from linked_list import LinkedList

def test_prepend():
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert list(ll) == [1, 2, 3]
