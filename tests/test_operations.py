def test_operation_base_execute():
    op = Operation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.operations import Add, Subtract, Multiply, Divide, Power, Root, Operation
from app.operations import OperationFactory

def test_add():
    op = Add()
    assert op.execute(2, 3) == 5

def test_subtract():
    op = Subtract()
    assert op.execute(5, 2) == 3

def test_multiply():
    op = Multiply()
    assert op.execute(3, 4) == 12

def test_divide():
    op = Divide()
    assert op.execute(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        op.execute(10, 0)

def test_power():
    op = Power()
    assert op.execute(2, 3) == 8

def test_root():
    op = Root()
    assert op.execute(27, 3) == 3
    with pytest.raises(ZeroDivisionError):
        op.execute(27, 0)


def test_operation_factory_unknown():
    with pytest.raises(ValueError):
        OperationFactory.create_operation("bogus")