import pandas as pd
import numpy as np
import datetime

def generate_synthetic_data(num_workflows, max_subtasks):
    """Generates synthetic data for multi-agent workflows."""

    data = []
    for workflow_id in range(num_workflows):
        num_subtasks = np.random.randint(1, max_subtasks + 1)
        overall_project_completion_time_s = 0.0
        inter_agent_communication_count_total = 0

        for subtask_id in range(num_subtasks):
            agent_role = np.random.choice(['Analyst', 'Developer', 'Tester', 'Manager'])
            subtask_status = np.random.choice(['Pending', 'In Progress', 'Completed', 'Failed'])

            # Simulate completion time, influenced by orchestration strategy
            orchestration_strategy = np.random.choice(['Single Agent AI', 'Agentic AI'])

            # Simulate differences in performance
            if orchestration_strategy == 'Single Agent AI':
                subtask_completion_time_s = np.random.normal(loc=60, scale=20)  # Average longer time
            else:  # Agentic AI
                subtask_completion_time_s = np.random.normal(loc=30, scale=10)  # Faster completion

            subtask_completion_time_s = max(subtask_completion_time_s, 5)  # Ensure non-negative

            inter_agent_communication_count = np.random.randint(0, 5)
            inter_agent_communication_count_total += inter_agent_communication_count

            overall_project_completion_time_s += subtask_completion_time_s

            timestamp = datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 30))  # Recent timestamps
            task_complexity = np.random.randint(1, max_subtasks + 1) # Complexity based on max_subtasks
            num_specialized_agents = np.random.randint(1, 4)  # Number of agents involved

            # Model the impact of orchestration_strategy on overall_success_rate
            if orchestration_strategy == 'Single Agent AI':
                success_rate_base = 0.7
            else:
                success_rate_base = 0.9

            # Introduce randomness to success rate
            overall_success_rate = np.clip(np.random.normal(loc=success_rate_base, scale=0.1), 0.0, 1.0)

            data.append([workflow_id, agent_role, subtask_id, subtask_status, subtask_completion_time_s, inter_agent_communication_count, overall_project_completion_time_s, timestamp, task_complexity, num_specialized_agents, orchestration_strategy, overall_success_rate])

        #Correct the overall_project_completion_time_s in all subtasks for the workflow_id
        for i in range(len(data)):
            if data[i][0] == workflow_id:
                data[i][6] = overall_project_completion_time_s
                

    df = pd.DataFrame(data, columns=['workflow_id', 'agent_role', 'subtask_id', 'subtask_status', 'subtask_completion_time_s', 'inter_agent_communication_count', 'overall_project_completion_time_s', 'timestamp', 'task_complexity', 'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate'])
    
    if not df.empty:
        df['workflow_id'] = df['workflow_id'].astype(int)
        df['subtask_id'] = df['subtask_id'].astype(int)
        df['task_complexity'] = df['task_complexity'].astype(int)
        df['num_specialized_agents'] = df['num_specialized_agents'].astype(int)
        df['subtask_completion_time_s'] = df['subtask_completion_time_s'].astype(float)
        df['overall_project_completion_time_s'] = df['overall_project_completion_time_s'].astype(float)
        df['inter_agent_communication_count'] = df['inter_agent_communication_count'].astype(int)
        df['overall_success_rate'] = df['overall_success_rate'].astype(float)
        df['agent_role'] = df['agent_role'].astype(object)
        df['subtask_status'] = df['subtask_status'].astype(object)
        df['orchestration_strategy'] = df['orchestration_strategy'].astype(object)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
    return df

import pandas as pd

