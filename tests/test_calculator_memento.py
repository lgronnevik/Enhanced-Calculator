def test_redo_empty_history():
    # Branch: _history is empty, _current == -1
    caretaker = Caretaker()
    result = caretaker.redo()
    assert result.empty
import sys
import os
import pytest
import pandas as pd

# Fix Python path to find app package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator_memento import Memento, Caretaker

def test_memento_undo_redo():
    df = pd.DataFrame(columns=["operation", "a", "b", "result"])      
    caretaker = Caretaker()

    caretaker.save_state(df)

    df1 = pd.DataFrame([{"operation":"add","a":1,"b":2,"result":3}])  
    caretaker.save_state(df1)

    state = caretaker.undo()
    assert state.empty

    state = caretaker.redo()
    assert not state.empty
    assert state.iloc[0]["operation"] == "add"


def test_trim_redo_history():
    df0 = pd.DataFrame(columns=["operation", "a", "b", "result"])  
    caretaker = Caretaker()

    caretaker.save_state(df0)

    df1 = pd.DataFrame([{"operation": "add", "a": 1, "b": 2, "result": 3}])
    caretaker.save_state(df1)

    df2 = pd.DataFrame([{"operation": "subtract", "a": 5, "b": 2, "result": 3}])
    caretaker.save_state(df2)

    # Undo one step (to df1)
    s = caretaker.undo()
    assert s.iloc[0]["operation"] == "add"

    # Save a new state after undo: this should trim the redo history
    df_new = pd.DataFrame([{"operation": "multiply", "a": 2, "b": 3, "result": 6}])
    caretaker.save_state(df_new)

    # There should be no redo to df2 now; redo should return the current state
    r = caretaker.redo()
    assert r.iloc[0]["operation"] == "multiply"


def test_undo_empty_history_returns_empty():
    caretaker = Caretaker()
    res = caretaker.undo()
    assert list(res.columns) == ["operation", "a", "b", "result"]