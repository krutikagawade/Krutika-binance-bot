from .client import get_client
from .utils.validator import validate_symbol, validate_side, validate_quantity, validate_price
from .utils.logger import get_logger

logger = get_logger("limit_orders")

def place_limit(symbol, side, qty, price):
    if not validate_symbol(symbol):
        raise ValueError("Invalid symbol")
    side = validate_side(side)
    qty = validate_quantity(qty)
    price = validate_price(price)

    client = get_client()
    result = client.place_limit_order(symbol, side, qty, price)
    logger.info(f"Result: {result}")
    return result