def validate_and_preprocess_data(df):
    """Validates and preprocesses the input DataFrame.
    Args:
        df: The pandas DataFrame to validate and preprocess.
    Returns:
        The processed pandas DataFrame.
    Raises:
        KeyError: If a required column is missing.
        ValueError: If there are duplicate workflow IDs or missing values in critical columns.
        TypeError: If the data type of a column is incorrect.
    """

    required_columns = ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status',
                        'subtask_completion_time_s', 'inter_agent_communication_count',
                        'overall_project_completion_time_s', 'timestamp', 'task_complexity',
                        'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']

    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Required column '{col}' is missing.")

    if not pd.api.types.is_numeric_dtype(df['workflow_id']):
        raise TypeError("workflow_id must be numeric")
    if not pd.api.types.is_numeric_dtype(df['subtask_id']):
        raise TypeError("subtask_id must be numeric")
    if not pd.api.types.is_numeric_dtype(df['subtask_completion_time_s']):
        raise TypeError("subtask_completion_time_s must be numeric")
    if not pd.api.types.is_numeric_dtype(df['inter_agent_communication_count']):
        raise TypeError("inter_agent_communication_count must be numeric")
    if not pd.api.types.is_numeric_dtype(df['overall_project_completion_time_s']):
        raise TypeError("overall_project_completion_time_s must be numeric")
    if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        raise TypeError("timestamp must be datetime")
    if not pd.api.types.is_numeric_dtype(df['task_complexity']):
        raise TypeError("task_complexity must be numeric")
    if not pd.api.types.is_numeric_dtype(df['num_specialized_agents']):
        raise TypeError("num_specialized_agents must be numeric")
    if not pd.api.types.is_numeric_dtype(df['overall_success_rate']):
        raise TypeError("overall_success_rate must be numeric")
    
    if df['workflow_id'].duplicated().any():
        raise ValueError("Duplicate workflow IDs found.")

    if df['subtask_completion_time_s'].isnull().any():
        raise ValueError("Missing values found in 'subtask_completion_time_s' column.")
    if df['inter_agent_communication_count'].isnull().any():
        raise ValueError("Missing values found in 'inter_agent_communication_count' column.")
    if df['overall_project_completion_time_s'].isnull().any():
        raise ValueError("Missing values found in 'overall_project_completion_time_s' column.")
    if df['task_complexity'].isnull().any():
        raise ValueError("Missing values found in 'task_complexity' column.")
    if df['num_specialized_agents'].isnull().any():
        raise ValueError("Missing values found in 'num_specialized_agents' column.")

    df['system_type'] = df['num_specialized_agents'].apply(
        lambda x: 'Single Agent AI' if x <= 1 else 'Agentic AI'
    )

    return df

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_project_completion_time(df):
    """Generates a line plot of project completion time vs. task complexity."""
    if df.empty:
        print("DataFrame is empty, cannot plot.")
        return

    try:
        sns.lineplot(x='task_complexity', y='overall_project_completion_time_s', hue='system_type', data=df)
        plt.xlabel('Task Complexity')
        plt.ylabel('Overall Project Completion Time (s)')
        plt.title('Project Completion Time vs. Task Complexity')
        plt.show()
    except KeyError as e:
        raise KeyError(f"Required column missing: {e}")
    except TypeError:
        raise TypeError("Task complexity must be numeric.")
    except ValueError as e:
        if "Could not convert" in str(e):
            raise TypeError("overall_project_completion_time_s must be numeric.")
        else:
             raise ValueError(e)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_communication_overhead(df):
    """Generates a scatter plot of communication overhead vs. completion time."""

    agentic_df = df[df['system_type'] == 'Agentic AI']
    if not agentic_df.empty:
        sns.scatterplot(x='inter_agent_communication_count', y='subtask_completion_time_s', data=agentic_df)
        plt.xlabel('Inter-Agent Communication Count')
        plt.ylabel('Subtask Completion Time (s)')
        plt.title('Communication Overhead vs. Completion Time for Agentic AI')
        plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_orchestration_comparison(df):
    """Generates bar charts comparing success rate and completion time across orchestration strategies.
    Args:
        df: DataFrame containing the data.
    """

    if df.empty:
        raise Exception("DataFrame is empty")

    required_columns = ['orchestration_strategy', 'overall_success_rate', 'average_project_completion_time_s', 'system_type']
    if not all(col in df.columns for col in required_columns):
        raise KeyError("Missing required columns")

    if not all(isinstance(x, str) for x in df['orchestration_strategy']):
        raise TypeError("orchestration_strategy must be strings")

    df = df[df['system_type'] == 'Agentic AI'].copy()

    if len(df) == 0:
        return

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    sns.barplot(x='orchestration_strategy', y='overall_success_rate', data=df)
    plt.title('Overall Success Rate vs. Orchestration Strategy')
    plt.xlabel('Orchestration Strategy')
    plt.ylabel('Overall Success Rate')

    plt.subplot(1, 2, 2)
    sns.barplot(x='orchestration_strategy', y='average_project_completion_time_s', data=df)
    plt.title('Average Project Completion Time vs. Orchestration Strategy')
    plt.xlabel('Orchestration Strategy')
    plt.ylabel('Average Project Completion Time (s)')

    plt.tight_layout()
    plt.show()

import ipywidgets as widgets

def setup_interactive_widgets():
    """Creates ipywidgets for interactive parameter selection."""

    task_type_selector = widgets.Dropdown(
        options=['Automated Grant Proposal Generation', 'Cybersecurity Incident Response'],
        description='Task Type:',
    )

    num_agents_slider = widgets.IntSlider(
        min=1,
        max=5,
        description='Number of Agents:',
    )

    orchestration_strategy_selector = widgets.Dropdown(
        options=['Centralized', 'Decentralized', 'None'],
        description='Orchestration:',
    )

    return task_type_selector, num_agents_slider, orchestration_strategy_selector

import pandas as pd

def run_interactive_analysis(task_type, num_agents, orchestration_strategy, original_df):
    """Filters data, calculates metrics, and displays output."""

    filtered_df = original_df[
        (original_df['task_type'] == task_type) &
        (original_df['num_specialized_agents'] == num_agents) &
        (original_df['orchestration_strategy'] == orchestration_strategy)
    ]

    if filtered_df.empty:
        print("No data matching the selected criteria.")
        return

    avg_completion_time = filtered_df['overall_project_completion_time_s'].mean()
    avg_success_rate = filtered_df['overall_success_rate'].mean()

    print(f"Task Type: {task_type}")
    print(f"Number of Agents: {num_agents}")
    print(f"Orchestration Strategy: {orchestration_strategy}")
    print(f"Average Completion Time: {avg_completion_time:.2f}")
    print(f"Average Success Rate: {avg_success_rate:.2f}")