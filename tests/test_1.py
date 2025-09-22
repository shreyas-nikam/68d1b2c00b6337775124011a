import pytest
import pandas as pd
from definition_6a5925fe82bc4250be8f611dde0706d1 import validate_and_preprocess_data

@pytest.fixture
def sample_dataframe():
    data = {
        'workflow_id': [1, 2, 3],
        'agent_role': ['Planner', 'Retriever', 'Summarizer'],
        'subtask_id': [1, 2, 3],
        'subtask_status': ['Completed', 'InProgress', 'Failed'],
        'subtask_completion_time_s': [10.0, 15.0, 20.0],
        'inter_agent_communication_count': [2, 3, 1],
        'overall_project_completion_time_s': [60.0, 70.0, 80.0],
        'timestamp': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'task_complexity': [5, 7, 9],
        'num_specialized_agents': [1, 3, 5],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None'],
        'overall_success_rate': [0.9, 0.8, 0.7]
    }
    return pd.DataFrame(data)


def test_validate_and_preprocess_data_valid(sample_dataframe):
    df = validate_and_preprocess_data(sample_dataframe)
    assert 'system_type' in df.columns
    assert df['system_type'].iloc[0] == 'Single Agent AI'
    assert df['system_type'].iloc[1] == 'Agentic AI'


def test_validate_and_preprocess_data_missing_column(sample_dataframe):
    del sample_dataframe['workflow_id']
    with pytest.raises(KeyError):
        validate_and_preprocess_data(sample_dataframe)


def test_validate_and_preprocess_data_duplicate_workflow_id(sample_dataframe):
    sample_dataframe['workflow_id'] = [1, 1, 3]
    with pytest.raises(ValueError):
        validate_and_preprocess_data(sample_dataframe)


def test_validate_and_preprocess_data_missing_values(sample_dataframe):
    sample_dataframe['subtask_completion_time_s'] = [10.0, None, 20.0]
    with pytest.raises(ValueError):
         validate_and_preprocess_data(sample_dataframe)

def test_validate_and_preprocess_data_incorrect_data_type(sample_dataframe):
    sample_dataframe['num_specialized_agents'] = ['1', '3', '5']
    with pytest.raises(TypeError):
        validate_and_preprocess_data(sample_dataframe)
