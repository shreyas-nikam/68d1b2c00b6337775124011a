
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO


@st.cache_data
def generate_synthetic_data(num_workflows=100, max_subtasks=50):
    data = []
    task_types = ['Automated Grant Proposal', 'Cybersecurity Incident Response', 'General Task']
    for workflow_id in range(num_workflows):
        num_subtasks = np.random.randint(1, max_subtasks + 1)
        workflow_task_type = np.random.choice(task_types)

        for subtask_id in range(num_subtasks):
            agent_role = np.random.choice(['Planner', 'Retriever', 'Summarizer', 'Formatter', 'Orchestrator', 'Generalist'])
            subtask_status = np.random.choice(['Pending', 'InProgress', 'Completed', 'Failed'])
            subtask_completion_time_s = np.random.uniform(10, 3600) if subtask_status == 'Completed' else 0
            inter_agent_communication_count = np.random.randint(0, 10)
            overall_project_completion_time_s = np.random.uniform(3600, 86400)
            task_complexity = np.random.randint(1, 10)
            if workflow_task_type == 'Automated Grant Proposal':
                task_complexity = np.random.randint(6, 10)
            elif workflow_task_type == 'Cybersecurity Incident Response':
                task_complexity = np.random.randint(4, 8)
            else:  # General Task
                task_complexity = np.random.randint(1, 5)

            num_specialized_agents = np.random.randint(1, 5)
            orchestration_strategy = np.random.choice(['Centralized', 'Decentralized', 'None'])
            overall_success_rate = np.random.uniform(0.5, 1.0)

            data.append({
                'workflow_id': workflow_id,
                'agent_role': agent_role,
                'subtask_id': subtask_id,
                'subtask_status': subtask_status,
                'subtask_completion_time_s': subtask_completion_time_s,
                'inter_agent_communication_count': inter_agent_communication_count,
                'overall_project_completion_time_s': overall_project_completion_time_s,
                'task_complexity': task_complexity,
                'num_specialized_agents': num_specialized_agents,
                'orchestration_strategy': orchestration_strategy,
                'overall_success_rate': overall_success_rate,
                'task_type': workflow_task_type  # Add task_type to dataframe
            })

    df = pd.DataFrame(data)
    df['system_type'] = np.random.choice(['Single Agent AI', 'Agentic AI'], size=len(df))
    df.loc[df['system_type'] == 'Single Agent AI', 'orchestration_strategy'] = 'None'
    df.loc[df['system_type'] == 'Single Agent AI', 'num_specialized_agents'] = 1
    df.loc[(df['system_type'] == 'Agentic AI') & (df['num_specialized_agents'] == 1), 'num_specialized_agents'] = np.random.randint(2, 5)
    return df


def validate_and_preprocess_data(df):
    expected_cols = {
        'workflow_id': np.int64,
        'agent_role': object,
        'subtask_id': np.int64,
        'subtask_status': object,
        'subtask_completion_time_s': np.float64,
        'inter_agent_communication_count': np.int64,
        'overall_project_completion_time_s': np.float64,
        # 'timestamp': 'datetime64[ns]',
        'task_complexity': np.int64,
        'num_specialized_agents': np.int64,
        'orchestration_strategy': object,
        'overall_success_rate': np.float64,
        'system_type': object,
        'task_type': object
    }

    for col, dtype in expected_cols.items():
        if col not in df.columns:
            st.error(f"Missing critical column: {col}")
            st.stop()
        if not pd.api.types.is_dtype_equal(df[col].dtype, dtype) and dtype != object:
            try:
                df[col] = df[col].astype(dtype)
            except ValueError:
                st.warning(f"Column '{col}' expected type {dtype} but found {df[col].dtype}. Attempted conversion.")

    critical_fields = ['overall_project_completion_time_s', 'overall_success_rate']
    for field in critical_fields:
        if df[field].isnull().any():
            st.warning(f"Missing values found in '{field}'. Consider imputation or removal.")
            df.dropna(subset=[field], inplace=True)

    if not df[['workflow_id', 'subtask_id']].duplicated().any():
        st.success("Primary key (workflow_id, subtask_id) is unique.")
    else:
        st.warning("Duplicate primary keys found (workflow_id, subtask_id).")
        df.drop_duplicates(subset=['workflow_id', 'subtask_id'], inplace=True)

    st.write("### Summary Statistics for Numeric Columns")
    st.dataframe(df.describe())

    st.write("### Data Information (concise summary)")
    buffer = StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    return df


