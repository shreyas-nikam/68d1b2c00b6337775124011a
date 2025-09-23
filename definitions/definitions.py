import pandas as pd
import numpy as np

def generate_synthetic_data(num_workflows, max_subtasks):
    """Generates synthetic workflow data.

    Args:
        num_workflows (int): Number of workflows.
        max_subtasks (int): Max subtasks per workflow.

    Returns:
        pd.DataFrame: Synthetic data.
    """
    if num_workflows < 0 or max_subtasks < 0:
        raise ValueError("Number of workflows and max_subtasks must be non-negative.")

    if num_workflows == 0 or max_subtasks == 0:
        return None

    data = []
    for workflow_id in range(num_workflows):
        num_subtasks = np.random.randint(1, max_subtasks + 1)
        for subtask_id in range(num_subtasks):
            agent_role = np.random.choice(['analyst', 'developer', 'tester'])
            subtask_status = np.random.choice(['pending', 'in_progress', 'completed', 'failed'])
            subtask_completion_time_s = np.random.uniform(10, 3600) if subtask_status == 'completed' else 0
            inter_agent_communication_count = np.random.randint(0, 10)
            overall_project_completion_time_s = np.random.uniform(3600, 86400)
            timestamp = pd.Timestamp.now()
            task_complexity = np.random.choice(['low', 'medium', 'high'])
            num_specialized_agents = np.random.randint(1, 5)
            orchestration_strategy = np.random.choice(['centralized', 'decentralized', 'hybrid'])
            overall_success_rate = np.random.uniform(0.5, 1.0)

            data.append({
                'workflow_id': workflow_id,
                'agent_role': agent_role,
                'subtask_id': subtask_id,
                'subtask_status': subtask_status,
                'subtask_completion_time_s': subtask_completion_time_s,
                'inter_agent_communication_count': inter_agent_communication_count,
                'overall_project_completion_time_s': overall_project_completion_time_s,
                'timestamp': timestamp,
                'task_complexity': task_complexity,
                'num_specialized_agents': num_specialized_agents,
                'orchestration_strategy': orchestration_strategy,
                'overall_success_rate': overall_success_rate
            })

    df = pd.DataFrame(data)
    return df if not df.empty else None

import pandas as pd
import numpy as np

def validate_and_preprocess_data(df):
    """Performs validation and preprocessing on the DataFrame."""

    # Column Name and Data Type Validation
    expected_columns = ['workflow_id', 'agent_role', 'subtask_id', 'subtask_status',
                        'subtask_completion_time_s', 'inter_agent_communication_count',
                        'overall_project_completion_time_s', 'timestamp', 'task_complexity',
                        'num_specialized_agents', 'orchestration_strategy', 'overall_success_rate']
    if not all(col in df.columns for col in expected_columns):
        raise ValueError("Missing required columns")
    
    # Check data types
    if not pd.api.types.is_numeric_dtype(df['workflow_id']):
        raise TypeError("workflow_id must be numeric")
    
    # Check for `workflow_id` and `subtask_id` uniqueness
    if not df[['workflow_id', 'subtask_id']].duplicated().any() == False:
        raise ValueError("workflow_id and subtask_id are not unique")

    # Check for missing values in critical columns
    critical_columns = ['subtask_completion_time_s', 'overall_project_completion_time_s', 'overall_success_rate']
    for col in critical_columns:
        if df[col].isnull().any():
            print(f"Warning: Missing values found in column '{col}'")

    # Calculate and log descriptive statistics for numeric columns
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    print("Descriptive Statistics:")
    print(df[numeric_columns].describe())

    # Create a `system_type` column
    df['system_type'] = df['num_specialized_agents'].apply(
        lambda x: 'Single Agent AI' if x <= 1 else 'Agentic AI')

    return df

import pandas as pd
import matplotlib.pyplot as plt

