from ..client import get_client
from ..utils.validator import validate_symbol, validate_side, validate_quantity, validate_price
from ..utils.logger import get_logger

logger = get_logger("oco")

def place_oco(symbol, side, qty, tp_price, sl_price):
    validate_symbol(symbol)
    side = validate_side(side)
    qty = validate_quantity(qty)
    tp_price = validate_price(tp_price)
    sl_price = validate_price(sl_price)

    client = get_client()

    tp_order = client.place_limit_order(symbol, side, qty, tp_price)
    sl_order = client.place_stop_limit_order(symbol, side, qty, sl_price, sl_price)

    logger.info(f"OCO => TP: {tp_order}, SL: {sl_order}")

    return {"take_profit": tp_order, "stop_loss": sl_order}
