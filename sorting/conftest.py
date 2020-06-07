import pytest

from sorting.Sorting import Sort


@pytest.fixture(scope="function")
def sort() -> Sort:
    return Sort()
