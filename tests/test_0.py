import pytest
from definition_f4267b44bd844f4cba73e49c3bbc028e import generate_synthetic_data
import pandas as pd

def is_valid_dataframe(df):
    required_columns = ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status',
                          'subtask_completion_time_s', 'inter_agent_communication_count',
                          'overall_project_completion_time_s', 'timestamp', 'task_complexity',
                          'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']
    return all(col in df.columns for col in required_columns)


def is_non_negative(df):
    numeric_columns = ['subtask_completion_time_s', 'inter_agent_communication_count',
                         'overall_project_completion_time_s', 'overall_success_rate', 'task_complexity',
                         'num_specialized_agents']
    return all((df[col] >= 0).all() for col in numeric_columns if col in df.columns)


def has_expected_data_types(df):
    expected_types = {
        'workflow_id': 'int64',
        'subtask_id': 'int64',
        'subtask_completion_time_s': 'float64',
        'inter_agent_communication_count': 'int64',
        'overall_project_completion_time_s': 'float64',
        'task_complexity': 'int64',
        'num_specialized_agents': 'int64',
        'overall_success_rate': 'float64',
        'orchestration_strategy': 'object',
        'agent_role': 'object',
        'subtask_status': 'object',
        'timestamp': 'datetime64[ns]'
    }
    for col, expected_type in expected_types.items():
        if col in df.columns:
            if df[col].dtype != expected_types[col]:
                return False
    return True

@pytest.mark.parametrize("num_workflows, max_subtasks", [
    (10, 5),
    (0, 0),
    (1, 1),
])
def test_generate_synthetic_data_basic(num_workflows, max_subtasks):
    df = generate_synthetic_data(num_workflows, max_subtasks)
    assert isinstance(df, pd.DataFrame)
    if num_workflows > 0:
        assert is_valid_dataframe(df)
        assert len(df) >= 0  # There may be zero rows, but the data frame can be constructed
    else:
        assert len(df) == 0

def test_generate_synthetic_data_valid_data():
    df = generate_synthetic_data(5, 5)
    assert is_valid_dataframe(df)
    assert is_non_negative(df)
    assert has_expected_data_types(df)

def test_generate_synthetic_data_correct_lengths():
    num_workflows = 5
    max_subtasks = 5
    df = generate_synthetic_data(num_workflows, max_subtasks)
    assert len(df['workflow_id'].unique()) <= num_workflows

def test_generate_synthetic_data_edge_cases():
    df = generate_synthetic_data(num_workflows=1, max_subtasks=1)
    assert isinstance(df, pd.DataFrame)
    assert is_valid_dataframe(df)
    assert is_non_negative(df)
    assert has_expected_data_types(df)