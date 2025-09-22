import pytest
import pandas as pd
import matplotlib.pyplot as plt
from definition_2b7dd6a0417f4eacb4766c6e06ba0753 import plot_communication_overhead

def create_sample_dataframe():
    data = {
        'system_type': ['Agentic AI', 'Agentic AI', 'Single Agent AI', 'Agentic AI'],
        'inter_agent_communication_count': [10, 5, 0, 15],
        'subtask_completion_time_s': [25.5, 15.2, 10.0, 30.1]
    }
    return pd.DataFrame(data)

def test_plot_communication_overhead_agentic_ai_only():
    df = create_sample_dataframe()
    try:
        plot_communication_overhead(df)
        plt.close()
        assert True  
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

def test_plot_communication_overhead_empty_dataframe():
    df = pd.DataFrame({'system_type': [], 'inter_agent_communication_count': [], 'subtask_completion_time_s': []})
    try:
        plot_communication_overhead(df)
        plt.close()
        assert True
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

def test_plot_communication_overhead_no_agentic_ai():
    data = {'system_type': ['Single Agent AI', 'Single Agent AI'],
            'inter_agent_communication_count': [0, 0],
            'subtask_completion_time_s': [10.0, 12.0]}
    df = pd.DataFrame(data)
    try:
        plot_communication_overhead(df)
        plt.close()
        assert True
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

def test_plot_communication_overhead_missing_columns():
    df = pd.DataFrame({'system_type': ['Agentic AI'], 'inter_agent_communication_count': [10]})
    with pytest.raises(KeyError):
        plot_communication_overhead(df)

def test_plot_communication_overhead_invalid_data_types():
     data = {
        'system_type': ['Agentic AI'],
        'inter_agent_communication_count': ['invalid'],
        'subtask_completion_time_s': [25.5]
    }
     df = pd.DataFrame(data)

     with pytest.raises(TypeError):
         plot_communication_overhead(df)
