import pytest
import pandas as pd
from definition_9ecbc6d8850549cab4be8cb287713ef2 import validate_and_preprocess_data

def create_sample_dataframe():
    data = {
        'workflow_id': [1, 2, 3],
        'agent_role': ['Planner', 'Retriever', 'Summarizer'],
        'subtask_id': [1, 2, 3],
        'subtask_status': ['Completed', 'InProgress', 'Failed'],
        'subtask_completion_time_s': [10.0, 20.0, 30.0],
        'inter_agent_communication_count': [2, 3, 4],
        'overall_project_completion_time_s': [100.0, 200.0, 300.0],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'task_complexity': [5, 10, 15],
        'num_specialized_agents': [1, 2, 3],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None'],
        'overall_success_rate': [0.8, 0.9, 0.7]
    }
    return pd.DataFrame(data)

def create_incomplete_dataframe():
    data = {
        'workflow_id': [1, 2, 3],
        'agent_role': ['Planner', 'Retriever', 'Summarizer'],
        'subtask_id': [1, 2, 3],
        'subtask_status': ['Completed', 'InProgress', 'Failed'],
        'subtask_completion_time_s': [10.0, 20.0, None],
        'inter_agent_communication_count': [2, 3, 4],
        'overall_project_completion_time_s': [100.0, 200.0, 300.0],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'task_complexity': [5, 10, 15],
        'num_specialized_agents': [1, 2, 3],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None'],
        'overall_success_rate': [0.8, 0.9, 0.7]
    }
    return pd.DataFrame(data)

def create_duplicate_ids_dataframe():
    data = {
        'workflow_id': [1, 1, 3],
        'agent_role': ['Planner', 'Retriever', 'Summarizer'],
        'subtask_id': [1, 2, 3],
        'subtask_status': ['Completed', 'InProgress', 'Failed'],
        'subtask_completion_time_s': [10.0, 20.0, 30.0],
        'inter_agent_communication_count': [2, 3, 4],
        'overall_project_completion_time_s': [100.0, 200.0, 300.0],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'task_complexity': [5, 10, 15],
        'num_specialized_agents': [1, 2, 3],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None'],
        'overall_success_rate': [0.8, 0.9, 0.7]
    }
    return pd.DataFrame(data)


def create_invalid_datatypes_dataframe():
     data = {
        'workflow_id': ['1', '2', '3'],
        'agent_role': ['Planner', 'Retriever', 'Summarizer'],
        'subtask_id': [1, 2, 3],
        'subtask_status': ['Completed', 'InProgress', 'Failed'],
        'subtask_completion_time_s': [10.0, 20.0, 30.0],
        'inter_agent_communication_count': [2, 3, 4],
        'overall_project_completion_time_s': [100.0, 200.0, 300.0],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'task_complexity': [5, 10, 15],
        'num_specialized_agents': [1, 2, 3],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None'],
        'overall_success_rate': [0.8, 0.9, 0.7]
    }
     return pd.DataFrame(data)


def test_validate_and_preprocess_data_success():
    df = create_sample_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert 'system_type' in processed_df.columns
    assert processed_df['system_type'].tolist() == ['Single Agent AI', 'Agentic AI', 'Agentic AI']

def test_validate_and_preprocess_data_missing_values():
    df = create_incomplete_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert df['subtask_completion_time_s'].isnull().any()

def test_validate_and_preprocess_data_duplicate_ids():
    df = create_duplicate_ids_dataframe()
    with pytest.raises(ValueError):
        validate_and_preprocess_data(df.copy())

def test_validate_and_preprocess_data_no_errors():
    df = create_sample_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert processed_df is not None

def test_validate_and_preprocess_invalid_datatypes():
     df = create_invalid_datatypes_dataframe()
     with pytest.raises(TypeError):
        validate_and_preprocess_data(df.copy())
