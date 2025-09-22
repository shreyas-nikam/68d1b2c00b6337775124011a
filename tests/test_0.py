import pytest
from definition_7adc621bd8b141ee81e1f5cf589cdb6e import generate_synthetic_data
import pandas as pd

def is_dataframe(obj):
    try:
        return isinstance(obj, pd.DataFrame)
    except ImportError:
        return False

@pytest.mark.parametrize("num_workflows, max_subtasks, expected_columns", [
    (10, 5, ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status', 'subtask_completion_time_s', 'inter_agent_communication_count', 'overall_project_completion_time_s', 'timestamp', 'task_complexity', 'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']),
    (0, 5, ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status', 'subtask_completion_time_s', 'inter_agent_communication_count', 'overall_project_completion_time_s', 'timestamp', 'task_complexity', 'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']),  # Edge case: zero workflows
])
def test_generate_synthetic_data_basic(num_workflows, max_subtasks, expected_columns):
    data = generate_synthetic_data(num_workflows, max_subtasks)
    if is_dataframe(data):
        df = data
        assert isinstance(df, pd.DataFrame)
        assert all(col in df.columns for col in expected_columns)
        if num_workflows > 0:
            assert len(df) > 0
        else:
            assert len(df) == 0
    else:
        assert False, "Expected a Pandas DataFrame"


def test_generate_synthetic_data_max_subtasks():
    num_workflows = 5
    max_subtasks = 2
    df = generate_synthetic_data(num_workflows, max_subtasks)
    if is_dataframe(df):
      assert df['task_complexity'].max() <= max_subtasks
    else:
      assert False, "Expected a Pandas DataFrame"


def test_generate_synthetic_data_types():
    num_workflows = 5
    max_subtasks = 2
    df = generate_synthetic_data(num_workflows, max_subtasks)
    if is_dataframe(df):
        assert df['workflow_id'].dtype == 'int64'
        assert df['subtask_id'].dtype == 'int64'
        assert df['task_complexity'].dtype == 'int64'
        assert df['num_specialized_agents'].dtype == 'int64'
        assert df['subtask_completion_time_s'].dtype == 'float64'
        assert df['overall_project_completion_time_s'].dtype == 'float64'
        assert df['inter_agent_communication_count'].dtype == 'int64'
        assert df['overall_success_rate'].dtype == 'float64'
        assert df['agent_role'].dtype == 'object'
        assert df['subtask_status'].dtype == 'object'
        assert df['orchestration_strategy'].dtype == 'object'
        assert df['timestamp'].dtype == 'datetime64[ns]'
    else:
        assert False, "Expected a Pandas DataFrame"

def test_generate_synthetic_data_non_negative_times():
    num_workflows = 5
    max_subtasks = 2
    df = generate_synthetic_data(num_workflows, max_subtasks)
    if is_dataframe(df):
        assert (df['subtask_completion_time_s'] >= 0).all()
        assert (df['overall_project_completion_time_s'] >= 0).all()
    else:
        assert False, "Expected a Pandas DataFrame"
