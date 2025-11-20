from ..client import get_client
from ..utils.validator import validate_symbol, validate_quantity, validate_price
from ..utils.logger import get_logger

logger = get_logger("grid")

def create_grid_orders(symbol, low, high, levels, qty_each):
    validate_symbol(symbol)
    low = validate_price(low)
    high = validate_price(high)
    qty_each = validate_quantity(qty_each)

    step = (high - low) / (levels - 1)
    client = get_client()
    orders = []

    for i in range(levels):
        price = low + i * step
        res = client.place_limit_order(symbol, "BUY", qty_each, price)
        orders.append(res)
        logger.info(f"Grid order: {res}")

    return orders
