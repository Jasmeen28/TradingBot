# main.py
from bot import BasicBot, logger

def main_menu():
    """Displays the main menu and gets user input."""
    print("\n--- 🤖 Binance Futures Bot ---")
    print("1: Place Market Order")
    print("2: Place Limit Order")
    print("3: Check Account Balance")
    print("q: Quit")
    return input("What would you like to do? ")

def get_market_order_input():
    """Gets user input for a market order."""
    try:
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Enter side (BUY or SELL): ").upper()
        quantity = float(input("Enter quantity (e.g., 0.001): "))

        if side not in ['BUY', 'SELL']:
            logger.warning("Invalid side. Must be 'BUY' or 'SELL'.")
            return None
        return symbol, side, quantity
    except ValueError:
        logger.warning("Invalid quantity. Please enter a number.")
        return None

def get_limit_order_input():
    """Gets user input for a limit order."""
    try:
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Enter side (BUY or SELL): ").upper()
        quantity = float(input("Enter quantity (e.g., 0.001): "))
        price = float(input(f"Enter limit price in USDT: "))

        if side not in ['BUY', 'SELL']:
            logger.warning("Invalid side. Must be 'BUY' or 'SELL'.")
            return None
        return symbol, side, quantity, price
    except ValueError:
        logger.warning("Invalid input. Please enter a number for quantity/price.")
        return None

if __name__ == "__main__":
    try:
        # Initialize the bot
        # We explicitly set testnet=True for safety
        bot = BasicBot(testnet=True) 

        while True:
            choice = main_menu()

            if choice == '1':
                # Place Market Order
                order_details = get_market_order_input()
                if order_details:
                    symbol, side, quantity = order_details
                    bot.place_market_order(symbol, side, quantity)

            elif choice == '2':
                # Place Limit Order
                order_details = get_limit_order_input()
                if order_details:
                    symbol, side, quantity, price = order_details
                    bot.place_limit_order(symbol, side, quantity, price)

            elif choice == '3':
                # Check connection (which also prints balance)
                bot.check_connection()

            elif choice.lower() == 'q':
                logger.info("Exiting bot. Goodbye!")
                break

            else:
                logger.warning("Invalid choice. Please try again.")

    except Exception as e:
        logger.error(f"Bot failed to start: {e}")