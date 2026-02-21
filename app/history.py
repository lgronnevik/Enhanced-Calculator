import pandas as pd
from app.calculator_memento import Caretaker

class History:
    """Manages calculator history using pandas and supports undo/redo."""
    def __init__(self, filename="history.csv"):
        self.filename = filename
        self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self.caretaker = Caretaker()

    def add_entry(self, operation, a, b, result):
        """Add a new calculation to history and save state for undo/redo."""
        new_row = {"operation": operation, "a": a, "b": b, "result": result}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.caretaker.save_state(self.df)

    def undo(self):
        """Undo last calculation."""
        self.df = self.caretaker.undo()
        return self.df

    def redo(self):
        """Redo previously undone calculation."""
        self.df = self.caretaker.redo()
        return self.df

    def save(self):
        """Save history to CSV."""
        self.df.to_csv(self.filename, index=False)

    def load(self):
        """Load history from CSV."""
        try:
            self.df = pd.read_csv(self.filename)
            self.caretaker.save_state(self.df)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])
            self.caretaker.save_state(self.df)