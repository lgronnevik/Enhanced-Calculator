# Enhanced Calculator Application

## Overview
This is an enhanced Python calculator application that uses advanced design patterns, pandas for data management, and a modular structure with full test coverage. The calculator supports basic arithmetic operations, power/root operations, undo/redo functionality, and maintains a persistent calculation history.

## Features
- **REPL Interface**: Interactive command-line interface for continuous use.
- **Arithmetic Operations**: Addition, subtraction, multiplication, division, power, and root.
- **Design Patterns Implemented**:
  - **Observer Pattern**: Tracks calculation history.
  - **Memento Pattern**: Supports undo/redo functionality.
  - **Strategy Pattern**: Interchangeable operation execution strategies.
  - **Factory Pattern**: Dynamically creates operation instances.
  - **Facade Pattern**: Simplifies interaction with calculator subsystems.
- **Data Management**: Uses pandas DataFrames to store, load, and auto-save calculation history to CSV.
- **Configuration**: Supports environment variable configuration via `CALCULATOR_HISTORY_FILE`.
- **User Commands**:
  - `help` – Displays available commands
  - `history` – Shows calculation history
  - `undo` / `redo` – Revert or repeat calculations
  - `clear` – Clears the REPL screen
  - `save` / `load` – Save or load calculation history
  - `exit` – Exit the calculator
- **Error Handling**: Handles invalid inputs, division by zero, and other exceptional cases using LBYL and EAFP strategies.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd Enhanced-Calculator