import sys
import os
import pytest
import pandas as pd
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.history import History

def test_add_entry_and_save_load():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        temp_history_file = tmp.name

    history = History(filename=temp_history_file)
    history.add_entry("add", 1, 2, 3)
    history.save()

    new_history = History(filename=temp_history_file)
    new_history.load()
    
    assert len(new_history.df) == 1
    assert new_history.df.iloc[0]["operation"] == "add"

    os.remove(temp_history_file)


def test_undo_redo_empty():
    h = History()
    # undo/redo on empty history should return empty DataFrame
    df_undo = h.undo()
    df_redo = h.redo()
    assert df_undo.empty
    assert df_redo.empty


def test_load_file_not_found():
    h = History(filename="nonexistent_file.csv")
    h.load()
    assert h.df.empty