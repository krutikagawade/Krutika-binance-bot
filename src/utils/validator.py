from decimal import Decimal, InvalidOperation

def validate_symbol(symbol):
    return isinstance(symbol, str) and len(symbol) >= 4

def validate_side(side):
    s = side.upper()
    if s in ("BUY", "SELL"):
        return s
    raise ValueError("Side must be BUY or SELL")

def validate_quantity(q):
    try:
        qty = Decimal(str(q))
    except InvalidOperation:
        raise ValueError("Invalid quantity")
    if qty <= 0:
        raise ValueError("Quantity must be > 0")
    return float(qty)

def validate_price(p):
    try:
        price = Decimal(str(p))
    except InvalidOperation:
        raise ValueError("Invalid price")
    if price <= 0:
        raise ValueError("Price must be > 0")
    return float(price)
