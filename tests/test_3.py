import pytest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from definition_3ae5883d593d40c7b1299edacce2389c import plot_communication_overhead

@pytest.fixture
def sample_dataframe():
    data = {'inter_agent_communication_count': [10, 5, 15, 20, 8],
            'subtask_completion_time_s': [5, 2, 7, 10, 3],
            'system_type': ['Agentic AI', 'Agentic AI', 'Agentic AI', 'Agentic AI', 'Agentic AI']}
    return pd.DataFrame(data)

def test_plot_communication_overhead_agentic_ai(sample_dataframe, monkeypatch):
    # Test that the function runs without errors for Agentic AI data.
    monkeypatch.setattr(plt, 'show', lambda: None)  # Prevent plot from displaying during test
    try:
        plot_communication_overhead(sample_dataframe)
    except Exception as e:
        pytest.fail(f"plot_communication_overhead raised an exception: {e}")


def test_plot_communication_overhead_empty_dataframe():
    # Test with an empty dataframe.
    df = pd.DataFrame({'inter_agent_communication_count': [], 'subtask_completion_time_s': [], 'system_type':[]})
    try:
        plot_communication_overhead(df)
    except Exception as e:
        pytest.fail(f"plot_communication_overhead raised an exception: {e}")

def test_plot_communication_overhead_mixed_system_types(monkeypatch):
    # Test with a dataframe that has mixed system types, but the plot should only show agentic ai.
    data = {'inter_agent_communication_count': [10, 5, 15, 20, 8],
            'subtask_completion_time_s': [5, 2, 7, 10, 3],
            'system_type': ['Agentic AI', 'Single Agent AI', 'Agentic AI', 'Agentic AI', 'Single Agent AI']}
    df = pd.DataFrame(data)
    monkeypatch.setattr(plt, 'show', lambda: None)  # Prevent plot from displaying during test
    try:
        plot_communication_overhead(df)
    except Exception as e:
        pytest.fail(f"plot_communication_overhead raised an exception: {e}")

def test_plot_communication_overhead_no_communication(sample_dataframe, monkeypatch):
    # Test with a dataframe where there is no inter-agent communication.
    sample_dataframe['inter_agent_communication_count'] = 0
    monkeypatch.setattr(plt, 'show', lambda: None)  # Prevent plot from displaying during test
    try:
        plot_communication_overhead(sample_dataframe)
    except Exception as e:
        pytest.fail(f"plot_communication_overhead raised an exception: {e}")
