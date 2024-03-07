import pytest
from ukp_github_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp_github_workshop import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####
def test_fib_1():
    f = Fibonacci()
    assert f.fib(1) == 1

def test_fib_2():
    f = Fibonacci()
    assert f.fib(2) == 1

def test_fib_5():
    f = Fibonacci()
    assert f.fib(5) == 5
##########################