import pandas as pd
import numpy as np
import datetime

def generate_synthetic_data(num_workflows, max_subtasks):
    """Generates synthetic workflow data.

    Args:
        num_workflows (int): Number of workflows.
        max_subtasks (int): Max subtasks per workflow.

    Returns:
        pd.DataFrame: Synthetic data.
    """

    data = []
    for workflow_id in range(num_workflows):
        num_subtasks = np.random.randint(0, max_subtasks + 1)
        for subtask_id in range(num_subtasks):
            agent_role = np.random.choice(['analyst', 'developer', 'tester', 'manager'])
            subtask_status = np.random.choice(['pending', 'in progress', 'completed', 'failed'])
            subtask_completion_time_s = np.random.exponential(scale=60)
            inter_agent_communication_count = np.random.randint(0, 10)
            overall_project_completion_time_s = np.random.exponential(scale=3600)
            timestamp = datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 30))
            task_complexity = np.random.randint(1, 6)
            num_specialized_agents = np.random.randint(1, 4)
            orchestration_strategy = np.random.choice(['centralized', 'distributed', 'hybrid'])
            overall_success_rate = np.random.uniform(0, 1)

            data.append([workflow_id, agent_role, subtask_id, subtask_status,
                         subtask_completion_time_s, inter_agent_communication_count,
                         overall_project_completion_time_s, timestamp, task_complexity,
                         num_specialized_agents, orchestration_strategy, overall_success_rate])

    df = pd.DataFrame(data, columns=['workflow_id', 'agent_role', 'subtask_id', 'subtask_status',
                                     'subtask_completion_time_s', 'inter_agent_communication_count',
                                     'overall_project_completion_time_s', 'timestamp', 'task_complexity',
                                     'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate'])
    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

import pandas as pd
import numpy as np

def validate_and_preprocess_data(df):
    """Performs validation and preprocessing."""

    # Column name and data type validation (example, can be extended)
    expected_columns = ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status',
                        'subtask_completion_time_s', 'inter_agent_communication_count',
                        'overall_project_completion_time_s', 'timestamp', 'task_complexity',
                        'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']
    if not all(col in df.columns for col in expected_columns):
        raise ValueError("Missing expected columns")
    
    if not pd.api.types.is_numeric_dtype(df['overall_success_rate']):
        raise TypeError("overall_success_rate must be numeric")

    # Check for workflow_id and subtask_id uniqueness
    if df[['workflow_id', 'subtask_id']].duplicated().any():
        df = df.drop_duplicates(subset=['workflow_id', 'subtask_id'], keep='first')

    # Check for missing values in critical columns
    critical_columns = ['subtask_completion_time_s', 'overall_project_completion_time_s', 'task_complexity', 'overall_success_rate']
    if df[critical_columns].isnull().any().any():
        df = df.dropna(subset=critical_columns)


    # Calculate and log descriptive statistics for numeric columns (example)
    numeric_columns = df.select_dtypes(include=np.number).columns
    #print(df[numeric_columns].describe())  # Logging statistics would be done here.

    # Create system_type column
    df['system_type'] = df['num_specialized_agents'].apply(lambda x: 'Single Agent AI' if x == 1 else 'Agentic AI')

    return df

import pandas as pd
import matplotlib.pyplot as plt

