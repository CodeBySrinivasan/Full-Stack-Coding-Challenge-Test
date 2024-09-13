import pytest
from secret_santa import assign_santas

def test_assign_santas():
    participants = ["Alice", "Bob", "Charlie", "David"]
    assignments = assign_santas(participants)

    assert len(assignments) == len(participants)
    for participant in participants:
        assert participant in assignments
        assert assignments[participant] != participant  # Ensure no one is their own Santa

def test_assign_santas_error():
    with pytest.raises(ValueError):
        assign_santas(["Alice"])
