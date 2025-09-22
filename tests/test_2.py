import pytest
import pandas as pd
import matplotlib.pyplot as plt
from definition_5b764f50d07c4ddd936fc69f6d668485 import plot_project_completion_time

@pytest.fixture
def mock_dataframe():
    data = {
        'overall_project_completion_time_s': [10, 15, 20, 25, 30, 35],
        'task_complexity': [1, 2, 3, 4, 5, 6],
        'system_type': ['Single Agent AI', 'Agentic AI', 'Single Agent AI', 'Agentic AI', 'Single Agent AI', 'Agentic AI']
    }
    return pd.DataFrame(data)

def test_plot_project_completion_time_valid_data(mock_dataframe, monkeypatch):
    # Test that the function runs without errors with valid data
    monkeypatch.setattr(plt, 'show', lambda: None)  # Prevent plot from displaying
    try:
        plot_project_completion_time(mock_dataframe)
    except Exception as e:
        pytest.fail(f"plot_project_completion_time raised an exception: {e}")

def test_plot_project_completion_time_empty_dataframe():
    # Test that the function handles an empty DataFrame gracefully
    df = pd.DataFrame({'overall_project_completion_time_s': [], 'task_complexity': [], 'system_type': []})
    try:
        plot_project_completion_time(df)
    except Exception as e:
        assert "The truth value of a DataFrame is ambiguous" in str(e) or "no data to plot" in str(e)

def test_plot_project_completion_time_missing_columns():
    # Test that the function raises an error if required columns are missing
    df = pd.DataFrame({'task_complexity': [1, 2, 3]})
    with pytest.raises(KeyError):
        plot_project_completion_time(df)

def test_plot_project_completion_time_non_numeric_complexity(mock_dataframe):
    # Test when task_complexity is non-numeric
     mock_dataframe['task_complexity'] = ['a', 'b', 'c', 'd', 'e', 'f']
     with pytest.raises(TypeError):
        plot_project_completion_time(mock_dataframe)
