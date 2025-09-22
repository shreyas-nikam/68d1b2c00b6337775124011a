import pytest
from definition_4287640be1834d679eb0a7e32fe03948 import run_interactive_analysis
import pandas as pd
from unittest.mock import MagicMock


@pytest.fixture
def mock_dataframe():
    data = {
        'workflow_id': [1, 2, 3, 4, 5],
        'agent_role': ['A', 'B', 'A', 'C', 'B'],
        'num_specialized_agents': [1, 2, 1, 3, 2],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized', 'Decentralized'],
        'task_type': ['Type1', 'Type2', 'Type1', 'Type2', 'Type1'],
        'overall_project_completion_time_s': [10, 20, 15, 25, 18],
        'overall_success_rate': [0.8, 0.9, 0.7, 0.95, 0.85]
    }
    return pd.DataFrame(data)


def test_run_interactive_analysis_filters_data(mock_dataframe, capsys):
    run_interactive_analysis('Type1', 2, 'Decentralized', mock_dataframe)
    captured = capsys.readouterr()
    assert "overall_project_completion_time_s" in captured.out
    assert "18.00" in captured.out
    assert "overall_success_rate" in captured.out
    assert "0.85" in captured.out

def test_run_interactive_analysis_no_matching_data(mock_dataframe, capsys):
    run_interactive_analysis('NonExistentType', 5, 'UnknownStrategy', mock_dataframe)
    captured = capsys.readouterr()
    assert "No data matching" in captured.out

def test_run_interactive_analysis_single_agent_scenario(mock_dataframe, capsys):
    run_interactive_analysis('Type1', 1, 'Centralized', mock_dataframe)
    captured = capsys.readouterr()
    assert "overall_project_completion_time_s" in captured.out
    assert "10.00" in captured.out
    assert "overall_success_rate" in captured.out
    assert "0.80" in captured.out

def test_run_interactive_analysis_handles_empty_dataframe(capsys):
    empty_df = pd.DataFrame()
    run_interactive_analysis('AnyType', 3, 'AnyStrategy', empty_df)
    captured = capsys.readouterr()
    assert "No data matching" in captured.out

def test_run_interactive_analysis_with_mocked_plotting(mock_dataframe, monkeypatch, capsys):
    monkeypatch.setattr("definition_4287640be1834d679eb0a7e32fe03948.plot_orchestration_comparison", MagicMock())
    run_interactive_analysis('Type2', 3, 'Centralized', mock_dataframe)
    captured = capsys.readouterr()
    assert "overall_project_completion_time_s" in captured.out
    assert "25.00" in captured.out
    assert "overall_success_rate" in captured.out
    assert "0.95" in captured.out
    # Assert that the mocking worked.
    # from definition_4287640be1834d679eb0a7e32fe03948 import plot_orchestration_comparison
    # plot_orchestration_comparison.assert_called_once()
