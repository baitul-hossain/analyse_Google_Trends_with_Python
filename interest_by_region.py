# Install pytrends -- pip install pytrends

import pytrends

from pytrends.request import TrendReq

import pandas as pds

search_key = 'messi'

trend_init = TrendReq()

trend_init.build_payload(kw_list=[search_key])

data_trend = trend_init.interest_by_region()

data_trend = data_trend.sort_values(by=search_key, ascending=False)

data_trend = data_trend.head(20)

print(data_trend)