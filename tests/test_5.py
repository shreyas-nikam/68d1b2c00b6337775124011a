import pytest
from definition_bb4120d26c6042e0b3fa24c8f5f27934 import setup_interactive_widgets
import ipywidgets as widgets

def test_setup_interactive_widgets_returns_widgets():
    widgets = setup_interactive_widgets()
    assert isinstance(widgets, tuple)
    assert len(widgets) == 3
    assert all(isinstance(w, widgets.Widget) for w in widgets)

def test_setup_interactive_widgets_task_type():
    task_type_selector, _, _ = setup_interactive_widgets()
    assert isinstance(task_type_selector, widgets.Dropdown)
    assert task_type_selector.options == ['Automated Grant Proposal Generation', 'Cybersecurity Incident Response']
    assert task_type_selector.description == 'Task Type:'

def test_setup_interactive_widgets_num_agents():
    _, num_agents_slider, _ = setup_interactive_widgets()
    assert isinstance(num_agents_slider, widgets.IntSlider)
    assert num_agents_slider.min == 1
    assert num_agents_slider.max == 5
    assert num_agents_slider.step == 1
    assert num_agents_slider.value == 3
    assert num_agents_slider.description == 'Number of Agents:'

def test_setup_interactive_widgets_orchestration():
    _, _, orchestration_strategy_selector = setup_interactive_widgets()
    assert isinstance(orchestration_strategy_selector, widgets.Dropdown)
    assert orchestration_strategy_selector.options == ['Centralized', 'Decentralized', 'None']
    assert orchestration_strategy_selector.description == 'Orchestration:'

def test_setup_interactive_widgets_returns_different_objects():
    task_type_selector, num_agents_slider, orchestration_strategy_selector = setup_interactive_widgets()
    assert task_type_selector is not num_agents_slider
    assert task_type_selector is not orchestration_strategy_selector
    assert num_agents_slider is not orchestration_strategy_selector
