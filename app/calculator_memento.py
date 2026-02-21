import pandas as pd

class Memento:
    """Stores a snapshot of the calculator's state (history DataFrame)."""
    def __init__(self, state: pd.DataFrame):
        self.state = state.copy()

class Caretaker:
    """Manages undo/redo states using the Memento pattern."""
    def __init__(self):
        self._history = []
        self._current = -1

    def save_state(self, state: pd.DataFrame):
        """Save a new state and discard any redo history."""
        if self._current < len(self._history) - 1:
            self._history = self._history[:self._current + 1]
        self._history.append(Memento(state))
        self._current += 1

    def undo(self):
        """Go one step back in history."""
        if self._current > 0:
            self._current -= 1
            return self._history[self._current].state.copy()
        elif self._current == 0:
            return self._history[0].state.copy()
        return pd.DataFrame(columns=["operation", "a", "b", "result"])

    def redo(self):
        """Go one step forward in history."""
        if self._current < len(self._history) - 1:
            self._current += 1
            return self._history[self._current].state.copy()
        return self._history[self._current].state.copy() if self._history else pd.DataFrame(columns=["operation", "a", "b", "result"])