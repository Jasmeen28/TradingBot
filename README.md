# Python Trading Bot for Binance Futures

This is a simple, command-line-based trading bot built in Python. It connects to the Binance Futures (USDT-M) **Testnet**, allowing you to place and manage orders without using real money.

## 🚀 Core Features

* **Place Orders:** Supports placing both Market and Limit orders.
* **Order Sides:** Full support for both Buy (Long) and Sell (Short) orders.
* **Safe:** Built to connect to the Binance Testnet by default.
* **Interactive CLI:** A simple command-line interface (CLI) for placing orders and checking your balance.
* **Logging:** All API requests, responses, and errors are logged to `bot.log` for easy debugging.

## 🛠️ Technology Stack

* **Python 3**
* **`python-binance`:** The official Binance library for an easy API connection.
* **Binance Futures REST API:** Used for all authenticated endpoints.
* **Logging:** Python's built-in logging module.

## ⚙️ Setup and Installation

Follow these steps to get the bot running on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
cd your-repo-name