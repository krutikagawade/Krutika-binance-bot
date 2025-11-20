from .client import get_client
from .utils.validator import validate_symbol, validate_side, validate_quantity
from .utils.logger import get_logger

logger = get_logger("market_orders")

def place_market(symbol, side, qty):
    if not validate_symbol(symbol):
        raise ValueError("Invalid symbol")
    side = validate_side(side)
    qty = validate_quantity(qty)

    client = get_client()
    result = client.place_market_order(symbol, side, qty)
    logger.info(f"Result: {result}")
    return result
