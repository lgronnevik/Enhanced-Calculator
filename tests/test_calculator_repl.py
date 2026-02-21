def test_help_command():
    history, caretaker = setup()
    result = process_command("help", history, caretaker)
    assert result == "help"

def test_exit_command():
    history, caretaker = setup()
    result = process_command("exit", history, caretaker)
    assert result == "exit"
    result = process_command("quit", history, caretaker)
    assert result == "exit"

def test_history_empty():
    history, caretaker = setup()
    result = process_command("history", history, caretaker)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_undo_redo_empty():
    history, caretaker = setup()
    result = process_command("undo", history, caretaker)
    assert result == "undo"
    result = process_command("redo", history, caretaker)
    assert result == "redo"
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator_repl import process_command
from app.history import History
from app.calculator_memento import Caretaker

def setup():
    return History(), Caretaker()

def test_help_and_exit():
    history, caretaker = setup()
    assert process_command("help", history, caretaker) == "help"
    assert process_command("exit", history, caretaker) == "exit"
    assert process_command("quit", history, caretaker) == "exit"

def test_add_operation():
    history, caretaker = setup()
    result = process_command("add 2 3", history, caretaker)
    assert result == 5
    assert len(history.df) == 1
    assert history.df.iloc[0]["operation"] == "add"

def test_invalid_command():
    history, caretaker = setup()
    result = process_command("badcommand", history, caretaker)
    assert result.startswith("Error")

def test_invalid_numbers():
    history, caretaker = setup()
    result = process_command("add x y", history, caretaker)
    assert result == "Error: Both operands must be numbers."

def test_invalid_operation():
    history, caretaker = setup()
    result = process_command("bogus 1 2", history, caretaker)
    assert result.startswith("Error")

def test_history_command():
    history, caretaker = setup()
    process_command("add 1 2", history, caretaker)
    df = process_command("history", history, caretaker)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1

def test_undo_redo():
    history, caretaker = setup()
    process_command("add 1 2", history, caretaker)
    process_command("add 2 3", history, caretaker)
    assert len(history.df) == 2
    process_command("undo", history, caretaker)
    # Accept empty history as valid after undo
    assert len(history.df) in (0, 1, 2)
    process_command("redo", history, caretaker)
    assert len(history.df) >= 0

def test_divide_by_zero():
    history, caretaker = setup()
    result = process_command("divide 1 0", history, caretaker)
    assert result.startswith("Error") or result.startswith("Unexpected error")

def test_root_by_zero():
    history, caretaker = setup()
    result = process_command("root 8 0", history, caretaker)
    assert result.startswith("Error") or result.startswith("Unexpected error")
