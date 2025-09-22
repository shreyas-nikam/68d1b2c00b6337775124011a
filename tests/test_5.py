import pytest
from definition_2bd8010fb79546eba79fd01b1b49bd61 import setup_interactive_widgets
import ipywidgets as widgets

def test_setup_interactive_widgets_returns_tuple():
    result = setup_interactive_widgets()
    assert isinstance(result, tuple)
    assert len(result) == 3

def test_setup_interactive_widgets_correct_widget_types():
    task_type_selector, num_agents_slider, orchestration_strategy_selector = setup_interactive_widgets()
    assert isinstance(task_type_selector, widgets.Dropdown)
    assert isinstance(num_agents_slider, widgets.IntSlider)
    assert isinstance(orchestration_strategy_selector, widgets.Dropdown)

def test_setup_interactive_widgets_dropdown_options():
    task_type_selector, _, orchestration_strategy_selector = setup_interactive_widgets()
    assert task_type_selector.options == ['Automated Grant Proposal Generation', 'Cybersecurity Incident Response']
    assert orchestration_strategy_selector.options == ['Centralized', 'Decentralized', 'None']

def test_setup_interactive_widgets_slider_range():
    _, num_agents_slider, _ = setup_interactive_widgets()
    assert num_agents_slider.min == 1
    assert num_agents_slider.max == 5

def test_setup_interactive_widgets_descriptions():
    task_type_selector, num_agents_slider, orchestration_strategy_selector = setup_interactive_widgets()
    assert task_type_selector.description == 'Task Type:'
    assert num_agents_slider.description == 'Number of Agents:'
    assert orchestration_strategy_selector.description == 'Orchestration:'
