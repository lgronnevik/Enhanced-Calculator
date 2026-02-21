import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.input_validators import InputValidator

def test_validate_integer():
    assert InputValidator.validate_integer("5") == 5
    assert InputValidator.validate_integer("-10") == -10
    with pytest.raises(ValueError):
        InputValidator.validate_integer("abc")

def test_validate_float():
    assert InputValidator.validate_float("3.14") == 3.14
    assert InputValidator.validate_float("-0.5") == -0.5
    with pytest.raises(ValueError):
        InputValidator.validate_float("xyz")


def test_validate_operation():
    # valid operation returns (True, '')
    valid, msg = InputValidator.validate_operation("add")
    assert valid is True
    assert msg == ""

    # invalid operation returns (False, ...)
    valid, msg = InputValidator.validate_operation("unknown_op")
    assert valid is False
    assert "Invalid operation" in msg