def plot_project_completion_time(df):
    """Plots project completion time vs. task complexity for different system types."""

    if df.empty:
        print("DataFrame is empty. No plot will be generated.")
        return

    if not all(col in df.columns for col in ['overall_project_completion_time_s', 'task_complexity', 'system_type']):
        raise KeyError("DataFrame must contain 'overall_project_completion_time_s', 'task_complexity', and 'system_type' columns.")

    if not pd.api.types.is_numeric_dtype(df['task_complexity']):
        raise TypeError("The 'task_complexity' column must be numeric.")

    plt.figure(figsize=(10, 6))
    for system_type in df['system_type'].unique():
        subset = df[df['system_type'] == system_type]
        subset = subset.sort_values('task_complexity')
        plt.plot(subset['task_complexity'], subset['overall_project_completion_time_s'], marker='o', label=system_type)

    plt.xlabel('Task Complexity')
    plt.ylabel('Overall Project Completion Time (s)')
    plt.title('Project Completion Time vs. Task Complexity')
    plt.legend()
    plt.grid(True)
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def plot_communication_overhead(df):
    """Plots communication overhead for Agentic AI."""
    if df.empty:
        return

    agentic_df = df[df['system_type'] == 'Agentic AI']

    if agentic_df.empty:
        return
    
    try:
        plt.figure(figsize=(8, 6))
        plt.scatter(agentic_df['inter_agent_communication_count'], agentic_df['subtask_completion_time_s'])
        plt.xlabel('Inter-Agent Communication Count')
        plt.ylabel('Subtask Completion Time (s)')
        plt.title('Communication Overhead for Agentic AI')
        plt.grid(True)
        plt.show()
    except KeyError as e:
        raise KeyError(f"Required column missing: {e}")
    except TypeError:
        raise TypeError("Invalid data types for plotting.")

import pandas as pd
import matplotlib.pyplot as plt

def plot_orchestration_comparison(df):
    """
    Generates bar charts comparing the `overall_success_rate` and `average_project_completion_time_s` for different `orchestration_strategies`.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to plot.

    Returns:
        None: Displays the plot.
    """
    if df.empty:
        raise ValueError("Input DataFrame is empty.")

    if not all(col in df.columns for col in ['orchestration_strategy', 'overall_success_rate', 'overall_project_completion_time_s', 'system_type']):
        raise KeyError("Missing required columns in DataFrame.")

    agentic_ai_data = df[df['system_type'] == 'Agentic AI']
    if agentic_ai_data.empty:
        raise ValueError("No 'Agentic AI' data to plot.")

    # Group by orchestration strategy and calculate the mean of the metrics
    grouped_data = agentic_ai_data.groupby('orchestration_strategy').agg(
        overall_success_rate=('overall_success_rate', 'mean'),
        average_project_completion_time_s=('overall_project_completion_time_s', 'mean')
    )

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot overall success rate
    grouped_data['overall_success_rate'].plot(kind='bar', ax=axes[0], color='skyblue')
    axes[0].set_title('Overall Success Rate by Orchestration Strategy')
    axes[0].set_xlabel('Orchestration Strategy')
    axes[0].set_ylabel('Success Rate')
    axes[0].set_ylim(0, 1)  # Assuming success rate is between 0 and 1
    axes[0].tick_params(axis='x', rotation=45)

    # Plot average project completion time
    grouped_data['average_project_completion_time_s'].plot(kind='bar', ax=axes[1], color='lightcoral')
    axes[1].set_title('Average Project Completion Time by Orchestration Strategy')
    axes[1].set_xlabel('Orchestration Strategy')
    axes[1].set_ylabel('Completion Time (s)')
    axes[1].tick_params(axis='x', rotation=45)

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

import ipywidgets as widgets

def setup_interactive_widgets():
    """Creates ipywidgets for task type, num agents, and orchestration strategy."""

    task_type_selector = widgets.Dropdown(
        options=['Automated Grant Proposal Generation', 'Cybersecurity Incident Response'],
        description='Task Type:'
    )

    num_agents_slider = widgets.IntSlider(
        min=1,
        max=5,
        step=1,
        value=3,
        description='Number of Agents:'
    )

    orchestration_strategy_selector = widgets.Dropdown(
        options=['Centralized', 'Decentralized', 'None'],
        description='Orchestration:'
    )

    return task_type_selector, num_agents_slider, orchestration_strategy_selector

import pandas as pd

def run_interactive_analysis(task_type, num_agents, orchestration_strategy, original_df):
    """Filters data, calculates metrics, and displays results."""

    if not isinstance(task_type, str):
        raise TypeError("Task type must be a string.")

    if original_df.empty:
        raise Exception("DataFrame is empty.")

    filtered_df = original_df[
        (original_df['task_type'] == task_type) &
        (original_df['num_agents'] == num_agents) &
        (original_df['orchestration_strategy'] == orchestration_strategy)
    ]

    if filtered_df.empty:
        print("No data matching the selected criteria.")
        return

    average_value = filtered_df['value'].mean()
    print(f"Average Value: {average_value}")