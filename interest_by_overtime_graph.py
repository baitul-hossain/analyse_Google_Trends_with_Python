# Install pytrends -- pip install pytrends
# Install matplotlib -- pip install matplotlib

import pytrends

from pytrends.request import TrendReq

import pandas as pds

import matplotlib.pyplot as pplt

search_key = 'messi'

trend_init = TrendReq(hl='en_Us', tz=360)

trend_init.build_payload(kw_list=[search_key])

data_trend = trend_init.interest_over_time()

data_trend = data_trend.sort_values(by=search_key, ascending=False)

data_trend = data_trend.head(20)

data_trend.reset_index().plot(x='date', y=search_key, figsize=(8,6), kind='bar')

pplt.title('Analysis data over time', fontweight='bold')

pplt.xlabel('Year')

pplt.ylabel('Trend')

pplt.show()