def plot_project_completion_time(df):
    """Generates a line plot of project completion time vs. task complexity, differentiated by system type."""

    if df.empty:
        raise Exception("DataFrame is empty")

    required_columns = ['overall_project_completion_time_s', 'task_complexity', 'system_type']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' missing in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df['task_complexity']):
        raise TypeError("Task complexity must be numeric")

    system_types = df['system_type'].unique()

    plt.figure(figsize=(10, 6))
    for system_type in system_types:
        subset = df[df['system_type'] == system_type]
        plt.plot(subset['task_complexity'], subset['overall_project_completion_time_s'], marker='o', label=system_type)

    plt.xlabel('Task Complexity')
    plt.ylabel('Overall Project Completion Time (s)')
    plt.title('Project Completion Time vs. Task Complexity by System Type')
    plt.legend()
    plt.grid(True)
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def plot_communication_overhead(df):
    """Generates a scatter plot for Agentic AI communication overhead."""
    try:
        agentic_ai_data = df[df['system_type'] == 'Agentic AI'].copy()

        if agentic_ai_data.empty:
            print("No 'Agentic AI' data found. Skipping plot.")
            return

        agentic_ai_data.loc[:, 'inter_agent_communication_count'] = pd.to_numeric(agentic_ai_data['inter_agent_communication_count'])
        agentic_ai_data.loc[:, 'subtask_completion_time_s'] = pd.to_numeric(agentic_ai_data['subtask_completion_time_s'])
        
        plt.figure(figsize=(8, 6))
        plt.scatter(agentic_ai_data['inter_agent_communication_count'], agentic_ai_data['subtask_completion_time_s'])
        plt.xlabel('Inter-Agent Communication Count')
        plt.ylabel('Subtask Completion Time (s)')
        plt.title('Communication Overhead for Agentic AI')
        plt.grid(True)
        plt.show()

    except KeyError as e:
        raise KeyError(f"Required column missing: {e}")
    except TypeError:
        raise TypeError("Invalid data type in DataFrame.  'inter_agent_communication_count' and 'subtask_completion_time_s' must be numeric.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_orchestration_comparison(df):
    """Generates bar charts comparing success rate and completion time.
    Args:
        df (pandas.DataFrame): DataFrame containing the data.
    """
    if df.empty:
        return

    # Check if required columns exist
    required_columns = ['orchestration_strategy', 'overall_success_rate', 'average_project_completion_time_s']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' missing in DataFrame.")
    
    # Check if 'overall_success_rate' and 'average_project_completion_time_s' are numeric
    if not pd.api.types.is_numeric_dtype(df['overall_success_rate']):
        raise TypeError("Column 'overall_success_rate' must be numeric.")
    if not pd.api.types.is_numeric_dtype(df['average_project_completion_time_s']):
        raise TypeError("Column 'average_project_completion_time_s' must be numeric.")

    # Create the first bar plot for overall success rate
    plt.figure(figsize=(10, 6))
    sns.barplot(x='orchestration_strategy', y='overall_success_rate', data=df)
    plt.title('Overall Success Rate by Orchestration Strategy')
    plt.xlabel('Orchestration Strategy')
    plt.ylabel('Overall Success Rate')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Create the second bar plot for average project completion time
    plt.figure(figsize=(10, 6))
    sns.barplot(x='orchestration_strategy', y='average_project_completion_time_s', data=df)
    plt.title('Average Project Completion Time by Orchestration Strategy')
    plt.xlabel('Orchestration Strategy')
    plt.ylabel('Average Project Completion Time (s)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

import ipywidgets as widgets

def setup_interactive_widgets():
    """Creates and returns ipywidgets objects."""

    task_type_selector = widgets.Dropdown(
        options=['Automated Grant Proposal Generation', 'Cybersecurity Incident Response'],
        description='Task Type:'
    )

    num_agents_slider = widgets.IntSlider(
        min=1,
        max=5,
        step=1,
        description='Number of Agents:'
    )

    orchestration_strategy_selector = widgets.Dropdown(
        options=['Centralized', 'Decentralized', 'None'],
        description='Orchestration:'
    )

    return task_type_selector, num_agents_slider, orchestration_strategy_selector

import pandas as pd

def run_interactive_analysis(task_type, num_agents, orchestration_strategy, original_df):
    """Filters, calculates, and displays metrics based on input parameters."""

    if not isinstance(original_df, pd.DataFrame):
        raise TypeError("original_df must be a pandas DataFrame.")

    try:
        # Filter the DataFrame
        filtered_df = original_df[
            (original_df['task_type'] == task_type) &
            (original_df['num_agents'] == num_agents) &
            (original_df['orchestration_strategy'] == orchestration_strategy)
        ]

        # Calculate and display aggregated metrics if filtered_df is not empty
        if not filtered_df.empty:
            print(f"Analysis for Task Type: {task_type}, Num Agents: {num_agents}, Strategy: {orchestration_strategy}")
            print("-" * 50)

            # Example: Calculate and display the mean of the 'data' column
            if 'data' in filtered_df.columns:
                average_data = filtered_df['data'].mean()
                print(f"Average Data Value: {average_data:.2f}")
            else:
                print("No 'data' column found in the filtered DataFrame.")

            # Add more metric calculations and display as needed.

        else:
            print("No data found matching the specified criteria.")

    except Exception as e:
        print(f"An error occurred during analysis: {e}")