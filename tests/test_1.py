import pytest
import pandas as pd
from definition_82e3172fdba1497a9f75cbd911e628ac import validate_and_preprocess_data

def create_sample_dataframe():
    data = {
        'workflow_id': [1, 2, 3, 1, 2],
        'agent_role': ['Planner', 'Retriever', 'Summarizer', 'Planner', 'Retriever'],
        'subtask_id': [1, 2, 3, 4, 5],
        'subtask_status': ['Completed', 'InProgress', 'Completed', 'Failed', 'Completed'],
        'subtask_completion_time_s': [10.5, 20.2, 15.7, 5.1, 12.3],
        'inter_agent_communication_count': [2, 5, 1, 0, 3],
        'overall_project_completion_time_s': [60.1, 120.5, 90.2, 30.8, 70.4],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'task_complexity': [10, 20, 15, 5, 12],
        'num_specialized_agents': [3, 1, 2, 5, 1],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized', 'Decentralized'],
        'overall_success_rate': [0.95, 0.85, 0.75, 0.65, 0.90]
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def create_incomplete_dataframe():
    data = {
        'workflow_id': [1, 2, 3, 1, 2],
        'agent_role': ['Planner', 'Retriever', 'Summarizer', 'Planner', 'Retriever'],
        'subtask_id': [1, 2, 3, 4, 5],
        'subtask_status': ['Completed', 'InProgress', 'Completed', 'Failed', 'Completed'],
        'subtask_completion_time_s': [10.5, 20.2, 15.7, 5.1, 12.3],
        'inter_agent_communication_count': [2, 5, 1, 0, 3],
        'overall_project_completion_time_s': [60.1, 120.5, 90.2, 30.8, 70.4],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'task_complexity': [10, 20, 15, 5, 12],
        'num_specialized_agents': [3, 1, 2, 5, 1],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized', 'Decentralized'],
        'overall_success_rate': [0.95, 0.85, 0.75, 0.65, None]
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def create_invalid_types_dataframe():
    data = {
        'workflow_id': [1, 2, 3, 1, 2],
        'agent_role': ['Planner', 'Retriever', 'Summarizer', 'Planner', 'Retriever'],
        'subtask_id': [1, 2, 3, 4, 5],
        'subtask_status': ['Completed', 'InProgress', 'Completed', 'Failed', 'Completed'],
        'subtask_completion_time_s': [10.5, 20.2, 15.7, 5.1, 12.3],
        'inter_agent_communication_count': [2, 5, 1, 0, 3],
        'overall_project_completion_time_s': [60.1, 120.5, 90.2, 30.8, 70.4],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'task_complexity': [10, 20, 15, 5, 12],
        'num_specialized_agents': [3, 1, 2, 5, 1],
        'orchestration_strategy': ['Centralized', 'Decentralized', 'None', 'Centralized', 'Decentralized'],
        'overall_success_rate': ["a", 0.85, 0.75, 0.65, 0.90]
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df


def test_validate_and_preprocess_data_success():
    df = create_sample_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert 'system_type' in processed_df.columns
    assert all(processed_df['workflow_id'].value_counts() <= 2)


def test_validate_and_preprocess_data_missing_values():
    df = create_incomplete_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert 'system_type' in processed_df.columns

def test_validate_and_preprocess_data_system_type():
    df = create_sample_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert (processed_df.loc[processed_df['num_specialized_agents'] == 1, 'system_type'] == 'Single Agent AI').all()
    assert (processed_df.loc[processed_df['num_specialized_agents'] != 1, 'system_type'] == 'Agentic AI').all()

def test_validate_and_preprocess_data_no_dupes():
    df = create_sample_dataframe()
    processed_df = validate_and_preprocess_data(df.copy())
    assert not processed_df[['workflow_id', 'subtask_id']].duplicated().any()

def test_validate_and_preprocess_data_invalid_types():
    df = create_invalid_types_dataframe()
    with pytest.raises(TypeError):
        validate_and_preprocess_data(df.copy())
