from yfapi import YahooFinanceAPI, Interval
import datetime

if __name__ == '__main__':
    dh = YahooFinanceAPI(Interval.WEEKLY)
    now = datetime.datetime(2020, 6, 28)
    then = datetime.datetime(2020, 1, 1)
    df = dh.get_ticker_data("msft", then, now)

    dh.set_interval(Interval.MONTHLY)
    data_dict = dh.get_data_for_tickers(['aapl', 'msft', 'amzn'], then, now)
    print(df)
    print(data_dict)
