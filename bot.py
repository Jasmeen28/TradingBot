# bot.py
from binance import Client, enums
from binance.exceptions import BinanceAPIException, BinanceOrderException
import config # Import our config file
import logging

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("bot.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

class BasicBot:
    def __init__(self, testnet=True):
        self.api_key = config.API_KEY
        self.api_secret = config.API_SECRET

        if testnet:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            # This is CRITICAL for testnet futures
            self.client.FUTURES_URL = config.BASE_URL 
            logger.info("Initialized bot in TESTNET mode.")
        else:
            # This is for a real account (don't use yet!)
            self.client = Client(self.api_key, self.api_secret)
            logger.info("Initialized bot in LIVE mode.")

        self.check_connection()

    def check_connection(self):
        """Checks the connection and gets account info."""
        try:
            account_info = self.client.futures_account_balance()
            logger.info("Connection successful. Account balance retrieved.")
            # You could print some balance info here if you want
            # For example, find the USDT balance
            for asset in account_info:
                if asset['asset'] == 'USDT':
                    logger.info(f"USDT Balance: {asset['balance']}")
                    break
        except BinanceAPIException as e:
            logger.error(f"Error connecting to Binance API: {e}")
            raise # Stop the bot if we can't connect
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise
    # ... (inside the BasicBot class, after check_connection) ...

    def place_market_order(self, symbol, side, quantity):
        """Places a market order.
        :param symbol: e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param quantity: float or string, e.g., 0.001
        """
        try:
            # Convert side to Binance enum
            order_side = enums.SIDE_BUY if side.upper() == 'BUY' else enums.SIDE_SELL
            
            logger.info(f"Placing MARKET {side} order for {quantity} {symbol}...")
            
            order = self.client.futures_create_order(
                symbol=symbol,
                side=order_side,
                type=enums.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            
            logger.info("Market order placed successfully:")
            logger.info(order)
            return order
            
        except BinanceAPIException as e:
            logger.error(f"API Error placing market order: {e}")
            return None
        except BinanceOrderException as e:
            logger.error(f"Order Error placing market order: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        """Places a limit order.
        :param symbol: e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param quantity: float or string, e.g., 0.001
        :param price: float or string, e.g., 50000
        """
        try:
            # Convert side to Binance enum
            order_side = enums.SIDE_BUY if side.upper() == 'BUY' else enums.SIDE_SELL
            
            logger.info(f"Placing LIMIT {side} order for {quantity} {symbol} @ {price}...")
            
            order = self.client.futures_create_order(
                symbol=symbol,
                side=order_side,
                type=enums.ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=enums.TIME_IN_FORCE_GTC  # Good 'Til Canceled
            )
            
            logger.info("Limit order placed successfully:")
            logger.info(order)
            return order

        except BinanceAPIException as e:
            logger.error(f"API Error placing limit order: {e}")
            return None
        except BinanceOrderException as e:
            logger.error(f"Order Error placing limit order: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error placing limit order: {e}")
            return None