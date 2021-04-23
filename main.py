# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import datetime as dt
from scipy.stats import norm

class DataProvider:

    def __init__(self):

      # CSVを取得する
      df = pd.read_csv("data/tocom/2020-01.csv").query("col_3 == '11'")

      print(df)

    def get_datas(self):
        pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dp = DataProvider()


    # tickers = ['YHOH712'] # AAPL', 'PB', 'C', 'DIS']

    # weights = np.array([.25, .3, .15, .3])

    # initial_investment = 1000000

    # data = pdr.get_data_yahoo(tickers, start='2018-01-01', end=dt.date.today())['Close']
    # print(data)

    # 収益率の計算 (A2 - A1) / A1
    # returns = data.pct_change()

    # print(returns)

    # 共分散の計算
    # cov_matrix = returns.cov()
    # print(cov_matrix)

    # 収益率の平均
    # avg_rets = returns.mean()

    # ポートフォリオの平均
    # port_means = avg_rets.dot(weights)

    # ポートフォリオの標準偏差
    # port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

    # 投資に対する平均値
    # mean_investment = (1 + port_means) * initial_investment

    # 投資に対する標準偏差
    # stdev_investment = initial_investment * port_stdev

    # 信頼区間
    # conf_level1 = 0.05

    # cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

    # var_ld1 = initial_investment - cutoff1

    # print(var_ld1)

    # print_hi('PyCharm')

# See PyCharm help at dddddhttps://www.jetbrains.com/help/pycharm/
