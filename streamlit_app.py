import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.title('SMA Crossover Backtest App')

# User input for the stock ticker
stock_ticker = st.text_input('Enter the stock ticker (e.g., "AAPL"):')

# User inputs for short-term and long-term windows
short_window = st.number_input('Enter short SMA window', value=20)
long_window = st.number_input('Enter long SMA window', value=50)

# Backtest button
if st.button('Backtest Strategy'):
    if stock_ticker and short_window and long_window:
        # Fetch historical data from Yahoo Finance
        data = yf.download(stock_ticker, start='2010-01-01', end='2020-12-31')

        if not data.empty:
            # Calculate short and long-term SMA
            data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
            data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

            # Signal for long (1) if short_mavg is above long_mavg
            data['signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)

            # Difference of signals to find the crossover points
            data['positions'] = data['signal'].diff()

            # Plot the closing price and moving averages
            st.line_chart(data[['Close', 'short_mavg', 'long_mavg']])

            # Show the points where the strategy would buy
            st.write(data[data['positions'] == 1])

            # Compute the portfolio's performance
            data['returns'] = data['Close'].pct_change()
            data['strategy_returns'] = data['returns'] * data['signal'].shift(1)
            cumulative_strategy_returns = (data['strategy_returns'] + 1).cumprod()

            # Plot cumulative strategy returns
            st.line_chart(cumulative_strategy_returns)

            # Show final backtest results
            st.metric(label="Strategy Performance", value=f"{cumulative_strategy_returns.iloc[-1] - 1:.2%}")
        else:
            st.error('Error: Could not fetch data for the provided ticker.')
    else:
        st.error('Please enter a stock ticker and SMA windows.')

