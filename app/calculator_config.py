# app/calculator_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CalculatorConfig:
    """
    Manages configuration settings for the calculator.
    Currently, it handles the history file path.
    """

    def __init__(self):
        # Default history filename
        default_filename = "history.csv"
        # Get from environment variable, fallback to default
        self.history_file = os.getenv("CALCULATOR_HISTORY_FILE", default_filename)

        # Validate the filename
        if not self.history_file.endswith(".csv"):
            raise ValueError("History file must have a .csv extension")