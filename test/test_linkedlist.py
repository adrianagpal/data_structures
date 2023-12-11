from ..linkedlist import LinkedList
from ..node import Node

def test_node():

    x = Node(50)

    assert 50 == x.data

def test_assign_next():
    x = Node(50)
    y = Node(60)
    x.assign_next(y)

    assert y == x.next
    assert None == y.next

def test_add():
    list = LinkedList()
    list.add(40)
    list.add(70)

    assert 2 == list.size

    list = LinkedList()
    list.add(40)
    list.add(70)

    assert list.last.data == 70

def test_remove():
    list = LinkedList()

    assert False == list.remove(0)
    list.add(10)
    list.add(20)
    list.add(30)
    list.remove(1)
    assert False == list.remove(-1)
    assert False == list.remove(2)

    assert 30 == list.get(1)
    assert 10 == list.get(0)
    assert None == list.get(2)

def test_get():
    list = LinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(40)
    list.add(50)

    assert 10 == list.get(0)
    assert 20 == list.get(1)
    assert 30 == list.get(2)
    assert 40 == list.get(3)
    assert 50 == list.get(4)
    assert None == list.get(5)
    assert None == list.get(-1)

def test_count():
    list = LinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(40)
    list.add(50)
    list.add(20)
    list.add(-1)
    list.remove(2)

    assert 2 == list.count(20)
    assert 0 == list.count(51)
    assert 1 == list.count(-1)
    assert 0 == list.count(30)

    lista = LinkedList()

    assert 0 == lista.count(30)

def test_find():
    list = LinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(40)
    list.add(50)
    list.add(20)
    list.add(-1)
    list.remove(2)

    assert 0 == list.find(10)
    assert 2 == list.find(40)
    assert None == list.find(55)
    assert 5 == list.find(-1)

    lista = LinkedList()

    assert None == lista.find(30)

def test_findall():
    list = LinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(40)
    list.add(50)
    list.add(20)
    list.add(-1)
    list.remove(2)

    assert [0] == list.findall(10)
    assert [2] == list.findall(40)
    assert None == list.findall(55)
    assert [5] == list.findall(-1)
    assert [1,4] == list.findall(20)

    lista = LinkedList()

    assert None == lista.findall(30)
