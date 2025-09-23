import pytest
import pandas as pd
import matplotlib.pyplot as plt
from definition_5725e7b71bd04562b338dfb8a145fb2d import plot_communication_overhead

def create_mock_dataframe():
    data = {
        'system_type': ['Agentic AI', 'Single Agent AI', 'Agentic AI', 'Agentic AI'],
        'inter_agent_communication_count': [10, 0, 5, 15],
        'subtask_completion_time_s': [20, 15, 10, 25]
    }
    return pd.DataFrame(data)

def test_plot_communication_overhead_agentic_ai_only():
    df = create_mock_dataframe()
    try:
        plot_communication_overhead(df)
        plt.close()
    except Exception as e:
        assert False, f"Plotting raised an exception: {e}"

def test_plot_communication_overhead_empty_dataframe():
    df = pd.DataFrame()
    try:
        plot_communication_overhead(df)
        plt.close()
    except Exception as e:
        assert False, f"Plotting raised an exception: {e}"

def test_plot_communication_overhead_no_agentic_ai():
    data = {'system_type': ['Single Agent AI', 'Single Agent AI'], 'inter_agent_communication_count': [0, 0], 'subtask_completion_time_s': [10, 15]}
    df = pd.DataFrame(data)

    try:
        plot_communication_overhead(df)
        plt.close()
    except Exception as e:
        assert False, f"Plotting raised an exception: {e}"

def test_plot_communication_overhead_invalid_data_types():
        data = {
            'system_type': ['Agentic AI', 'Agentic AI'],
            'inter_agent_communication_count': ['a', 'b'],
            'subtask_completion_time_s': [10, 20]
        }
        df = pd.DataFrame(data)
        with pytest.raises(TypeError):
            plot_communication_overhead(df)
            plt.close()

def test_plot_communication_overhead_missing_columns():
    data = {
        'inter_agent_communication_count': [10, 0, 5, 15],
        'subtask_completion_time_s': [20, 15, 10, 25]
    }
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        plot_communication_overhead(df)
        plt.close()