# Visualization Functions
def plot_project_completion_time(df):
    st.write("## Visualizing Project Completion Time by Task Complexity")
    st.markdown("""
    This section visualizes how `overall_project_completion_time_s` changes with `task_complexity` for both 'Single Agent AI' and 'Agentic AI' systems. We expect to see that Agentic AI systems maintain lower completion times, especially as tasks become more complex, demonstrating the benefits of parallelization and specialization.
    """)

    plot_df = df.groupby(['task_complexity', 'system_type'])['overall_project_completion_time_s'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=plot_df, x='task_complexity', y='overall_project_completion_time_s', hue='system_type', marker='o', ax=ax)
    ax.set_title('Average Project Completion Time vs. Task Complexity')
    ax.set_xlabel('Task Complexity (1-10)')
    ax.set_ylabel('Average Completion Time (seconds)')
    ax.legend(title='System Type')
    st.pyplot(fig)

def plot_communication_overhead(df):
    st.write("## Analyzing Communication Overhead in Agentic AI Systems")
    st.markdown("""
    In multi-agent systems, inter-agent communication is essential but can also introduce overhead. This scatter plot helps us visualize the relationship between the `inter_agent_communication_count` and `subtask_completion_time_s` specifically within Agentic AI scenarios. Understanding this relationship can shed light on coordination costs versus benefits.
    """)

    agentic_df = df[df['system_type'] == 'Agentic AI']

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=agentic_df, x='inter_agent_communication_count', y='subtask_completion_time_s', alpha=0.6, ax=ax)
    ax.set_title('Communication Overhead vs. Subtask Completion Time in Agentic AI')
    ax.set_xlabel('Inter-Agent Communication Count')
    ax.set_ylabel('Subtask Completion Time (seconds)')
    st.pyplot(fig)

def plot_orchestration_comparison(df):
    st.write("## Comparing Orchestration Strategies: Success Rate and Average Completion Time")
    st.markdown("""
    Orchestration strategies significantly influence the performance of Agentic AI systems. This section compares the `overall_success_rate` and `average_project_completion_time_s` across different `orchestration_strategies` to evaluate their effectiveness. We expect 'Centralized' or 'Decentralized' strategies to outperform 'None' for Agentic AI.
    """)

    agentic_df = df[df['system_type'] == 'Agentic AI']

    agg_df = agentic_df.groupby('orchestration_strategy').agg(
        avg_completion_time=('overall_project_completion_time_s', 'mean'),
        avg_success_rate=('overall_success_rate', 'mean')
    ).reset_index()

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    sns.barplot(data=agg_df, x='orchestration_strategy', y='avg_success_rate', ax=axes[0])
    axes[0].set_title('Overall Success Rate by Orchestration Strategy (Agentic AI)')
    axes[0].set_xlabel('Orchestration Strategy')
    axes[0].set_ylabel('Average Success Rate')
    axes[0].set_ylim(0, 1)

    sns.barplot(data=agg_df, x='orchestration_strategy', y='avg_completion_time', ax=axes[1])
    axes[1].set_title('Average Project Completion Time by Orchestration Strategy (Agentic AI)')
    axes[1].set_xlabel('Orchestration Strategy')
    axes[1].set_ylabel('Average Completion Time (seconds)')

    plt.tight_layout()
    st.pyplot(fig)


# Main Page Content
@st.cache_data
def load_and_process_data():
    df = generate_synthetic_data()
    validated_df = validate_and_preprocess_data(df)
    return validated_df


def run_page1():
    st.title("Data Overview and Validation")
    st.markdown("""
    This page provides an overview of the generated synthetic data and performs validation checks to ensure data integrity.
    """)

    validated_df = load_and_process_data()

    st.markdown("### Raw Data Preview")
    st.dataframe(validated_df.head())
    plot_project_completion_time(validated_df)
    plot_communication_overhead(validated_df)
    plot_orchestration_comparison(validated_df)

if __name__ == "__main__":
    run_page1()
