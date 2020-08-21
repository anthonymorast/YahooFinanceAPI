import datetime
import time
import pandas as pd

class YahooFinanceAPI(object):
    def __init__(self, interval="1d"):
        # 3M Example: "https://query1.finance.yahoo.com/v7/finance/download/MMM?period1=1434844800&period2=1592697600&interval=1d&events=history"
        self.base_url = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_time}&period2={end_time}&interval={interval}&events=history"
        self.interval = interval

    def __build_url(self, ticker, start_date, end_date):
        return self.base_url.format(ticker=ticker, start_time=start_date, end_time=end_date, interval=self.interval)

    def set_interval(self, interval):
        """
            Set data frequency
        """
        self.interval = interval

    def get_ticker_data(self, ticker, start_date, end_date):
        """
            ticker (string) - ticker symbol
            start_date (datetime) - start date of historical data
            end_date (datetime) - final date for historical data
        """
        # must pass datetime into this function
        epoch_start = int(time.mktime(start_date.timetuple()))
        epoch_end = int(time.mktime(end_date.timetuple()))

        df =  pd.read_csv(self.__build_url(ticker, epoch_start, epoch_end))
        df.Date = pd.to_datetime(df.Date, format="%Y-%m-%d")

        return df

    def get_data_for_tickers(self, tickers, start_date, end_date):
        """
            tickers (list) - list of ticker symbols
            start_date (datetime) - start date of historical data
            end_date (datetime) - final date for historical data
        """
        data_dict = {}
        for ticker in tickers:
            data_dict[ticker] = self.get_ticker_data(ticker, start_date, end_date)
        return data_dict


if __name__ == '__main__':
    dh = YahooFinanceAPI()
    now = datetime.datetime(2020, 6, 28)
    then = datetime.datetime(2020, 1, 1)
    df = dh.get_ticker_data("msft", then, now)
    data_dict = dh.get_data_for_tickers(['msft', 'aapl', 'amzn'], then, now)
    print(df)
    print(data_dict)
