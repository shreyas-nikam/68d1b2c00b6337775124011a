import pytest
from definition_e3819155a6d6455cac7f70552d5dceff import setup_interactive_widgets
import ipywidgets as widgets

def test_setup_interactive_widgets_returns_widgets():
    task_type_selector, num_agents_slider, orchestration_strategy_selector = setup_interactive_widgets()
    assert isinstance(task_type_selector, widgets.Dropdown)
    assert isinstance(num_agents_slider, widgets.IntSlider)
    assert isinstance(orchestration_strategy_selector, widgets.Dropdown)

def test_setup_interactive_widgets_task_type_options():
    task_type_selector, _, _ = setup_interactive_widgets()
    assert task_type_selector.options == ['Automated Grant Proposal Generation', 'Cybersecurity Incident Response']

def test_setup_interactive_widgets_num_agents_range():
    _, num_agents_slider, _ = setup_interactive_widgets()
    assert num_agents_slider.min == 1
    assert num_agents_slider.max == 5
    assert num_agents_slider.step == 1

def test_setup_interactive_widgets_orchestration_options():
    _, _, orchestration_strategy_selector = setup_interactive_widgets()
    assert orchestration_strategy_selector.options == ['Centralized', 'Decentralized', 'None']

def test_setup_interactive_widgets_descriptions():
    task_type_selector, num_agents_slider, orchestration_strategy_selector = setup_interactive_widgets()
    assert task_type_selector.description == 'Task Type:'
    assert num_agents_slider.description == 'Number of Agents:'
    assert orchestration_strategy_selector.description == 'Orchestration:'

