# QuLab: Exploring Multi-Agent Orchestration in Agentic AI

## Project Description

This Streamlit application, **QuLab**, provides an interactive environment to explore the fundamental concepts of multi-agent orchestration and role specialization within Agentic AI systems. It simulates multi-agent workflows, allowing users to visualize the impact of different orchestration strategies, task types, and agent configurations on task completion time and system performance.  The lab aims to demonstrate how agentic systems, characterized by their collaborative nature, can achieve complex goals more efficiently and robustly compared to single-agent approaches.

## Features

*   **Interactive Data Simulation:** Generates synthetic datasets simulating multi-agent workflows, allowing for flexible parameter adjustments.
*   **Data Validation and Preprocessing:**  Includes data validation to check for critical columns, data types, missing values, and primary key uniqueness.  Provides summary statistics and data info.
*   **Trend Plot:** Visualizes the relationship between `task_complexity` and `overall_project_completion_time_s` for single-agent and multi-agent systems.
*   **Scatter Plot:** Shows the correlation between `inter_agent_communication_count` and `subtask_completion_time_s` in Agentic AI systems, highlighting communication overhead.
*   **Bar Charts:** Compares `overall_success_rate` and `average_project_completion_time_s` across different orchestration strategies.
*   **User Interaction:**  Streamlit's sidebar allows users to navigate through different pages (currently Page 1) and control parameters like `task_type`, `num_specialized_agents`, and `orchestration_strategy`.
*   **Clear Explanations:**  Includes comprehensive markdown text to explain key concepts, the purpose of visualizations, and the underlying principles of Agentic AI.

## Getting Started

### Prerequisites

*   Python 3.7 or higher
*   `pip` package manager

### Installation

1.  **Clone the repository (Optional):**  If you have the source code locally, navigate to the project directory. Otherwise, you can skip this step.
2.  **Create a virtual environment (Recommended):**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install streamlit pandas numpy seaborn matplotlib
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**  The application will open automatically in your default web browser, typically at `http://localhost:8501`.

3.  **Navigate the Pages:** Use the sidebar to select between "Page 1", "Page 2" and "Page 3" (although only Page 1 is fully functional).

4.  **Interpret the Visualizations:** Analyze the visualizations (currently only in Page 1) to understand the impact of different factors (task complexity, orchestration strategy, etc.) on agentic system performance.

## Project Structure

```
QuLab/
├── app.py              # Main Streamlit application file
├── application_pages/
│   ├── page1.py        # Script containing the logic and visualizations for Page 1
│   ├── page2.py        # Script containing the logic for Page 2
│   └── page3.py        # Script containing the logic for Page 3
├── .venv/              # Virtual environment (if created)
├── README.md           # This file
```

## Technology Stack

*   **Python:** Programming language.
*   **Streamlit:** Framework for creating interactive web applications.
*   **Pandas:** Data manipulation and analysis library.
*   **NumPy:** Numerical computing library.
*   **Seaborn:** Data visualization library based on Matplotlib.
*   **Matplotlib:**  Plotting library.

## Contributing

Currently, this project is a learning lab and isn't actively accepting contributions.  However, feel free to fork the repository and experiment with the code. If you find bugs or have suggestions for improvements, feel free to create an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (Note: While there's no license file currently, it's good practice to include one. A basic MIT license file can be easily generated.)

## Contact

For questions or suggestions, please create an issue on the repository, or contact the project maintainer.
