"""Order business logic."""
import logging

from orders import store
from orders.models import Order

logger = logging.getLogger(__name__)


def cancel_order(order_id: str) -> Order:
    """Cancel a pending order and return the updated order.

    Raises KeyError if the order is unknown, ValueError if it can't be cancelled.
    """
    order = store.fetch(order_id)
    if order is None:
        raise KeyError(f"unknown order: {order_id}")
    if order.status != "pending":
        raise ValueError(f"cannot cancel a {order.status} order")
    order.status = "cancelled"
    store.put(order)
    logger.info("cancelled order %s", order_id)
    return order
