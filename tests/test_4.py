import pytest
import pandas as pd
import matplotlib.pyplot as plt
from definition_aabda653ae6947558e17dfd64d7219c0 import plot_orchestration_comparison

@pytest.fixture
def mock_dataframe():
    data = {'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized', 'Decentralized'],
            'overall_success_rate': [0.8, 0.9, 0.6, 0.7, 0.85],
            'overall_project_completion_time_s': [100, 120, 150, 110, 130],
            'system_type': ['Agentic AI'] * 5}
    return pd.DataFrame(data)

def test_plot_orchestration_comparison_valid_data(mock_dataframe):
    try:
        plot_orchestration_comparison(mock_dataframe)
        plt.close('all')
    except Exception as e:
        pytest.fail(f"plot_orchestration_comparison raised an exception: {e}")

def test_plot_orchestration_comparison_empty_dataframe():
    df = pd.DataFrame()
    try:
        plot_orchestration_comparison(df)
        plt.close('all')
    except Exception as e:
        assert str(e) == "Input DataFrame is empty."

def test_plot_orchestration_comparison_missing_columns(mock_dataframe):
    del mock_dataframe['overall_success_rate']
    with pytest.raises(KeyError):
         plot_orchestration_comparison(mock_dataframe)
         plt.close('all')

def test_plot_orchestration_comparison_non_agentic_ai_data(mock_dataframe):
    mock_dataframe['system_type'] = ['Single Agent AI'] * 5
    try:
        plot_orchestration_comparison(mock_dataframe)
        plt.close('all')
    except Exception as e:
        assert str(e) == "No 'Agentic AI' data to plot."

def test_plot_orchestration_comparison_invalid_data_types(mock_dataframe):
    mock_dataframe['overall_success_rate'] = ['invalid', 'invalid', 'invalid', 'invalid', 'invalid']
    with pytest.raises(TypeError):
        plot_orchestration_comparison(mock_dataframe)
        plt.close('all')
