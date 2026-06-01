# Binance Futures Testnet Trading Bot

## Overview

A Python-based trading bot for Binance Futures Testnet (USDT-M) that allows users to place Market and Limit orders through both a Command Line Interface (CLI) and a lightweight Streamlit web interface.

The project demonstrates API integration, input validation, error handling, logging, and modular software design.

---

## Features

### Core Features

* Place Market Orders
* Place Limit Orders
* Support BUY and SELL sides
* Input validation
* Error handling
* API request and response logging
* Modular project structure

### Bonus Features

* Streamlit-based lightweight web UI
* Enhanced user experience for order placement
* Reusable backend architecture

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Technologies Used

* Python 3.x
* Binance Futures API (Testnet)
* python-binance
* Streamlit
* dotenv
* logging

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Running the CLI Application

### Market Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Limit Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Running the Streamlit UI

Launch the web interface:

```bash
streamlit run app.py
```

The UI allows users to:

* Enter trading symbol
* Select BUY or SELL
* Choose MARKET or LIMIT order
* Enter quantity
* Enter price for LIMIT orders
* Submit orders directly to Binance Futures Testnet

---

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading_bot.log
```

This helps with debugging and monitoring application activity.

---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Invalid quantity values
* Missing LIMIT order price
* Binance API errors
* Network-related exceptions

---

## Assumptions

* Binance Futures Testnet account is available.
* Valid Testnet API credentials are configured.
* Orders are executed only on Binance Futures Testnet.
* Internet connection is available during execution.

---

## Sample Output

```text
===== ORDER REQUEST =====

Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

===== ORDER RESPONSE =====

Order ID     : 13706276296
Status       : NEW
Executed Qty : 0.0000

SUCCESS
```

---

## Author

Goldi Gond

Python Developer Internship Assignment Submission
