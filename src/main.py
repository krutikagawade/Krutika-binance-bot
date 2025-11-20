import argparse
from .market_orders import place_market
from .limit_orders import place_limit
from .advanced.stop_limit import place_stop_limit
from .advanced.oco import place_oco
from .advanced.twap import twap_execute
from .advanced.grid_strategy import create_grid_orders

def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")
    sub = parser.add_subparsers(dest="cmd")

    # MARKET
    p1 = sub.add_parser("market")
    p1.add_argument("symbol")
    p1.add_argument("side")
    p1.add_argument("qty")

    # LIMIT
    p2 = sub.add_parser("limit")
    p2.add_argument("symbol")
    p2.add_argument("side")
    p2.add_argument("qty")
    p2.add_argument("price")

    # STOP-LIMIT
    p3 = sub.add_parser("stoplimit")
    p3.add_argument("symbol")
    p3.add_argument("side")
    p3.add_argument("qty")
    p3.add_argument("stop_price")
    p3.add_argument("limit_price")

    # OCO
    p4 = sub.add_parser("oco")
    p4.add_argument("symbol")
    p4.add_argument("side")
    p4.add_argument("qty")
    p4.add_argument("--tp")
    p4.add_argument("--sl")

    # TWAP
    p5 = sub.add_parser("twap")
    p5.add_argument("symbol")
    p5.add_argument("side")
    p5.add_argument("qty")
    p5.add_argument("--slices", default=5, type=int)
    p5.add_argument("--delay", default=2, type=int)

    # GRID
    p6 = sub.add_parser("grid")
    p6.add_argument("symbol")
    p6.add_argument("low")
    p6.add_argument("high")
    p6.add_argument("levels", type=int)
    p6.add_argument("qty_each")

    args = parser.parse_args()

    if args.cmd == "market":
        print(place_market(args.symbol, args.side, args.qty))

    elif args.cmd == "limit":
        print(place_limit(args.symbol, args.side, args.qty, args.price))

    elif args.cmd == "stoplimit":
        print(place_stop_limit(args.symbol, args.side, args.qty, args.stop_price, args.limit_price))

    elif args.cmd == "oco":
        print(place_oco(args.symbol, args.side, args.qty, args.tp, args.sl))

    elif args.cmd == "twap":
        print(twap_execute(args.symbol, args.side, args.qty, args.slices, args.delay))

    elif args.cmd == "grid":
        print(create_grid_orders(args.symbol, args.low, args.high, args.levels, args.qty_each))

if __name__ == "__main__":
    main()
