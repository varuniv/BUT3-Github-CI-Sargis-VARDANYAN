""" fichier pour test main """


from greeting.main import greet
from greeting.utils import add,sub


def test_greet():
    """test great"""

    assert greet("World") == "Hello, World!"


def test_add():
    """test add"""

    assert add(5, 7) == 12

def test_sub():
    """test sub"""

    assert add(9, 7) == 2