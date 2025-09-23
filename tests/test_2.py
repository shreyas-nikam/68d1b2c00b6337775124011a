import pytest
import pandas as pd
import matplotlib.pyplot as plt
from definition_96b3939e0bb24c06965423b7b72c6eae import plot_project_completion_time

@pytest.fixture
def sample_dataframe():
    data = {'overall_project_completion_time_s': [10, 15, 20, 25, 30],
            'task_complexity': [1, 2, 3, 4, 5],
            'system_type': ['Single Agent AI', 'Agentic AI', 'Single Agent AI', 'Agentic AI', 'Single Agent AI']}
    return pd.DataFrame(data)

def test_plot_project_completion_time_runs_without_error(sample_dataframe):
    try:
        plot_project_completion_time(sample_dataframe)
        plt.close()
    except Exception as e:
        pytest.fail(f"plot_project_completion_time raised an exception: {e}")

def test_plot_project_completion_time_empty_dataframe():
    df = pd.DataFrame({'overall_project_completion_time_s': [],
                           'task_complexity': [],
                           'system_type': []})
    try:
        plot_project_completion_time(df)
        plt.close()
    except Exception as e:
        pytest.fail(f"plot_project_completion_time raised an exception: {e}")

def test_plot_project_completion_time_missing_columns():
    df = pd.DataFrame({'task_complexity': [1, 2, 3], 'system_type': ['A', 'B', 'C']})
    with pytest.raises(KeyError):
        plot_project_completion_time(df)

def test_plot_project_completion_time_non_numeric_complexity(sample_dataframe):
    df = sample_dataframe.copy()
    df['task_complexity'] = ['a', 'b', 'c', 'd', 'e']
    with pytest.raises(TypeError):
        plot_project_completion_time(df)

def test_plot_project_completion_time_no_system_type(sample_dataframe):
    df = sample_dataframe.drop('system_type', axis=1)
    with pytest.raises(KeyError):
        plot_project_completion_time(df)
