"""In-memory order store. Stands in for a real database."""
from orders.models import Order

_ORDERS: dict[str, Order] = {
    "A-10422": Order("A-10422", "Ada Lovelace", 89.0, "shipped"),
    "A-10423": Order("A-10423", "Alan Turing", 42.5, "pending"),
}


def fetch(order_id: str) -> Order | None:
    return _ORDERS.get(order_id)


def put(order: Order) -> None:
    _ORDERS[order.order_id] = order
