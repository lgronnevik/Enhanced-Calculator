# app/calculator_repl.py

from app.operations import OperationFactory
from app.history import History
from app.calculator_memento import Caretaker
from app.input_validators import InputValidator

def process_command(user_input, history, caretaker):
    user_input = user_input.strip()
    if user_input.lower() in ("exit", "quit"):
        history.save()
        return "exit"
    if user_input.lower() == "help":
        return "help"
    if user_input.lower() == "history":
        return history.df.copy()
    if user_input.lower() == "undo":
        previous_state = caretaker.undo()
        history.df = previous_state
        return "undo"
    if user_input.lower() == "redo":
        next_state = caretaker.redo()
        history.df = next_state
        return "redo"
    parts = user_input.split()
    valid, message = InputValidator.validate_command(parts)
    if not valid:
        return f"Error: {message}"
    op_name, a_str, b_str = parts
    valid, a, b = InputValidator.validate_numbers(a_str, b_str)
    if not valid:
        return "Error: Both operands must be numbers."
    valid, message = InputValidator.validate_operation(op_name)
    if not valid:
        return f"Error: {message}"
    try:
        caretaker.save_state(history.df)
        operation = OperationFactory.create_operation(op_name)
        result = operation.execute(a, b)
        history.add_entry(op_name, a, b, result)
        return result
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    print("Welcome to the Enhanced Calculator with Config, History, Undo/Redo, and Validation!")
    print("Type 'help' for commands or 'exit' to quit.\n")
    history = History()
    caretaker = Caretaker()
    while True:
        user_input = input(">>> ").strip()
        result = process_command(user_input, history, caretaker)
        if isinstance(result, str) and result == "exit":
            print(f"Saving history to {history.filename}...")
            print("Goodbye!")
            break
        elif isinstance(result, str) and result == "help":
            print("\nCommands:")
            print("  add a b       → addition")
            print("  subtract a b  → subtraction")
            print("  multiply a b  → multiplication")
            print("  divide a b    → division")
            print("  power a b     → a raised to the power of b")
            print("  root a b      → b-th root of a")
            print("  history       → show past calculations")
            print("  undo          → undo last calculation")
            print("  redo          → redo last undone calculation")
            print("  help          → show this message")
            print("  exit / quit   → exit the calculator\n")
        elif isinstance(result, str) and result == "undo":
            print("Undo performed.")
        elif isinstance(result, str) and result == "redo":
            print("Redo performed.")
        elif isinstance(result, str) and result.startswith("Error"):
            print(result)
        elif isinstance(result, (int, float)):
            print(f"Result: {result}")
        elif isinstance(result, type(history.df)):
            print(history.df)

if __name__ == "__main__":
    main()