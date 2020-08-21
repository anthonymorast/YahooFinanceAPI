# YahooFinanceAPI

YahooFinanceAPI is a small wrapper that is meant solely to retrieve historical data from Yahoo Finance.

## Installation
```
  pip install YahooFinanceAPI
```

## Functions

The function declarations for the limited functionality are listed below with
comments.

```python
# reset the data frequency (daily, weekly, or monthly) the Interval
# class allows access to class variables that define these intervals, i.e.
# Interval.WEEKLY, Interval.MONTHLY, and Interval.DAILY
set_interval(interval)

# Retrieve data for one ticker from start_date to end_date.
# ticker is a string and start_date and end_date are python datetimes.
# This function returns a Pandas dataframe.
get_ticker_data(ticker, start_date, end_date)

# Retrieve data for a list of tickers.
# tickers -> list of strings, start_date and end_date -> datatimes
# Returns a dictionary taking the ticker symbol to a Pandas dataframe
get_data_for_tickers(tickers, start_date, end_date)
```

## Usage

Acceptable intervals are *1d* (default), *1wk*, and *1mo*. The API only offers the
ability to retrieve data for a ticker or a list of tickers. The results are returned
 as a Pandas dataframe and include the following columns:

```
Date
Open
High
Low
Close
Adj Close
Volume
```

Example usage, as seen in *example.py*:

```python
from yfapi import YahooFinanceAPI, Interval

# instantiate the API and set the interval to weekly data
dh = YahooFinanceAPI(Interval.WEEKLY)
now = datetime.datetime(2020, 6, 28)
then = datetime.datetime(2020, 1, 1)

# returns dataframe holding the historical data
df = dh.get_ticker_data("msft", then, now)

# reset the data interval to monthly
dh.set_interval(Interval.MONTHLY)
# returns results as a dictionary: ticker -> dataframe
data_dict = dh.get_data_for_tickers(['msft', 'aapl', 'amzn'], then, now)
```
