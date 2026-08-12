import copy

import pytest

from orders import store


@pytest.fixture(autouse=True)
def reset_store():
    """Snapshot the in-memory store before each test and restore it after."""
    original = copy.deepcopy(store._ORDERS)
    yield
    store._ORDERS.clear()
    store._ORDERS.update(original)
