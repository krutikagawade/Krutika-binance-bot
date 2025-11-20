from ..client import get_client
from ..utils.validator import validate_symbol, validate_side, validate_quantity, validate_price
from ..utils.logger import get_logger

logger = get_logger("stop_limit")

def place_stop_limit(symbol, side, qty, stop_price, limit_price):
    validate_symbol(symbol)
    side = validate_side(side)
    qty = validate_quantity(qty)
    stop_price = validate_price(stop_price)
    limit_price = validate_price(limit_price)

    client = get_client()
    result = client.place_stop_limit_order(symbol, side, qty, stop_price, limit_price)
    logger.info(f"STOP-LIMIT Result: {result}")

    return result
