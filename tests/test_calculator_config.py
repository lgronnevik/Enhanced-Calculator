import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator_config import CalculatorConfig


def test_default_history_file(monkeypatch):
	# Ensure no env var -> default used
	monkeypatch.delenv("CALCULATOR_HISTORY_FILE", raising=False)
	cfg = CalculatorConfig()
	assert cfg.history_file.endswith(".csv")


def test_env_history_file_validation(monkeypatch):
	# Non-csv extension raises
	monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "my_history.txt")
	with pytest.raises(ValueError):
		CalculatorConfig()

	# Valid csv passes
	monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "my_history.csv")
	cfg = CalculatorConfig()
	assert cfg.history_file == "my_history.csv"

