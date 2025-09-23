import pytest
from definition_0a5607c802584e36986ab2c55cd55256 import generate_synthetic_data

@pytest.mark.parametrize("num_workflows, max_subtasks, expected_type", [
    (10, 5, type(None)),
    (0, 10, type(None)),
    (5, 0, type(None)),
    (-1, 5, pytest.raises(ValueError)),
    (5, -1, pytest.raises(ValueError)),
])
def test_generate_synthetic_data(num_workflows, max_subtasks, expected_type):
    if isinstance(expected_type, type) and issubclass(expected_type, Exception):
        with expected_type:
            generate_synthetic_data(num_workflows, max_subtasks)
    else:
        result = generate_synthetic_data(num_workflows, max_subtasks)
        assert result is None

