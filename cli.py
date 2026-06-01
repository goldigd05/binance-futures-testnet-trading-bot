import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and args.price is None:
            raise ValueError(
                "Price is required for LIMIT order"
            )

        client = get_client()

        print("\n===== ORDER REQUEST =====")

        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if args.price:
            print(f"Price    : {args.price}")

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            args.price
        )

        print("\n===== ORDER RESPONSE =====")

        print(
            f"Order ID     : {response.get('orderId')}"
        )

        print(
            f"Status       : {response.get('status')}"
        )

        print(
            f"Executed Qty : {response.get('executedQty')}"
        )

        if "avgPrice" in response:
            print(
                f"Avg Price    : {response.get('avgPrice')}"
            )

        print("\nSUCCESS")

    except Exception as e:

        print("\nFAILED")
        print(str(e))


if __name__ == "__main__":
    main()