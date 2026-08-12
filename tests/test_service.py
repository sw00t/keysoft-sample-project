import pytest

from orders import store
from orders.models import Order
from orders.service import cancel_order


def test_cancel_pending_order():
    store.put(Order("T-1", "Test User", 10.0, "pending"))
    result = cancel_order("T-1")
    assert result.status == "cancelled"


def test_cancel_unknown_order_raises():
    with pytest.raises(KeyError):
        cancel_order("does-not-exist")


def test_cannot_cancel_shipped_order():
    store.put(Order("T-2", "Test User", 10.0, "shipped"))
    with pytest.raises(ValueError):
        cancel_order("T-2")
