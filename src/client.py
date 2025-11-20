from .config import MOCK
from .utils.logger import get_logger

logger = get_logger("client")

class MockClient:
    """Fake orders (safe for testing)."""

    def __init__(self):
        self.orders = {}
        self.order_id = 1000

    def place_market_order(self, symbol, side, qty):
        self.order_id += 1
        order = {
            "orderId": self.order_id,
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "qty": qty,
            "status": "FILLED"
        }
        self.orders[self.order_id] = order
        logger.info(f"MOCK MARKET ORDER: {order}")
        return order

    def place_limit_order(self, symbol, side, qty, price):
        self.order_id += 1
        order = {
            "orderId": self.order_id,
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "qty": qty,
            "price": price,
            "status": "NEW"
        }
        self.orders[self.order_id] = order
        logger.info(f"MOCK LIMIT ORDER: {order}")
        return order

    def place_stop_limit_order(self, symbol, side, qty, stop_price, limit_price):
        self.order_id += 1
        order = {
            "orderId": self.order_id,
            "symbol": symbol,
            "side": side,
            "type": "STOP_LIMIT",
            "qty": qty,
            "stop_price": stop_price,
            "limit_price": limit_price,
            "status": "NEW"
        }
        self.orders[self.order_id] = order
        logger.info(f"MOCK STOP-LIMIT ORDER: {order}")
        return order


def get_client():
    # ALWAYS MOCK unless API key + MOCK_MODE=false
    return MockClient()
