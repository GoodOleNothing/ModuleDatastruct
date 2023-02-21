import pytest
from main import *

tv = Stack()
def test_push():
    assert tv.push(4) == None
