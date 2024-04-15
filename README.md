
# SMA Crossover Backtest App

This is a Streamlit application that allows users to backtest a simple moving average (SMA) crossover trading strategy using historical stock data from Yahoo Finance.

## Overview

The SMA crossover strategy generates buy signals when a short-term SMA crosses above a long-term SMA and sell signals when the short-term SMA crosses below the long-term SMA. This application provides a basic simulation of how this strategy would have performed historically for a given stock.

## Installation

To run this application, you'll need Python installed on your system. This app was built using Python 3.8, but it should be compatible with other Python 3 versions.

### Setting Up a Virtual Environment

It's recommended to run Python applications in a virtual environment. To set one up, navigate to the project's root directory in your terminal and run:

```bash
python -m venv venv
```

Activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```

On Windows:
```bash
.\venv\Scripts\activate
```

### Installing Dependencies

With your virtual environment activated, install the required packages using pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```
streamlit
yfinance
pandas
numpy
```

## Usage

To start the application, run the following command in the root directory of the project:

```bash
streamlit run streamlit_app.py
```

The Streamlit interface will open in your default web browser.

### Using the App

1. Enter the stock ticker symbol (e.g., "AAPL" for Apple Inc.) in the input box.
2. Specify the short-term and long-term SMA windows (e.g., 20 and 50).
3. Click "Backtest Strategy" to see the historical price chart with SMA lines and backtest results.

## Disclaimer

The SMA Crossover Backtest App is for informational purposes only and does not constitute financial advice. Past performance is not indicative of future results. Please do your own research before executing any trades.


