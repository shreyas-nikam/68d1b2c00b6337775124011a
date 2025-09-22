import pytest
from definition_e45ffdb853904355861bdc6aed0dcc46 import run_interactive_analysis
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {'task_type': ['A', 'A', 'B', 'B'],
            'num_agents': [1, 2, 1, 2],
            'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized'],
            'data': [1, 2, 3, 4]}
    return pd.DataFrame(data)

def test_run_interactive_analysis_valid_filter(sample_dataframe, capsys):
    run_interactive_analysis('A', 2, 'Decentralized', sample_dataframe)
    captured = capsys.readouterr()
    assert "task_type" in captured.out #Basic smoke test - if it runs

def test_run_interactive_analysis_no_match(sample_dataframe, capsys):
    run_interactive_analysis('C', 3, 'Unknown', sample_dataframe)
    captured = capsys.readouterr()
    assert captured.out != "" # should not crash

def test_run_interactive_analysis_empty_dataframe():
    df = pd.DataFrame()
    try:
        run_interactive_analysis('A', 1, 'Centralized', df)
    except Exception as e:
        assert False, f"Unexpected exception: {e}" #Should not crash.

def test_run_interactive_analysis_type_error():
    with pytest.raises(TypeError):
         run_interactive_analysis(123, 'abc', [], 123)
