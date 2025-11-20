from ..client import get_client
from ..utils.helpers import sleep_seconds
from ..utils.validator import validate_symbol, validate_side, validate_quantity
from ..utils.logger import get_logger

logger = get_logger("twap")

def twap_execute(symbol, side, total_qty, slices=5, delay=2):
    validate_symbol(symbol)
    side = validate_side(side)
    total_qty = validate_quantity(total_qty)

    qty_per_order = total_qty / slices
    client = get_client()

    results = []
    for i in range(slices):
        res = client.place_market_order(symbol, side, qty_per_order)
        logger.info(f"TWAP Slice {i+1}/{slices}: {res}")
        results.append(res)

        if i < slices - 1:
            sleep_seconds(delay)

    return results
