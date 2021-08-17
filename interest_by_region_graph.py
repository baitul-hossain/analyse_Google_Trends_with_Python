# Install pytrends -- pip install pytrends
# Install matplotlib -- pip install matplotlib

import pytrends

from pytrends.request import TrendReq

import pandas as pds

import matplotlib.pyplot as pplt

search_key = 'messi'

trend_init = TrendReq()

trend_init.build_payload(kw_list=[search_key])

data_trend = trend_init.interest_by_region()

data_trend = data_trend.sort_values(by=search_key, ascending=False)

data_trend = data_trend.head(20)

data_trend.reset_index().plot(x='geoName', y=search_key, figsize=(10,10), kind='bar')

pplt.title('Analysis data by region', fontweight='bold')

pplt.xlabel('Country')

pplt.ylabel('Trend')

pplt.show()
